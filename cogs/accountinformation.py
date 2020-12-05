from datetime import datetime as dt

import discord
from discord.ext import commands
import voxelbotutils as utils
import humanize


class AccountInformation(utils.Cog):

    # running the command
    @commands.command()
    async def accountinfo(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author

        if user.nick is not None:
            name = f"{user.name} ({user.nick})"
        else:
            name = user.name

        # Make and send an embed to the channel listing account information
        embed = discord.Embed(
            colour=0xBAFFC9,
            title=f"Account Information For {name}"
        )
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Account Created", value=user.created_at.strftime("%m/%d/%Y %H:%M:%S"))
        embed.add_field(name="Account Age", value=humanize.precisedelta(dt.now() - user.created_at))
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%m/%d/%Y %H:%M:%S"))
        embed.add_field(name="Join Server Age", value=humanize.precisedelta(dt.now() - user.joined_at))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AccountInformation(bot))
