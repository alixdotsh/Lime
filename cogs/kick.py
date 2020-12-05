import discord
from discord.ext import commands
import voxelbotutils as utils

class Kick(utils.Cog):

    @commands.command()
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:discord.Member, *, reason:str):
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} was kicked by {ctx.author.mention}")
        ctx.bot.dispatch("modlog", user, ctx.author, "kick", reason)


def setup(bot):
    bot.add_cog(Kick(bot))
