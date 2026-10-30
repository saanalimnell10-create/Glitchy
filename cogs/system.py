import discord
from discord.ext import commands
import time

class SystemCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command(name="status", aliases=["sys", "node"])
    async def system_status(self, ctx):
        """Displays Glitchy's system status and node metrics."""
        
        # Lasketaan botin päälläoloaika (uptime)
        uptime_seconds = int(time.time() - self.start_time)
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        seconds = uptime_seconds % 60
        
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="> [SYSTEM_OVERLOAD // NODE_STATUS]",
            description="Diagnostic scan complete. Core systems operating within parameters.",
            color=discord.Color.dark_green()
        )

        embed.add_field(
            name="🟢 Core Node",
            value=f"`Online` (Uptime: {hours}h {minutes}m {seconds}s)",
            inline=False
        )

        embed.add_field(
            name="⚡ Network Latency",
            value=f"`{latency}ms`",
            inline=True
        )

        embed.add_field(
            name="🔒 Security Protocol",
            value="`Cyber-Noir v1.0`",
            inline=True
        )

        embed.set_footer(text="System Overload • Glitchy core active.")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SystemCog(bot))
