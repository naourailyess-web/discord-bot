import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # récupère le token depuis Render

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Salut {ctx.author.mention} 👋 ! Je suis en ligne !")

bot.run(TOKEN)


