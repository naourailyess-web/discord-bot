import discord
from discord.ext import commands
import random
import os

TOKEN = os.getenv("TOKEN")

# ⬇️ ajoute "help_command=None" ici pour désactiver le help intégré
bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

# Quand le bot se connecte
@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")
    await bot.change_presence(activity=discord.Game(name="créer le meilleur bot du monde 🌍"))

# Commande help
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="📜 Commandes du Bot",
        description="""
**!help** → Affiche cette liste  
**!ping** → Teste la connexion  
**!info** → Donne des infos sur le serveur  
**!say [texte]** → Le bot répète ton message  
**!meme** → Envoie un meme aléatoire 😎
""",
        color=discord.Color.blurple()
    )
    await ctx.send(embed=embed)

# Commande ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong ! Latence : {round(bot.latency * 1000)}ms")

# Commande info
@bot.command()
async def info(ctx):
    server = ctx.guild
    embed = discord.Embed(
        title=f"ℹ️ Infos sur {server.name}",
        color=discord.Color.green()
    )
    embed.add_field(name="👑 Propriétaire", value=server.owner, inline=False)
    embed.add_field(name="👥 Membres", value=server.member_count, inline=False)
    embed.add_field(name="🆔 ID", value=server.id, inline=False)
    await ctx.send(embed=embed)

# Commande say
@bot.command()
async def say(ctx, *, message: str):
    await ctx.message.delete()
    await ctx.send(message)

# Commande meme
@bot.command()
async def meme(ctx):
    memes = [
        "https://i.imgflip.com/4/1bij.jpg",
        "https://i.imgflip.com/30b1gx.jpg",
        "https://i.imgflip.com/26am.jpg",
        "https://i.imgflip.com/3si4.jpg"
    ]
    await ctx.send(random.choice(memes))

# Réponses automatiques simples
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    if "bonjour" in msg:
        await message.channel.send("Salut 👋 ! Comment tu vas ?")
    elif "ça va" in msg:
        await message.channel.send("Moi ça va nickel 😎 et toi ?")
    elif "t ki" in msg or "t'es qui" in msg:
        await message.channel.send("Je suis le meilleur bot du monde 🤖🔥")
    elif "je t'aime" in msg:
        await message.channel.send("Aww 🥰 moi aussi je t’aime !")
    elif "tg" in msg:
        await message.channel.send("😡 Pas gentil ça.")
    else:
        await bot.process_commands(message)

bot.run(TOKEN)





