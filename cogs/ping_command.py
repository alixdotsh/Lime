import voxelbotutils as utils


class PingCommand(utils.Cog):

    @utils.command()
    async def ping(self, ctx:utils.Context):
        """
        A sexy lil ping command for the bot.
        """

        await ctx.send("I'm here!")


def setup(bot:utils.Bot):
    x = PingCommand(bot)
    bot.add_cog(x)
