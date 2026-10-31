import discord
from discord.ext import commands

class IsolateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="isolate", aliases=["room_isolate", "lockdown"])
    @commands.has_permissions(manage_channels=True)
    async def room_isolate(self, ctx):
        """Severs the current channel from the main network loop (locks the channel)."""
        channel = ctx.channel
        guild = ctx.guild
        
        # Estetään @everyone-roolin viestien lähetys tällä kanavalla (eristys)
        overwrite = channel.overwrites_for(guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(guild.default_role, overwrite=overwrite)

        glitch_color = discord.Color.from_rgb(176, 38, 255)
        embed = discord.Embed(
            title="🔒 // CHANNEL ISOLATED",
            description=f"```ansi\n\u001b[31m[LOCKDOWN]\u001b[0m Channel **{channel.name}** has been severed from the main network loop.\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Security Protocol")
        
        await ctx.send(embed=embed)

    @commands.command(name="unisolate", aliases=["restore"])
    @commands.has_permissions(manage_channels=True)
    async def room_unisolate(self, ctx):
        """Restores network connection to the channel."""
        channel = ctx.channel
        guild = ctx.guild
        
        # Palautetaan @everyone-roolin oikeudet ennalleen
        overwrite = channel.overwrites_for(guild.default_role)
        overwrite.send_messages = None
        await channel.set_permissions(guild.default_role, overwrite=overwrite)

        glitch_color = discord.Color.from_rgb(176, 38, 255)
        embed = discord.Embed(
            title="🔓 // NETWORK RESTORED",
            description=f"```ansi\n\u001b[32m[SYSTEM]\u001b[0m Channel **{channel.name}** reconnected to the grid.\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Security Protocol")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(IsolateCog(bot))
