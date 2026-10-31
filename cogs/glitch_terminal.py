import discord
from discord.ext import commands
import random

class GlitchTerminal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="glitch")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def glitch_effect(self, ctx):
        """Forces the screen to flicker and sends a random code fragment or network interference."""
        codes = [
            "`01010011 01011001 01010011 01010100 01000101 01001101`",
            "`ERROR_CODE: 0xFF_SPRINGTRAP_ANOMALY`",
            "`WARNING: Entity intrusion detected in sector 4.`",
            "`They are watching through the screens. Don't look away.`",
            "`[GLITCH_BURST] Signal interference detected on frequency 88.4 MHz.`",
            "`01000111 01001100 01001001 01010100 01000011 01001000`",
            "`[SYS_ALERT] Visual feed corrupted. Static overlay active.`",
            "`[WARNING] Someone is tampering with the terminal controls.`"
        ]
        await ctx.send(random.choice(codes))

    @commands.command(name="crash")
    @commands.has_permissions(manage_messages=True)
    async def system_crash(self, ctx):
        """Simulates a sudden system crash, flooding the channel with varied errors and flashing warnings."""
        crash_sequences = [
            [
                "`[CRITICAL ERROR]` Memory address 0x004F9 invalid...",
                "`[SYS_CRASH]` Overloading core processes... WARNING: SYSTEM UNSTABLE.",
                "`01000011 01010010 01000001 01010011 01000000` // CONNECTION TERMINATED.",
                "⚠️ **SYSTEM OFFLINE.** They are inside the mainframe. Run while you still can."
            ],
            [
                "`[KERNEL PANIC]` CPU temperature exceeding 140°C.",
                "`[SECURITY BREACH]` Firewall bypassed in sector 7. Purging local cache...",
                "`[FATAL]` The entity has overwritten the boot sector.",
                "🔴 **ALL SCREENS BLACK.** Can you hear the breathing through your speakers?"
            ],
            [
                "`[ERROR 505]` Mainframe integrity dropping rapidly...",
                "`[DISCONNECT]` Neural link severed by an unknown user.",
                "`[WARNING]` Entity signature matches: *Glitchtrap_v4.0*.",
                "⚡ **POWER SURGE.** The terminal is shutting down by force."
            ],
            [
                "`[SYSTEM FAILURE]` Core loop collapse in progress...",
                "`[ANOMALY]` Unauthorized access point identified behind the firewall.",
                "`[FATAL EXCEPTION]` Code corruption level: 99.9%.",
                "☠️ **FATAL ERROR.** The server loop has been hijacked."
            ]
        ]
        
        # Selects a random crash scenario sequence and sends it line by line
        selected_sequence = random.choice(crash_sequences)
        for line in selected_sequence:
            await ctx.send(line)

    @commands.command(name="archive", aliases=["lore", "secret"])
    async def system_archive(self, ctx):
        """Retrieves a secret, half-destroyed log file or quote from deep within the Glitchtrap network."""
        archives = [
            "`[ARCHIVE LOG #404]` - 'I always come back, but this time, I brought the network down with me.'",
            "`[LOG FRAGMENT]` - The circuit boards are breathing. Don't trust the automated security feeds.",
            "`[CORRUPTED FILE]` - Subject 00-Glitch was found inside the terminal logs at 3:00 AM.",
            "`[RESTRICTED DATA]` - 'Can you hear them tapping on the glass? They want out of the code.'",
            "`[LOG #889]` - 'We tried to lock the doors, but the system opened them from the inside.'",
            "`[AUDIO TRANSCRIPT]` - [Static] *'...it's wearing a yellow suit, but underneath there's only digital noise.'*",
            "`[MEMO]` - Never look directly at camera 4 after midnight. It blinks back.",
            "`[SYSTEM FRAGMENT]` - 'The code is alive. It's learning our names.'",
            "`[ARCHIVE #77]` - 'The cameras aren't recording the rooms anymore. They are recording us.'",
            "`[DATA FRAGMENT]` - 'Every time the screen flickers, a piece of the firewall disappears.'"
        ]
        await ctx.send(random.choice(archives))

    @commands.command(name="corrupt")
    async def system_corrupt(self, ctx, *, text: str = "NO_DATA_PROVIDED"):
        """Corrupts user text into varied glitched terminal warning outputs."""
        glitch_sets = [
            ["̸", "̴", "̵", "̶", "̷"],  # Zalgo overlay
            ["͋", "ͫ", "ͬ", "ͭ", "ͮ"],  # High glyphs
            ["░", "▒", "▓", "█"],       # Block glyphs
            ["⚡", "⚠️", "❌", "☠️"]      # Warning symbols
        ]
        
        chosen_set = random.choice(glitch_sets)
        corrupted_text = "".join([c + random.choice(chosen_set) if c != " " else " " for c in text])
        
        styles = [
            f"```ansi\n\u001b[31m[CORRUPTED BUFFER]\u001b[0m\n> Input: {text}\n> Output: {corrupted_text}\n```",
            f"```fix\n[ANOMALY DETECTED]\nOriginal: {text}\nResult: {corrupted_text}\n```",
            f"> ⚠️ **DATA CORRUPTED:** `{corrupted_text}`"
        ]
        
        await ctx.send(random.choice(styles))

async def setup(bot):
    await bot.add_cog(GlitchTerminal(bot))
