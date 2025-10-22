import discord
from discord.ext import commands
import os
import requests

TOKEN = os.getenv("TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Salut {ctx.author.mention} 👋 ! Je suis en ligne !")

@bot.command()
async def chat(ctx, *, message):
    """Commande IA : le bot répond comme ChatGPT."""
    await ctx.trigger_typing()
    
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    data = {"inputs": message}
    
    response = requests.post(
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers=headers, json=data
    )

    if response.status_code == 200:
        bot_reply = response.json()[0]["generated_text"]
        await ctx.send(bot_reply)
    else:
        await ctx.send("⚠️ Erreur lors de la génération de la réponse.")

bot.run(TOKEN)
