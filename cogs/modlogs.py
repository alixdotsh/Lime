import discord
from discord.ext import commands
import voxelbotutils as utils
import asyncpg


class Modlogs(utils.Cog):

    @commands.Cog.listener()
    async def on_modlog(self, user, moderator, command, reason):
        """Send a message to the modlogs when a moderator does something"""

        # Connect to the database
        conn = await asyncpg.connect(user='lime', password='021006', database='lime', host='127.0.0.1')
        values = await conn.fetch('''SELECT * FROM modlogs WHERE guild_id = $1''', moderator.guild.id)
        await conn.close()

        # See if there were any results, ie if the guild has a modlogs channel
        if len(values) == 0:
            modlogs = None
        else:
            modlogs = moderator.guild.get_channel(values[0]["modlog_channel"])

        # Create a new modlogs channel if one doesn't exist
        if modlogs is None:
            modlogs = await moderator.guild.create_text_channel(name="mod-logs")
            await modlogs.set_permissions(modlogs.guild.default_role, send_messages=False)
            await modlogs.set_permissions(modlogs.guild.me, send_messages=True)

            # Save the ID of the newly created modlogs channel
            conn = await asyncpg.connect(user='lime', password='021006', database='lime', host='127.0.0.1')
            await conn.fetch('''INSERT INTO modlogs (guild_id, modlog_channel) VALUES ($1, $2)''', moderator.guild.id, modlogs.id)
            await conn.close()

        # Make and send an embed to the channel
        embed = discord.Embed(
            colour=0x8A2BE2,
            title="New Audit Log",
            description=f"{moderator.mention} to {user.mention}\n Command: {command}\n Reason: {reason}"
        )
        embed.set_author(name=moderator.name, icon_url=moderator.avatar_url)
        await modlogs.send(embed=embed)


def setup(bot):
    bot.add_cog(Modlogs())
