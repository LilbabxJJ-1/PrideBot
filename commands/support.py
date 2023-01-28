import discord
from discord.ext import commands
from tokens import *
import random


class supportCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="prideservers")
    async def prideServers(self, ctx):
        """Get a list of LGBTQ oriented discord servers"""
        embed = discord.Embed(title="Servers for LGBTQ+",
                              description="***This bot is not affiliated or associated with these servers at all!***\n\nLGTBTQ+ Hangout - https://www.discord.gg/Pride"
                                          "\nTranscord - https://discord.gg/trans\nThe LGBTQ+ Community - https://discord.gg/pridemonth\nEnby_eautiful - https://discord.gg/j8MCnEC64S"
                                          "\nMore coming soon...",
                              colour=0xA020F0)
        await ctx.respond(embed=embed)
        chances = random.choice(list(range(1, 100)))
        # Come change this
        if chances <= 15:
            embed = discord.Embed(title="Like the bot?",
                                  description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college!"
                                              "\n --> https://gofund.me/557611f3\nIf you can't donate, that's okay! You can still show your support by upvoting on Top.gg"
                                              "\n -->..https://top.gg/bot/1066641327116255333#reviews",
                                  colour=0xA020F0)
            await ctx.send(embed=embed)

    @commands.slash_command(name="support")
    async def support(self, ctx, type: discord.Option(description="Type of support info you need", choices=['HRT', 'Therapy', "Hotlines", "Talking to Family", "Coming Out"])):
        """Get support as a person of the LGBTQ+ community"""
        if type == "HRT":
            embed = discord.Embed(title="Support for HRT",
                                  description="Keep in mind that if you're a minor (-17) you will need a parental consent for Hormone Replacement Therapy (HRT)"
                                              "\nSome helpful links:\n\nNHS UK - [Link](https://www.nhs.uk/conditions/hormone-replacement-therapy-hrt/)"
                                              "\nCleveland Clinic - [Link](https://my.clevelandclinic.org/health/treatments/21653-feminizing-hormone-therapy)"
                                              "\nMayo Clinic - [Link](https://www.mayoclinic.org/tests-procedures/masculinizing-hormone-therapy/about/pac-20385099)"
                                              "\nNCBI - [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5182227/)",
                                  colour=0xA020F0)
        elif type == "Therapy":
            embed = discord.Embed(title="Support for Therapy",
                                  description="Keep in mind that if you're a minor (-17) you will need a parental consent for therapy"
                                              "\nSome helpful links:\n\nNQTTCN - [Link](https://nqttcn.com/en/)"
                                              "\nTherapy For QPOC - [Link](https://www.therapyforqpoc.com/)"
                                              "\nFamily Connections Therapy - [Link](https://familyconnectionstherapy.com/therapy-solutions/lgbtq-child-teen-therapy/)"
                                              "\nThe Trevor Project - [Link](https://www.thetrevorproject.org/)",

                                  colour=0xA020F0)
        elif type == "Coming Out":
            embed = discord.Embed(title="Support for Coming Out",
                                  description="Some helpful links:\n\nPlanned Parenthood - [Link](https://www.plannedparenthood.org/learn/sexual-orientation/sexual-orientation/whats-coming-out)"
                                              "\nHealth Line - [Link](https://www.healthline.com/health/how-to-come-out)"
                                              "\nKids Health - [Link](https://kidshealth.org/en/teens/coming-out.html)"
                                              "\nWashington Edu - [Link](https://www.washington.edu/counseling/thinking-of-coming-out/)",
                                  colour=0xA020F0)
        elif type == "Hotlines":
            embed = discord.Embed(title="Hotlines",
                                  description="```diff\n"
                                              "- IF YOU ARE IN A BAD SITUATION (i.e. Have already done damage to yourself) GET OFF OF DISCORD AND CALL 911```\n"
                                              "Some helpful links:\n\nASFP - [Link](https://afsp.org/lgbtq-crisis-and-support-resources)"
                                              "\nStony Brook - [Link](https://www.stonybrook.edu/commcms/studentaffairs/lgbtq/resources/hotlines.php)"
                                              "\nLiam Carter - [Link](https://liamrcarter.wordpress.com/2015/09/05/list-of-lgbt-friendly-helplines-worldwide/)"
                                              "\nOstem - [Link](https://ostem.org/page/crisis-hotlines)",
                                  colour=0xA020F0)
        else:
            embed = discord.Embed(title="Support for Talking to family",
                                  description="Coming soon...",
                                  colour=0xA020F0)


        await ctx.respond(embed=embed)
        chances = random.choice(list(range(1, 100)))
        if chances <= 15:
            embed = discord.Embed(title="Like the bot?",
                                  description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college!"
                                              "\n --> https://gofund.me/557611f3\nIf you can't donate, that's okay! You can still show your support by upvoting on Top.gg"
                                              "\n -->..https://top.gg/bot/1066641327116255333#reviews",
                                  colour=0xA020F0)
            await ctx.send(embed=embed)



    #@commands.slash_command(name="help")
    #async def help(self, ctx, command: discord.Option(str, choices=['define', 'suggestpronouns', "prideservers", "hotlines", "support"])):
    #    """Find out what a command does and it's description"""
    #    command = commands.Bot.get_application_command(self.bot, command)
    #    embed = discord.Embed(title=f"Description for {command}",
    #                  description=f"Name: {command}\nParameters: {command._get_signature_parameters()}"
    #                              f"Description: {command}")
    #    await ctx.respond(embed=embed)