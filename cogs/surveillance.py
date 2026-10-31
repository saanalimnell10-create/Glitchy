import discord
from discord.ext import commands
import random

class SurveillanceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="surveillance", aliases=["surveil", "logs"])
    @commands.has_permissions(manage_roles=True)
    async def surveillance_view(self, ctx):
        """Accesses encrypted security camera feeds and logs."""
        surveillance_feeds = [
            "`[SECURE FEED #01]` Accessing camera room 3... Static on screen. Movement detected near the server racks.",
            "`[CAMERA 04]` Feed looping. The hallway is empty, but footsteps are audible on the audio track.",
            "`[LOG ARCHIVE]` Security patrol #2 failed to check in at 02:00 AM. Last known location: Sector C.",
            "`[ENCRYPTED FEED]` The monitoring screens are flickering. A yellow silhouette briefly appeared on camera 2.",
            "`[SURVEILLANCE WARNING]` Unauthorized remote connection detected on feed #8. Who is watching?"
        ]

        # Glitchtrap neon purple-magenta color
        glitch_color = discord.Color.from_rgb(176, 38, 255)
        
        embed = discord.Embed(
            title="👁️ // SURVEILLANCE FEED ACTIVE",
            description=f"```ansi\n\u001b[35m{random.choice(surveillance_feeds)}\u001b[0m\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Security Subroutine")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SurveillanceCog(bot))
