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
        
    @utils.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        async with self.bot.database()as db:
            rows = await db("select *from roles where message_id = $1 and emoji = $2", payload.message_id, str(payload.emoji))
        if len(rows) == 0:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        role = guild.get_role(rows[0]["role_id"])
        member = guild.get_member(payload.user_id)
        await memeber.add_roles(role)
        

def setup(bot):
    bot.add_cog(rolesystem(bot))


        