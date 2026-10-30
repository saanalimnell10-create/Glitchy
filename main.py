import os
import asyncio
import traceback
import discord
from discord.ext import commands
from keep_alive import keep_alive

# Määritetään intentit
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Funktio dynaamiselle prefixille (tuki botin omalle maininnalle + oletusmerkille "!
def get_prefix(bot, message):
    # Tähän voidaan myöhemmin liittää tietokannan haku serverikohtaiselle prefixille
    base_prefixes = ["!", "?"] # Voit lisätä tähän haluamasi prefixit, esim. "!" ja "?"
    return commands.when_mentioned_or(*base_prefixes)(bot, message)

# Luodaan botti käyttäen get_prefix-funktiota
bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("> [SYSTEM_OVERLOAD]: Glitchy core online. ⚡")

async def load_extensions():
    if not os.path.exists("./cogs"):
        print("⚠️ Varoitus: 'cogs'-kansiota ei löytynyt vielä!")
        return

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"cogs.{cog_name}")
                print(f"✅ Ladattu cog: {filename}")
            except Exception as e:
                print(f"❌ Virhe ladattaessa cogia {filename}:")
                traceback.print_exc()

async def main():
    async with bot:
        await load_extensions()
        TOKEN = os.getenv("DISCORD_TOKEN")
        
        if TOKEN:
            await bot.start(TOKEN)
        else:
            print("❌ Virhe: DISCORD_TOKENia ei löytynyt ympäristömuuttujista!")

if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
