import discord
from discord.ext import commands
from tokens import *
import random


class supportCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="pride-servers")
    async def prideServers(self, ctx):
        """Get a list of LGBTQ oriented discord servers"""
        embed = discord.Embed(title="Servers for LGBTQ+",
                              description="***This bot is not affiliated or associated with these servers at all!***\n\nLGTBTQ+ Hangout - https://www.discord.gg/Pride"
                                          "\nTranscord - https://discord.gg/trans\nThe LGBTQ+ Community - https://discord.gg/pridemonth\nEnby_eautiful - https://discord.gg/j8MCnEC64S",
                              colour=0xA020F0)
        embed.set_image(url="https://i.imgur.com/4M7IWwP.gif")
        await ctx.respond(embed=embed)
        chances = random.choice(list(range(1, 100)))
        if chances <= 15:
            embed = discord.Embed(title="Like the bot?",
                                  description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college!"
                                              "\n --> https://gofund.me/557611f3\nIf you can't donate, that's okay! You can still show your support by upvoting on Top.gg"
                                              "\n -->..https://top.gg/bot/1066641327116255333#reviews",
                                  colour=0xA020F0)
            await ctx.send(embed=embed)

    @commands.slash_command(name="support")
    async def support(self, ctx, type: discord.Option(description="Type of support info you need",
                                                      choices=['HRT', 'Therapy', "Hotlines", "Talking to Family", "Coming Out"])):
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
        chances = random.randint(1, 100)
        if chances <= 15:
            embed = discord.Embed(title="Like the bot?",
                                  description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college!"
                                              "\n --> https://gofund.me/557611f3\nIf you can't donate, that's okay! You can still show your support by upvoting on Top.gg"
                                              "\n -->..https://top.gg/bot/1066641327116255333#reviews",
                                  colour=0xA020F0)
            await ctx.send(embed=embed)

    @commands.slash_command(name="help")
    async def help(self, ctx, category: discord.Option(str, choices=['Definitions', 'Pronouns', "Support", "Profile", "Fun", "Misc"])):
        """Find out commands in a specific category and what it does"""
        if category == "Definitions":
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" </define:1067134957723594772> `term` - Defines a given LGBTQ related term | Leave term blank for word list\n"
                                              f" </suggest-definition:1072923893951627334> `term` `definition`\n"
                                              f" </tonetags:1067884336868769803> - Gives a list of common tonetags\n"
                                              f" </suggest-tonetags:1067884336868769804> `tonetag` `Meaning` - Allows user to suggest a tonetag to the /tonetags list",
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)
        elif category == "Pronouns":
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" </test-pronouns:1067343985900785695> - Use to test out pronouns (BETA):\n-`Name`\n-`Subjective Pronouns`\n-`Objective Pronouns`\n"
                                              f"-`Possessive Determiner`\n-`Possessive Pronoun`\n-`Reflective Pronoun`\n"
                                              f" </suggest-pronouns:1067184141352845344> `sentence` - Suggest sentences to better the future of the pronoun command",
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)
        elif category == "Support":
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" </pride-servers:1067197553109635162> - Shows a list of safeplaces that you can join!\n"
                                              f" </support:1067333840877658142> `type` (Shown below):\n- Hrt\n - Therapy\n - Hotlines\n - Talking to familiy\n - Coming out\n"
                                              f" </whats-new:1076235433022865470> - Get news on updates on PrideBot`",
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)
        elif category == "Profile":
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" /profile create - Create a profile to keep people up to date on your identity\n"
                                              f" /profile check `user` - Look at someone's profile. To look at your own, don't add a user\n"
                                              f" /profile name `new name` - Update the name on your profile\n"
                                              f" /profile sexuality `new sexuality` - Update the sexuality on your profile\n"
                                              f" /profile pronouns `new pronouns` - Update the pronouns on your profile\n"
                                              f" /profile closet `new closet status` - Update the closet status on your profile\n"
                                              f" /profile gender `new gender` - Update the gender on your profile\n"
                                  ,
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)
        elif category == "Fun":
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" </jail:1072951756625023007> - Get an image of you in jail\n"
                                              f" </ship:1072951756625023006> - Ship 2 friends together\n"
                                              f" </whowouldwin:1072929546589978754> - Place your fighting bets against someone else!\n",
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
        else:
            embed = discord.Embed(title=f"Commands for {category}",
                                  description=f" </vote:1068765760568180806> - Vote and review the bot on TopGG\n"
                                              f" </invite:1067884336868769802> - Get an invite for the bot\n"
                                              f" </donate:1067349685041381406> - Donate to the Owners GoFundMe to help college funds\n"
                                              f" /help - This command",
                                  colour=0xA020F0)
            embed.set_footer(text="Remember to check out the other commands!")
            embed.set_thumbnail(url=self.bot.user.avatar)
            await ctx.respond(embed=embed)
