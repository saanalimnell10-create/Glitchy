import discord
from discord.ext import commands
import random

class SystemArgsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="args")
    @commands.has_permissions(administrator=True)
    async def system_args(self, ctx):
        """Displays active system arguments, memory flags, and diagnostic errors."""
        diagnostic_outputs = [
            "`[DIAGNOSTICS]` Active flags: 0x89F4_GLITCH // Memory integrity: 78.4% // No critical failures found.",
            "`[SYSTEM ARGS]` Core parameters: --bypass-firewall=true --entity-presence=detected // Status: UNSTABLE.",
            "`[MEMORY DUMP]` Active threads: 14/16 // Anomaly signature: Glitchtrap_v4 // Integrity: 64.2%.",
            "`[CONFIG CHECK]` Flag overrides: --lockdown=false --surveillance-feed=encrypted // Warning: Unauthorized process running."
        ]
        
        # Luodaan tyylikäs violetti/purppura embed diagnostiikalle
        glitch_color = discord.Color.from_rgb(176, 38, 255)
        embed = discord.Embed(
            title="⚙️ // SYSTEM DIAGNOSTICS & ARGS",
            description=f"```ansi\n\u001b[35m{random.choice(diagnostic_outputs)}\u001b[0m\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Admin Subroutine")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SystemArgsCog(bot))
