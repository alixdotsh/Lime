import typing
import re

import discord
from discord.ext import commands
import voxelbotutils as utils

# Original command from https://github.com/Voxel-Fox-Ltd/Apple.Py/blob/master/cogs/emoji_commands.py !!!!PLEASE CREDIT THEM!!!!
class ImageUrl(commands.Converter):

    regex = re.compile(r"(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|gif|png)")
    # Recompile takes in effect here

    async def convert(self, ctx:utils.Context, argument:str):


        v = self.regex.search(argument)
        if v is None:
            raise commands.BadArgument()
        return argument


class EmojiCommands(utils.Cog):

    @utils.command(aliases=['addemoji'])
    @commands.bot_has_permissions(manage_emojis=True)
    @commands.has_guild_permissions(manage_emojis=True)
    @commands.guild_only()
    async def addemoji(self, ctx:utils.Context, emoji:typing.Union[discord.PartialEmoji, int, ImageUrl], name:str=None, animated:bool=False):
        # This will be copying the emoji given and uploading it to specified server

        # If an emote ID is given
        if isinstance(emoji, int):
            if name is None:
                raise utils.errors.MissingRequiredArgumentString("name")
            emoji = discord.PartialEmoji(name=name, animated=animated, id=emoji)

        # If it was an image or emote URL
        if isinstance(emoji, discord.PartialEmoji):
            url = str(emoji.url)
            name = name or emoji.name
        else:
            url = emoji

        # Grabber takes effect here
        async with self.bot.session.get(url) as r:
            data = await r.read()

        # Upload to Discord/Discord Server
        try:
            e = await ctx.guild.create_custom_emoji(name=name, image=data)
        except discord.HTTPException as e:
            return await ctx.send(f"I couldn't create that emoji - {e}")
        except discord.InvalidArgument:
            return await ctx.send("Unsupported image type - make sure you're providing the correct argument for the image's animation state.")
        await ctx.send(f"Emoji added - {e!s}")


def setup(bot:utils.Bot):
    x = EmojiCommands(bot)
    bot.add_cog(x)