import discord
from discord.ext import commands
import voxelbotutils as utils


class Ban(utils.Cog):

    @commands.command()
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason: str):
        await user.ban(reason=reason)
        await ctx.send(f"{user.mention} was banned by {ctx.author.mention}")
        ctx.bot.dispatch("modlog", user, ctx.author, "ban", reason)


def setup(bot):
    bot.add_cog(Ban())
