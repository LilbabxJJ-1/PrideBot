import random
import discord
from discord.ext import commands
from tokens import *


class funCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="whowouldwin")
    async def whowin(self, ctx, seconduser: discord.Option(discord.User, description="The person you're up against")):
        """Who would win template with friends!"""
        embed=discord.Embed(title="Place your bets!!",
                            description="",
                            color=0xA020F0)
        embed.set_image(url=f"https://api.popcat.xyz/whowouldwin?image2={ctx.author.avatar}&image1={seconduser.avatar}")
        return
