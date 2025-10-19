import discord
from discord.ext import commands

TOKEN =
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Salut {ctx.author.mention} 👋 ! Je suis en ligne !")

@bot.command()
async def info(ctx):
    await ctx.send("Je suis un bot Discord créé avec Python 🐍 !")

bot.run(TOKEN)
