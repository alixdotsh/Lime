import discord
from discord.ext import commands
import voxelbotutils as utils
import asyncpg


class SelectChannel(utils.Cog):

    # running the command
    @commands.command()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def setchannel_modlogs(self, ctx, channel: discord.TextChannel):
        """
        Set the channel for where modlogs go
        """

        # Connecting to the database uwu
        async with self.bot.database()as db:
        await db('''INSERT INTO modlogs (guild_id, modlog_channel) VALUES ($1, $2)on conflict(guild_id)do update set modlog_channel = $2''', channel.guild.id,
                         channel.id)

        await ctx.send(f" I have connected the channel {channel.mention} for sending modlogs")


def setup(bot):
    bot.add_cog(SelectChannel(bot))
