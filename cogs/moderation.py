import discord
from discord.ext import commands
import asyncio

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def system_kick(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Ejects a user entity from the network grid."""
        await member.kick(reason=reason)
        
        glitch_color = discord.Color.from_rgb(176, 38, 255)
        embed = discord.Embed(
            title="⚡ // ENTITY EJECTED",
            description=f"```ansi\n\u001b[31m[KICK]\u001b[0m Target **{member.display_name}** was purged from the server.\n> Reason: {reason}\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Moderation Protocol")
        await ctx.send(embed=embed)

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def system_ban(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Permanently bans an anomaly from the main database."""
        await member.ban(reason=reason)
        
        glitch_color = discord.Color.from_rgb(176, 38, 255)
        embed = discord.Embed(
            title="☠️ // PERMANENT BAN",
            description=f"```ansi\n\u001b[31m[BAN]\u001b[0m Entity **{member.display_name}** has been permanently deleted from the database.\n> Reason: {reason}\n```",
            color=glitch_color
        )
        embed.set_footer(text="SYSTEM OVERLOAD // Security Protocol")
        await ctx.send(embed=embed)

    @commands.command(name="clear", aliases=["purge", "clean"])
    @commands.has_permissions(manage_messages=True)
    async def system_clear(self, ctx, amount: int = 5):
        """Purges corrupted data packets (messages) from the active channel."""
        await ctx.channel.purge(limit=amount + 1)
        
        msg = await ctx.send(f"`[SYSTEM CLEANUP]` Purged {amount} corrupted data packets from the buffer.")
        await asyncio.sleep(4)
        try:
            await msg.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
