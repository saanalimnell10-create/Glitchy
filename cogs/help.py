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
        # Custom Glitchtrap neon purple-magenta color (0xB026FF)
        glitch_color = discord.Color.from_rgb(176, 38, 255)

        if self.values[0] == "SYSTEM PROTOCOLS":
            embed = discord.Embed(
                title="⚙️ // SYSTEM PROTOCOLS",
                description=(
                    "```ansi\n"
                    "\u001b[35m[ACCESS GRANTED: CORE SUBSYSTEMS]\u001b[0m\n"
                    "```"
                ),
                color=glitch_color
            )
            embed.add_field(name="`::setup`", value="Initializes system & surveillance nodes", inline=False)
            embed.add_field(name="`::welcome`", value="Broadcasts an automated anomaly greeting", inline=False)
            embed.add_field(name="`::goodbye`", value="Broadcasts a grim departure log", inline=False)
            embed.add_field(name="`::args`", value="Checks active system errors and memory flags", inline=False)

        elif self.values[0] == "SURVEILLANCE & SECURITY":
            embed = discord.Embed(
                title="👁️ // SURVEILLANCE LOGS",
                description=(
                    "```ansi\n"
                    "\u001b[35m[ACCESS GRANTED: SECURITY NODES]\u001b[0m\n"
                    "```"
                ),
                color=glitch_color
            )
            embed.add_field(name="`::isolate`", value="Severs the current channel from the network loop", inline=False)
            embed.add_field(name="`::surveillance`", value="Accesses encrypted camera feeds and logs", inline=False)

        elif self.values[0] == "GLITCH TERMINAL":
            embed = discord.Embed(
                title="⚡ // GLITCH TERMINAL",
                description=(
                    "```ansi\n"
                    "\u001b[31m[WARNING: ANOMALOUS MODULES ACTIVE]\u001b[0m\n"
                    "```"
                ),
                color=glitch_color
            )
            embed.add_field(name="`::glitch`", value="Triggers a random network flicker and data packet", inline=False)
            embed.add_field(name="`::crash`", value="Simulates a sudden core system collapse", inline=False)
            embed.add_field(name="`::archive`", value="Retrieves a half-destroyed network log or lore", inline=False)
            embed.add_field(name="`::corrupt <text>`", value="Corrupts string input into glitch text output", inline=False)

        embed.set_footer(text="SYSTEM OVERLOAD // THEY ARE WATCHING THROUGH THE SCREENS.")
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
        """Displays the neon-purple glitch interactive terminal dropdown menu."""
        glitch_color = discord.Color.from_rgb(176, 38, 255)
        
        embed = discord.Embed(
            title="> SYSTEM OVERLOAD // MAIN TERMINAL",
            description=(
                "```ansi\n"
                "\u001b[35m[STATUS: UNSTABLE]\u001b[0m\n"
                "Connection established via node \u001b[33m::\u001b[0m\n"
                "Select a target subsystem from the dropdown below...\n"
                "```"
            ),
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // PREFIX: ::")
        view = GlitchHelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(DropdownHelp(bot))
