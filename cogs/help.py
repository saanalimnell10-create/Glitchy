import discord
from discord.ext import commands

class HelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="System & Setup",
                description="Core system commands and administrative tools",
                emoji="⚙️"
            ),
            discord.SelectOption(
                label="Surveillance & Security",
                description="Channel isolation and network security logs",
                emoji="👁️"
            ),
            discord.SelectOption(
                label="Glitch Terminal",
                description="Network flickers, crash simulations, and data corruption",
                emoji="⚡"
            )
        ]
        super().__init__(placeholder="Select a system category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "System & Setup":
            embed = discord.Embed(
                title="⚙️ [SYSTEM / SETUP DIRECTORY]",
                description="Administrative subroutines and system protocols:",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::setup`", value="Initializes system & surveillance nodes *(Owner)*", inline=False)
            embed.add_field(name="`::welcome`", value="Automated anomaly greeting protocol", inline=False)
            embed.add_field(name="`::goodbye`", value="Automated departure log protocol", inline=False)
            embed.add_field(name="`::args`", value="Checks active system errors *(Owner)*", inline=False)

        elif self.values[0] == "Surveillance & Security":
            embed = discord.Embed(
                title="👁️ [SURVEILLANCE & SECURITY DIRECTORY]",
                description="Security nodes and monitoring subroutines:",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::isolate`", value="Severs a channel from the network *(Mod)*", inline=False)
            embed.add_field(name="`::surveillance`", value="Accesses encrypted camera logs *(Mod)*", inline=False)

        elif self.values[0] == "Glitch Terminal":
            embed = discord.Embed(
                title="⚡ [GLITCH TERMINAL DIRECTORY]",
                description="Anomalous network modules and corruption tools:",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::glitch`", value="Triggers a random network flicker & data packet", inline=False)
            embed.add_field(name="`::crash`", value="Simulates a core system collapse *(Mod)*", inline=False)
            embed.add_field(name="`::archive`", value="Retrieves a half-destroyed network log", inline=False)
            embed.add_field(name="`::corrupt <text>`", value="Corrupts string input into glitch text", inline=False)

        embed.set_footer(text="SYSTEM OVERLOAD v2.0 // Interactive Terminal")
        await interaction.response.edit_message(embed=embed, view=self.view)

class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(HelpDropdown())

class DropdownHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(name="help", aliases=["terminal", "commands", "menu"])
    async def help_command(self, ctx):
        """Displays the interactive terminal dropdown menu."""
        embed = discord.Embed(
            title="> SYSTEM OVERLOAD // INTERACTIVE TERMINAL",
            description="Select a module from the dropdown menu below to access subroutines:",
            color=discord.Color.dark_embed()
        )
        embed.set_footer(text="SYSTEM OVERLOAD v2.0 // They are watching.")
        view = HelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(DropdownHelp(bot))
