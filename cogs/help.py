import discord
from discord.ext import commands

class HelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="All Terminal Commands",
                description="View all available commands for Glitchy.",
                emoji="⚡",
                value="all_commands"
            ),
            discord.SelectOption(
                label="System Status & Node",
                description="Check uptime, latency, and connection metrics.",
                emoji="🟢",
                value="system_status"
            ),
            discord.SelectOption(
                label="Security Protocols",
                description="View node encryption and cyberpunk security status.",
                emoji="🔒",
                value="security"
            )
        ]
        super().__init__(placeholder="> Select a system database...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Käytetään syvää purppuraa / violettia sävyä (Discord color: purple tai custom hex)
        purple_color = discord.Color.from_rgb(138, 43, 226) # BlueViolet

        if self.values[0] == "all_commands":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // ALL_COMMANDS]",
                description="Accessing core mainframe... Here is the complete command registry:",
                color=purple_color
            )
            embed.add_field(
                name="⚡ `!help` / `?help`",
                value="Opens this interactive terminal menu.",
                inline=False
            )
            embed.add_field(
                name="🟢 `!status` / `!sys`",
                value="Displays node uptime, latency, and server metrics.",
                inline=False
            )
            
        elif self.values[0] == "system_status":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // NODE_METRICS]",
                description="Diagnostic data retrieved from current hosting node:",
                color=purple_color
            )
            embed.add_field(
                name="Hosting Route",
                value="Routing securely through Render cloud infrastructure.",
                inline=False
            )
            embed.add_field(
                name="Uptime Monitor",
                value="Active 24/7 via automated heartbeat signals.",
                inline=False
            )
            
        elif self.values[0] == "security":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // SECURITY_GRID]",
                description="Active cyber-noir security barriers:",
                color=purple_color
            )
            embed.add_field(
                name="Encryption Layer",
                value="Terminal Stream v1.0 — **Secure**",
                inline=False
            )

        await interaction.response.edit_message(embed=embed)

class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(HelpDropdown())

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", aliases=["commands", "glitchy"])
    async def help_menu(self, ctx):
        """Displays Glitchy's purplish interactive terminal help menu."""
        
        # Päävalikon embed purppuralla teemalla
        embed = discord.Embed(
            title="> [SYSTEM_OVERLOAD // GLITCHY_CORE]",
            description="Connection established. Select a database from the dropdown menu below to view system parameters and commands.",
            color=discord.Color.from_rgb(138, 43, 226)
        )
        embed.set_footer(text="System Overload Node v1.0 • Glitchy is watching.")
        
        view = HelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
