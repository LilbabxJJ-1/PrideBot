from discord.ext import commands
import discord
from difflib import get_close_matches as closest
from tokens import *
import random


class DictionaryCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="define")
    async def define(self, ctx, word: discord.Option(description="lGBTQ+ word to look up")):
        """Get a definition for our LGBTQ terms"""
        chances = random.choice(list(range(1, 100)))
        if chances <= 15:
            embed = discord.Embed(title="Like the bot?",
                                  description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college!"
                                              "\n --> https://gofund.me/557611f3\nIf you can't donate, that's okay! You can still show your support by upvoting on Top.gg"
                                              "\n -->..https://top.gg/bot/1066641327116255333#reviews",
                                  colour=0xA020F0)
            await ctx.send(embed=embed)
        term = mycol.find_one({"Term": str(word).title()})
        if term is not None:
            embed = discord.Embed(title=f"Definition for {str(word).title()}",
                                  description=term["Definition"],
                                  colour=0xA020F0)
            await ctx.respond(embed=embed)
            return
        else:
            wordlist = mycol.find_one({"ID": "Total"})
            try:
                suggest = closest(str(word).title(), wordlist["All"])[0]
                await ctx.respond(f"I don't know that word! Please try again and make sure it's lgbtq related | Did you mean {suggest}?", ephemeral=True)
                return
            except Exception:
                await ctx.respond(f"I don't know that word! Please try again and make sure it's lgbtq related | No suggest words..", ephemeral=True)
                return

    @commands.slash_command(name="adddefinition")
    @commands.is_owner()
    async def add_definition(self, ctx, word, definition):
        """Way for bot owner to add terms to dictionary"""
        if word == "" or definition == "":
            await ctx.respond("You need to use all arguments dummy", ephemeral=True)
            return
        search = mycol.find_one({"Term": str(word).title()})
        if search is not None:
            await ctx.respond("This word is already added", ephemeral=True)
            return

        term = {
            "Term": str(word).title(),
            "Definition": str(definition)
        }
        mycol.update_one({"ID": "Total"}, {"$push": {"All": str(word).title()}})
        mycol.insert_one(term)
        await ctx.respond(f"Successfully added {str(word).title()} to the dictionary")
        return

    @commands.slash_command(name="tonetags")
    async def tonetags(self, ctx):
        """Get a list of tonetags"""
        embed = discord.Embed(title="Tags",
                              description="""
                              ***Common tone tags***:\n\n
                              /j - Joking\n
                              /hj - Half-Joking\n
                              /s - Sarcastic\n
                              /srs - Serious\n
                              /gen - Genuine\n
                              /ly - Lyrics\n
                              /p - Platonic\n
                              /r - Romantic\n
                              /nm - Not Mad\n
                              """,
                              colour=0xA020F0)
        embed.set_footer(text="Wanna see more tags? Suggest it using the /suggesttone command!")
        await ctx.respond(embed=embed)
        return

    @commands.slash_command(name="suggesttone")
    async def suggesttone(self, ctx, tonetag: discord.Option(description="Tone tag that you want added")):
        """Suggest tonetags that can be added to the /tonetags list"""
        embed = discord.Embed(title="Tonetag Suggestion",
                              description=tonetag,
                              color=0xA020F0)
        channel = await self.bot.fetch_channel(991806371815243836)
        await channel.send(embed=embed)
        await ctx.respond("Successfully logged your suggestion!")
