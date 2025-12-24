import discord
from discord.ext import commands
import random
import asyncio
import os

TOKEN = os.getenv("TOKEN")

GUILD_ID = 893516392509354035  # PUT YOUR SERVER ID HERE

ROLE_IDS = [
    1453431403084644375,  # ROLE 1
    1453431627274522675,  # ROLE 2
    1453431804684927016   # ROLE 3
]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def randomroles(ctx):
    guild = bot.get_guild(GUILD_ID)
    roles = [guild.get_role(rid) for rid in ROLE_IDS]

    await ctx.send("⏳ Assigning random roles...")

    for member in guild.members:
        if member.bot:
            continue

        for r in roles:
            if r in member.roles:
                await member.remove_roles(r)

        role = random.choice(roles)
        try:
            await member.add_roles(role)
            await asyncio.sleep(1)
        except:
            pass

    await ctx.send("✅ Done!")

bot.run(TOKEN)
