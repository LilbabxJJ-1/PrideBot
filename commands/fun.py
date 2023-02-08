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
        embed = discord.Embed(title="Place your bets!!",
                              description="",
                              color=0xA020F0)
        embed.set_image(url=f"https://api.popcat.xyz/whowouldwin?image2={ctx.author.avatar}&image1={seconduser.avatar}")
        await ctx.respond(embed=embed)
        return

    @commands.slash_command(name="ship")
    async def ship(self, ctx, user1: discord.Option(discord.User, description="First person to ship"),
                   user2: discord.Option(discord.User, description="2nd person to ship")):
        """Ship 2 of your love dovey friends"""
        embed = discord.Embed(title="Aww! We ship it!",
                              description="",
                              color=0xA020F0)
        embed.set_image(url=f"https://api.popcat.xyz/ship?user1={user1.avatar}&user2={user2.avatar}")
        await ctx.respond(embed=embed)
        return

    @commands.slash_command(name="jail")
    async def jail(self, ctx, user: discord.Option(discord.User, description="User or leave blank if yourself") = None):
        """Watch as your pfp spends time in jail"""
        if user is None:
            embed = discord.Embed(title="La gasp! Criminal",
                                  description="",
                                  color=0xA020F0)
            embed.set_image(url=f"https://api.popcat.xyz/jail?image={ctx.author.avatar}")
        else:
            embed = discord.Embed(title="La gasp! Criminal",
                                  description="",
                                  color=0xA020F0)
            embed.set_image(url=f"https://api.popcat.xyz/jail?image={user.avatar}")

        await ctx.respond(embed=embed)
        return
