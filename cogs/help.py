import discord
from discord.ext import commands

class HelpDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Terminal Commands",
                description="View all available commands and their functions.",
                emoji="⚡",
                value="commands"
            ),
            discord.SelectOption(
                label="About Bot",
                description="Quick information about Glitchy.",
                emoji="🟣",
                value="about"
            )
        ]
        super().__init__(placeholder="✨ Select a category to explore commands...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        aesthetic_purple = discord.Color.from_rgb(147, 112, 219)

        if self.values[0] == "commands":
            embed = discord.Embed(
                title="⚡ Glitchy Command Center",
                description="Here are the active commands you can use:",
                color=aesthetic_purple
            )
            embed.add_field(
                name="`!help` / `?help`",
                value="Opens this interactive help menu.",
                inline=False
            )
            embed.add_field(
                name="`!status` / `!sys`",
                value="Displays the system status.",
                inline=False
            )
            embed.set_thumbnail(url=interaction.client.user.avatar.url if interaction.client.user.avatar else None)
            
        elif self.values[0] == "about":
            embed = discord.Embed(
                title="🟣 About Glitchy",
                description="A purplish, terminal-themed aesthetic bot.",
                color=aesthetic_purple
            )
            embed.add_field(
                name="Status",
                value="Online and ready.",
                inline=False
            )
            embed.set_thumbnail(url=interaction.client.user.avatar.url if interaction.client.user.avatar else None)

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
        embed = discord.Embed(
            title="🌸 Glitchy • Help Center",
            description=f"Hello {ctx.author.mention}! Welcome to the interactive help command center.\n\n✨ Please select a category from the dropdown menu below to view its available commands.",
            color=discord.Color.from_rgb(147, 112, 219)
        )
        
        if self.bot.user.avatar:
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            
        embed.set_footer(text="Glitchy • System Overload")
        
        view = HelpView()
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
