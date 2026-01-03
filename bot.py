import discord
from discord.ext import commands
import os

# ================== CONFIG ==================

TOKEN = os.getenv("TOKEN")  # Your bot token

# ================== INTENTS ==================

intents = discord.Intents.default()
intents.message_content = True  # REQUIRED for prefix commands

bot = commands.Bot(command_prefix="*", intents=intents)

# ================== EVENTS ==================

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

# ================== COMMAND ==================

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Njan evide ind WORKING !")

# ================== RUN ==================

bot.run(TOKEN)
