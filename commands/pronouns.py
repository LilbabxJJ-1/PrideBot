import random
import discord
from discord.ext import commands
from tokens import *


class pronounCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="testpronouns")
    async def testpronouns(self, ctx, name: discord.Option(description="Your name"), subjective_pronoun: discord.Option(description="Example: They"), objective_pronoun: discord.Option(description="Example: Them"), possessive_determiner: discord.Option(description="Example: Their"),
                           possesive_pronoun: discord.Option(description="Example: Theirs"), reflective_pronoun: discord.Option(description="Example: Themself")):
        """Test out your pronouns! More pronoun slots soon"""
        send = random.choice(sentences).replace("NAME", name).replace("SUBJECT", subjective_pronoun).replace("PP", possesive_pronoun).replace("OBJECTIVE", objective_pronoun).replace("REFLECT", reflective_pronoun).replace("PD", possessive_determiner)
        await ctx.respond(send)
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
        await ctx.respond("Successfully submitted suggestion")
        return
