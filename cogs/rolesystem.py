import discord
from discord.ext import commands
import voxelbotutils as utils
import asyncpg


class rolesystem(utils.Cog):

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, emote:str, *, rolename:str):

        role = discord.utils.get(ctx.guild.roles, name=rolename)
        if role is None:
            role = await ctx.guild.create_role(name=rolename)

        try:
            my_message = await ctx.send(f"React to this message to get the role **{role.mention}**",
            allowed_mentions=discord.AllowedMentions.none())
            await my_message.add_reaction(emote)
        except:
            await ctx.send("I cannot use that emote. Try another emote")
            return

        async with self.bot.database()as db:
            await db('''INSERT INTO roles (message_id, emoji, role_id) VALUES ($1, $2, $3)on conflict(message_id, emoji)do update set role_id = $3''', 
            my_message.id, emote, role.id)

def setup(bot):
    bot.add_cog(rolesystem(bot))


        