import discord
from discord.ext import commands

class GlitchHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Poistetaan oletus-help, jotta saadaan tehtyä oma tyylitetty versio
        bot.remove_command('help')

    @commands.command(name="help", aliases=["terminal", "commands", "menu"])
    async def help_menu(self, ctx):
        """Displays the main terminal command suite and system directory."""
        
        embed = discord.Embed(
            title="> SYSTEM OVERLOAD // COMMAND DIRECTORY",
            description="Access level verified. Available subroutines and system protocols listed below:",
            color=discord.Color.dark_embed()
        )
        
        # System Category
        embed.add_field(
            name="⚙️ [SYSTEM / SETUP]",
            value=(
                "`#setup` - Initializes system & surveillance nodes *(Owner)*\n"
                "`#welcome` - Automated anomaly greeting protocol\n"
                "`#goodbye` - Automated departure log protocol\n"
                "`#args` - Checks active system errors *(Owner)*"
            ),
            inline=False
        )
        
        # Anomaly & Surveillance Category
        embed.add_field(
            name="👁️ [SURVEILLANCE & SECURITY]",
            value=(
                "`#isolate` (or `#room isolate`) - Severs a channel from the network *(Mod)*\n"
                "`#surveillance` (or `#logs`) - Accesses encrypted camera logs *(Mod)*"
            ),
            inline=False
        )
        
        # Glitch Terminal Category
        embed.add_field(
            name="⚡ [GLITCH TERMINAL]",
            value=(
                "`#glitch` - Triggers a random network flicker & data packet\n"
                "`#crash` - Simulates a core system collapse *(Mod)*\n"
                "`#archive` (or `#lore`) - Retrieves a half-destroyed network log\n"
                "`#corrupt <text>` - Corrupts string input into glitch text"
            ),
            inline=False
        )
        
        embed.set_footer(text="SYSTEM OVERLOAD v2.0 // They are watching through the screens.")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GlitchHelp(bot))
