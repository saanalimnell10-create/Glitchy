import discord
from discord.ext import commands
import os
import asyncio
from flask import Flask
from threading import Thread
from cogs.prefix import get_prefix

# Luodaan Flask-appi pitämään Renderin portti auki
app = Flask('')

@app.route('/')
def home():
    return "Glitchy is online and running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask, daemon=True)
    t.start()

# Discord-botin asetukset
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"-----------------------------------")
    print(f"> Botti kirjautunut sisään: {bot.user}")
    print(f"> ID: {bot.user.id}")
    print(f"> Kyber-noir terminaali valmiina.")
    print(f"-----------------------------------")

    # Ladataan cogs-kansion moduulit automaattisesti
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"cogs.{cog_name}")
                print(f"✅ Ladattu cog: {cog_name}")
            except Exception as e:
                print(f"❌ Virhe ladatessa cogia {cog_name}: {e}")

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Virhe: DISCORD_TOKEN-ympäristömuuttuja puuttuu!")
        return
    
    # Käynnistetään Flask taustalle kuuntelemaan porttia
    keep_alive()
    
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
