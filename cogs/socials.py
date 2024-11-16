from tools.pinterest import Pinterest  # type: ignore
from discord.ext import commands
import discord
import io
from discord.ext.commands import Context
from aiohttp import ClientSession as Session
from tools.pinpostmodels import Model  # type: ignore
from tuuid import tuuid


class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pinterest = Pinterest()



async def setup(bot):
    await bot.add_cog(Socials(bot))
