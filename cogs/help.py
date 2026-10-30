import discord
from discord.ext import commands

class HelpSelect(discord.ui.Select):
    def __init__(self, prefix):
        self.prefix = prefix
        options = [
            discord.SelectOption(label="Moderation", description="Standard moderation commands (warn, kick, ban)", value="Moderation"),
            discord.SelectOption(label="Safety", description="Advanced moderation and isolation tools", value="Safety"),
            discord.SelectOption(label="Member Protection", description="Watchlist and user protection suite", value="Member Protection"),
            discord.SelectOption(label="Threat Security", description="Dynamic pressure tracking and modes", value="Threat Security"),
            discord.SelectOption(label="Security & Anti-Nuke", description="Anti-nuke, anti-raid, and whitelist settings", value="Security & Anti-Nuke"),
            discord.SelectOption(label="Channel Management", description="Lock, unlock, purge, and slowmode commands", value="Channel Management"),
            discord.SelectOption(label="Server Tools", description="Emoji steal and channel cloning tools", value="Server Tools"),
            discord.SelectOption(label="Tickets", description="Support ticket panel and management commands", value="Tickets"),
            discord.SelectOption(label="Staff Applications", description="Staff apply panel and application controls", value="Staff Applications"),
            discord.SelectOption(label="Welcome & Goodbye", description="Configure custom welcome and goodbye messages", value="Welcome & Goodbye"),
            discord.SelectOption(label="Giveaways", description="Advanced giveaways with tickets & auto-rerolls", value="Giveaways"),
            discord.SelectOption(label="Audit Logs", description="Configure server event logging", value="Audit Logs"),
        ]
        super().__init__(placeholder="> Select a system category...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        p = self.prefix
        embed = discord.Embed(color=discord.Color.from_rgb(138, 43, 226))
        embed.set_footer(text="[SYSTEM_OVERLOAD] • Glitchy Node")

        if selected == "Moderation":
            embed.title = "> [MODERATION_TOOLS]"
            embed.description = "Essential server moderation commands."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}warn [@user] [reason]` - Issues a warning to a member.\n"
                    f"`{p}kick [@user] [reason]` - Kicks a member from the server.\n"
                    f"`{p}ban [@user] [reason]` - Bans a member from the server."
                ),
                inline=False
            )

        elif selected == "Safety":
            embed.title = "> [SAFETY_PROTOCOLS]"
            embed.description = "Advanced user isolation and restriction tools."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}isolate [@user]` - Isolates a user from text channels.\n"
                    f"`{p}endbeef [@user]` - Ends the isolation for a user.\n"
                    f"`{p}forcename [@user] [name]` - Enforces a specific nickname on a user."
                ),
                inline=False
            )

        elif selected == "Member Protection":
            embed.title = "> [MEMBER_PROTECTION]"
            embed.description = "Track, mark, and protect server members."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}setupboycott setup [#channel]` - Set alert channel for flags.\n"
                    f"`{p}setupboycott mark [@user] [reason]` - Mark a user on the watchlist.\n"
                    f"`{p}setupboycott unmark [@user]` - Remove a user from the watchlist.\n"
                    f"`{p}setupboycott list` - List all currently marked users."
                ),
                inline=False
            )

        elif selected == "Threat Security":
            embed.title = "> [THREAT_SECURITY]"
            embed.description = "Automated pressure tracking and dynamic threat mode controls."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}threatlevel` - Views current threat score and security status.\n"
                    f"`{p}setthreatmode [mode]` - Overrides security mode (auto/normal/elevated/lockdown).\n"
                    f"`{p}togglethreat [on/off]` - Toggles dynamic threat monitoring."
                ),
                inline=False
            )

        elif selected == "Security & Anti-Nuke":
            embed.title = "> [ANTI_NUKE_GRID]"
            embed.description = "General protection, anti-nuke, anti-raid, and whitelist controls."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}antinuke [on/off]` - Toggle Anti-Nuke protection.\n"
                    f"`{p}antiraid [on/off]` - Toggle Anti-Raid protection.\n"
                    f"`{p}whitelist add [@user]` - Add a user to anti-nuke whitelist.\n"
                    f"`{p}whitelist remove [@user]` - Remove a user from whitelist.\n"
                    f"`{p}whitelisted` - Show whitelisted staff members."
                ),
                inline=False
            )

        elif selected == "Channel Management":
            embed.title = "> [CHANNEL_MANAGEMENT]"
            embed.description = "Manage channel permissions, cleanup, and slowmode."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}lock [reason]` - Locks the current channel.\n"
                    f"`{p}unlock` - Unlocks the current channel.\n"
                    f"`{p}purge [amount]` - Delete a specified number of messages.\n"
                    f"`{p}slowmode [time]` - Set a custom slowmode delay."
                ),
                inline=False
            )

        elif selected == "Server Tools":
            embed.title = "> [SERVER_TOOLS]"
            embed.description = "Utility tools for emojis and channels."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}steal [emoji/url]` - Steals an emoji to the server.\n"
                    f"`{p}clone [#channel]` - Clones an existing channel."
                ),
                inline=False
            )

        elif selected == "Tickets":
            embed.title = "> [SUPPORT_TICKETS]"
            embed.description = "Open and manage support tickets."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}ticketpanel` - Sends the ticket creation panel (Admin).\n"
                    f"`{p}close` - Closes the active ticket channel.\n"
                    f"`{p}add [@user]` - Adds a user to the ticket.\n"
                    f"`{p}remove [@user]` - Removes a user from the ticket."
                ),
                inline=False
            )

        elif selected == "Staff Applications":
            embed.title = "> [STAFF_APPLICATIONS]"
            embed.description = "Apply for staff and manage applications."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}staffapplypanel` - Sends the staff application panel (Admin).\n"
                    f"`{p}applyclose` - Closes the application and generates a transcript."
                ),
                inline=False
            )

        elif selected == "Welcome & Goodbye":
            embed.title = "> [WELCOME_GOODBYE]"
            embed.description = "Configure custom welcome and goodbye messages."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}setwelcomechannel [#channel]` - Sets the welcome channel.\n"
                    f"`{p}setwelcometext <text>` - Sets custom welcome text (`{{user}}`, `{{server}}`).\n"
                    f"`{p}setgoodbyechannel [#channel]` - Sets the goodbye channel.\n"
                    f"`{p}setgoodbyetext <text>` - Sets custom goodbye text."
                ),
                inline=False
            )

        elif selected == "Giveaways":
            embed.title = "> [GIVEAWAY_CENTER]"
            embed.description = "Advanced giveaways with tickets and auto-rerolls."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}giveaway create` - Create an advanced giveaway\n"
                    f"`{p}giveaway end` - End an active giveaway early\n"
                    f"`{p}giveaway delete` - Delete a giveaway message\n"
                    f"`{p}giveaway participants` - View all participants"
                ),
                inline=False
            )

        elif selected == "Audit Logs":
            embed.title = "> [AUDIT_LOGS]"
            embed.description = "Server logging configuration."
            embed.add_field(
                name="Commands",
                value=(
                    f"`{p}setlogs [#channel]` - Sets the audit logging channel.\n"
                    f"`{p}togglelogs` - Toggles server event logging on/off."
                ),
                inline=False
            )

        await interaction.response.edit_message(embed=embed)

class HelpView(discord.ui.View):
    def __init__(self, prefix):
        super().__init__(timeout=300)
        self.add_item(HelpSelect(prefix))

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if self.bot.help_command:
            self.bot.help_command = None

    @commands.command(name="help")
    async def help_command(self, ctx):
        """Displays Glitchy's interactive terminal help menu."""
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        except discord.HTTPException:
            pass
            
        embed = discord.Embed(
            title="> [GLITCHY // TERMINAL_HELP]",
            description=f"Accessing core database. Select a category from the dropdown menu below.\n\nCurrent Prefix: `{ctx.prefix}`",
            color=discord.Color.from_rgb(138, 43, 226)
        )
        embed.set_footer(text="[SYSTEM_OVERLOAD] • Glitchy Node")
        await ctx.send(embed=embed, view=HelpView(ctx.prefix))

async def setup(bot):
    bot.remove_command("help")
    await bot.add_cog(Help(bot))
