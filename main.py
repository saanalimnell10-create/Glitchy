import discord
from discord.ext import commands
import os
import asyncio
from flask import Flask
from threading import Thread

# Flask app to keep the Render port alive
app = Flask('')

@app.route('/')
def home():
    return "System Overload is online and running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_flask, daemon=True)
    t.start()

# Bot intents configuration
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Initialize bot with the '::' prefix and intents
bot = commands.Bot(command_prefix="::", intents=intents)

@bot.event
async def on_ready():
    print("-----------------------------------")
    print(f"> Logged in as: {bot.user}")
    print(f"> ID: {bot.user.id}")
    print(f"> Cyber-noir terminal online. Prefix: :: | Slash: /")
    print("-----------------------------------")

    # Automatically load cogs from the ./cogs directory
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f"cogs.{cog_name}")
                print(f"✅ Loaded cog: {cog_name}")
            except Exception as e:
                print(f"❌ Failed to load cog {cog_name}: {e}")

    # Synchronize Slash commands with Discord
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"❌ Failed to sync slash commands: {e}")

async def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Error: DISCORD_TOKEN environment variable is missing!")
        return
    
    # Start Flask background server for Render
    keep_alive()
    
    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
