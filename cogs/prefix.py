import discord
from discord.ext import commands
import json
import os

# Tiedosto, johon servereiden omat prefixit tallennetaan
PREFIX_FILE = "prefixes.json"

def load_prefixes():
    if os.path.exists(PREFIX_FILE):
        with open(PREFIX_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_prefixes(prefixes):
    with open(PREFIX_FILE, "w") as f:
        json.dump(prefixes, f, indent=4)

def get_prefix(bot, message):
    if not message.guild:
        return "#"  # Oletus yksityisviesteissä
    prefixes = load_prefixes()
    return prefixes.get(str(message.guild.id), "#")  # Oletuksena käytetään nyt #

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setprefix", aliases=["prefix"])
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, new_prefix: str):
        """Vaihtaa botin prefixin tällä serverillä."""
        if len(new_prefix) > 5:
            await ctx.send("> [!] Prefix on liian pitkä (max 5 merkkiä).")
            return

        prefixes = load_prefixes()
        prefixes[str(ctx.guild.id)] = new_prefix
        save_prefixes(prefixes)

        await ctx.send(f"> [SYSTEM] Prefix vaihdettu onnistuneesti muotoon: `{new_prefix}`")

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("> [!] Vaadit Administrator-oikeudet vaihtaaksesi prefixiä.")

async def setup(bot):
    await bot.add_cog(Prefix(bot))
