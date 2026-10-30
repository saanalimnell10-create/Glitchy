import discord
from discord.ext import commands

class HelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Core Commands",
                description="View basic terminal commands like ping and help.",
                emoji="⚡",
                value="core"
            ),
            discord.SelectOption(
                label="System Status",
                description="View server node metrics and system uptime.",
                emoji="🟢",
                value="system"
            ),
            discord.SelectOption(
                label="Security Protocols",
                description="Check Glitchy's cyber-noir security status.",
                emoji="🔒",
                value="security"
            )
        ]
        super().__init__(placeholder="> Select a system category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "core":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // CORE_COMMANDS]",
                description="Here are the basic operational commands:",
                color=discord.Color.dark_embed()
            )
            embed.add_field(name="!help", value="Displays this interactive terminal menu.", inline=False)
            embed.add_field(name="!status", value="Displays node metrics and uptime.", inline=False)
            
        elif self.values[0] == "system":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // NODE_SYSTEM]",
                description="System diagnostics and uptime information module.",
                color=discord.Color.dark_green()
            )
            embed.add_field(name="Status Metric", value="All nodes are currently routing traffic securely through Render.", inline=False)
            
        elif self.values[0] == "security":
            embed = discord.Embed(
                title="> [SYSTEM_OVERLOAD // SECURITY]",
                description="Cyber-noir node security protocols:",
                color=discord.Color.dark_red()
            )
            embed.add_field(name="Encryption", value="Active (256-bit simulated terminal stream)", inline=False)

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
        """Displays Glitchy's interactive terminal help menu."""
        
        embed = discord.Embed(
            title="> [SYSTEM_OVERLOAD // GLITCHY_CORE]",
            description="Accessing local node database... Use the dropdown menu below to navigate categories.",
            color=discord.Color.dark_embed()
        )
        embed.set_footer(text="System Overload Node v1.0 • Glitchy is watching.")
        
        view = HelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
