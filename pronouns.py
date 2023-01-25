import random
import discord
from discord.ext import commands
from tokens import *


class pronounCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="testpronouns")
    async def test_pronouns(self, ctx, name: discord.Option(description="Your name"), pronoun1: discord.Option(description="If using They/Them, They would go here"), pronoun2: discord.Option(description="If using They/Them, Them would go here")):
        """Test out your pronouns! More pronoun slots soon"""
        sentences = [f"{name} ate food because {pronoun1} was hungry.",
                     f"Have you seen {name}? {pronoun1} is supposed to go to the mall with me, let me know when you see {pronoun2}",
                     f"{name} is a great friend! I enjoy being around {pronoun2}"]

        await ctx.respond(random.choice(sentences))
        await ctx.send("These may come out as incorrect grammatically since this is still very new")
        return

    @commands.slash_command(name="suggestpronouns")
    async def suggestPronouns(self, ctx, sentence: discord.Option(description="A sentence that can be used to test pronouns")):
        """Suggest sentences we can use for the /testpronouns command"""
        embed = discord.Embed(title="Pronoun Sentence",
                              description=sentence,
                              color=0xA020F0)
        channel = await self.bot.fetch_channel(991806371815243836)
        await channel.send(embed=embed)
        await ctx.respond("Successfully submitted suggestion!")
        return
