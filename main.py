import discord
from discord.ext import commands
import os
import asyncio
from cogs.prefix import get_prefix

# Määritellään botin oikeudet (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Vaaditaan, että botti näkee viestit
intents.guilds = True

# Luodaan botti käyttäen dynaamista prefixiä
bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"-----------------------------------")
    print(f"> Botti kirjautunut sisään: {bot.user}")
    print(f"> ID: {bot.user.id}")
    print(f"> Kyber-noir terminaali valmiina.")
    print(f"-----------------------------------")

    # Ladataan kaikki cogs-kansiossa olevat moduulit automaattisesti
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"cogs.{cog_name}")
                print(f"✅ Ladattu cog: {cog_name}")
            except Exception as e:
                print(f"❌ Virhe ladatessa cogia {cog_name}: {e}")

# Käynnistetään botti ympäristömuuttujasta löytyvällä tokenilla
# Varmista, että Renderissä tai .env-tiedostossa on DISCORD_TOKEN
async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Virhe: DISCORD_TOKEN-ympäristömuuttuja puuttuu!")
        return
    
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
