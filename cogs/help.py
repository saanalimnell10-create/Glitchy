import discord
from discord.ext import commands

class GlitchHelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="SYSTEM PROTOCOLS",
                description="Core network commands and automated nodes",
                emoji="⚙️"
            ),
            discord.SelectOption(
                label="SURVEILLANCE & SECURITY",
                description="Channel isolation and camera feeds",
                emoji="👁️"
            ),
            discord.SelectOption(
                label="GLITCH TERMINAL",
                description="Anomalies, crashes, and text corruption",
                emoji="⚡"
            )
        ]
        super().__init__(placeholder="[SELECT TERMINAL SUBSYSTEM...]", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "SYSTEM PROTOCOLS":
            embed = discord.Embed(
                title="⚙️ // 5̷Y̷5̷T̷E̷M̷ ̷P̷R̷O̷T̷O̷C̷O̷L̷S̷",
                description="```fix\n[ACCESS GRANTED: CORE SUBSYSTEMS]\n```",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::setup`", value="Initializes system & surveillance nodes", inline=False)
            embed.add_field(name="`::welcome`", value="Broadcasts an automated anomaly greeting", inline=False)
            embed.add_field(name="`::goodbye`", value="Broadcasts a grim departure log", inline=False)
            embed.add_field(name="`::args`", value="Checks active system errors and memory flags", inline=False)

        elif self.values[0] == "SURVEILLANCE & SECURITY":
            embed = discord.Embed(
                title="👁️ // 5̷U̷R̷V̷E̷I̷L̷L̷A̷N̷C̷E̷ ̷L̷O̷G̷S̷",
                description="```fix\n[ACCESS GRANTED: SECURITY NODES]\n```",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::isolate`", value="Severs the current channel from the network loop", inline=False)
            embed.add_field(name="`::surveillance`", value="Accesses encrypted camera feeds and logs", inline=False)

        elif self.values[0] == "GLITCH TERMINAL":
            embed = discord.Embed(
                title="⚡ // G̷L̷I̷T̷C̷H̷ ̷T̷E̷R̷M̷I̷N̷A̷L̷",
                description="```fix\n[WARNING: ANOMALOUS MODULES ACTIVE]\n```",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="`::glitch`", value="Triggers a random network flicker and data packet", inline=False)
            embed.add_field(name="`::crash`", value="Simulates a sudden core system collapse", inline=False)
            embed.add_field(name="`::archive`", value="Retrieves a half-destroyed network log or lore", inline=False)
            embed.add_field(name="`::corrupt <text>`", value="Corrupts string input into glitch text output", inline=False)

        embed.set_footer(text="⚠️ SYSTEM OVERLOAD // THEY ARE WATCHING THROUGH THE SCREENS.")
        await interaction.response.edit_message(embed=embed, view=self.view)

class GlitchHelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(GlitchHelpDropdown())

class DropdownHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

    @commands.command(name="help", aliases=["terminal", "commands", "menu"])
    async def help_command(self, ctx):
        """Displays the glitchy interactive terminal dropdown menu."""
        embed = discord.Embed(
            title="> █▒▓ SYSTEM OVERLOAD // MAIN TERMINAL ▓▒█",
            description=(
                "```ini\n"
                "[STATUS: UNSTABLE]\n"
                "Connection established via node ::\n"
                "Select a target subsystem from the dropdown below...\n"
                "```"
            ),
            color=discord.Color.dark_embed()
        )
        embed.set_footer(text="⚠️ SYSTEM OVERLOAD // PREFIX: ::")
        view = GlitchHelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(DropdownHelp(bot))
