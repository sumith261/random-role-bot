import discord
from discord.ext import commands
import random
import asyncio
import os

# ================== CONFIG ==================

TOKEN = os.getenv("TOKEN")  # Bot token from environment variable

GUILD_ID = 893516392509354035  # Your server ID

ROLE_IDS = [
    1453431403084644375,  # Santa
    1453431627274522675,  # Snowman
    1453431804684927016   # Reindeer
]

ROLE_DELAY = 6  # seconds (safe for Discord rate limits)

# ================== INTENTS ==================

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================== EVENTS ==================

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

# ================== COMMAND ==================

@bot.command()
@commands.has_permissions(administrator=True)
async def randomroles(ctx):
    guild = bot.get_guild(GUILD_ID)

    if guild is None:
        await ctx.send("❌ Guild not found.")
        return

    roles = [guild.get_role(rid) for rid in ROLE_IDS if guild.get_role(rid)]

    if not roles:
        await ctx.send("❌ Roles not found.")
        return

    await ctx.send("⏳ Assigning **one random role per member**...")

    for member in guild.members:
        if member.bot:
            continue

        try:
            # Remove existing random roles
            for role in roles:
                if role in member.roles:
                    await member.remove_roles(role)
                    await asyncio.sleep(1)

            # Add exactly ONE random role
            new_role = random.choice(roles)
            await member.add_roles(new_role)

            # Delay to avoid rate limits
            await asyncio.sleep(ROLE_DELAY)

        except discord.Forbidden:
            print(f"❌ Missing permission for {member}")
        except discord.HTTPException as e:
            print(f"⚠️ HTTP error for {member}: {e}")
            await asyncio.sleep(10)  # extra cooldown on error
        except Exception as e:
            print(f"⚠️ Unexpected error for {member}: {e}")

    await ctx.send("✅ **Done! Everyone now has exactly ONE role.**")

# ================== RUN ==================

bot.run(TOKEN)
