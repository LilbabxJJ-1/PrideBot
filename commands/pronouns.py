import random
import discord
from discord.ext import commands
from tokens import *


class pronounCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="testpronouns")
    async def testpronouns(self, ctx, name: discord.Option(description="Your name"), Subjective_Pronouns: discord.Option(description="Example: They"), Objective_Pronoun: discord.Option(description="Example: Them"), Possessive_Determiner: discord.Option(description="Example: Their"),
                           Possesive_Pronoun: discord.Option(description="Example: Theirs"), Reflective_Pronoun: discord.Option(description="Example: Themself")):
        """Test out your pronouns! More pronoun slots soon"""
        send = random.choice(sentences).replace("NAME", name).replace("SUBJECT", Subjective_Pronouns).replace("PP", Possesive_Pronoun).replace("OBJECTIVE", Objective_Pronoun).replace("REFLECT", Reflective_Pronoun).replace("PD", Possessive_Determiner)
        await ctx.respond()
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
