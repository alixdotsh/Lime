import asyncio

import discord
import voxelbotutils as utils
from discord.ext import commands


class Mute(utils.Cog):

    @commands.command()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member, time:int, *, reason: str):
        muterole = discord.utils.get(ctx.guild.roles, name="Muted")
        if muterole is None:
            muterole = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muterole, send_messages=False)
        await user.add_roles(muterole, reason=reason)
        await ctx.send(f"{user.mention} was muted by {ctx.author.mention}")
        ctx.bot.dispatch("modlog", user, ctx.author, "mute", reason)
        await asyncio.sleep(time * 60)
        await user.remove_roles(muterole)


def setup(bot):
    bot.add_cog(Mute(bot))
