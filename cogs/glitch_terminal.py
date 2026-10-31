import discord
from discord.ext import commands
import random

class GlitchTerminal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="crash")
    @commands.has_permissions(manage_messages=True)
    async def system_crash(self, ctx):
        """Simulates a sudden system crash, flooding the channel with fake errors and flashing warnings."""
        crash_sequence = [
            "`[CRITICAL ERROR]` Memory address 0x004F9 invalid...",
            "`[SYS_CRASH]` Overloading core processes... WARNING: SYSTEM UNSTABLE.",
            "`01000011 01010010 01000001 01010011 01001000` // CONNECTION TERMINATED.",
            "⚠️ **SYSTEM OFFLINE.** They are inside the mainframe. Run while you still can."
        ]
        for line in crash_sequence:
            await ctx.send(line)

    @commands.command(name="archive", aliases=["lore", "secret"])
    async def system_archive(self, ctx):
        """Retrieves a secret, half-destroyed log file or quote from deep within the Glitchtrap network."""
        archives = [
            "`[ARCHIVE LOG #404]` - 'I always come back, but this time, I brought the network down with me.'",
            "`[LOG FRAGMENT]` - The circuit boards are breathing. Don't trust the automated security feeds.",
            "`[CORRUPTED FILE]` - Subject 00-Glitch was found inside the terminal logs at 3:00 AM.",
            "`[RESTRICTED DATA]` - 'Can you hear them tapping on the glass? They want out of the code.'"
        ]
        await ctx.send(random.choice(archives))

    @commands.command(name="corrupt")
    async def system_corrupt(self, ctx, *, text: str = "NO_DATA_PROVIDED"):
        """Corrupts user text into a glitched terminal warning output."""
        glitch_chars = ["̸", "̴", "̵", "̶", "̷", "͋", "ͫ", "ͬ", "ͭ", "ͮ"]
        corrupted_text = "".join([c + random.choice(glitch_chars) for c in text])
        
        response = (
            f"```ansi\n"
            f"\u001b[31m[CORRUPTED BUFFER]\u001b[0m\n"
            f"> Input: {text}\n"
            f"> Output: {corrupted_text}\n"
            f"```"
        )
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(GlitchTerminal(bot))
