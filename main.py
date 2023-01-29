import discord
from tokens import *
from discord.ext import commands as cd
from commands import dictionary as dic, pronouns as pro, support as sup
from commands.profile import profile
import topgg

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='Myself Being built')
bot = cd.Bot(case_insensitive=True, intents=intents, help_command=None, activity=activity, chunk_guilds_at_startup=False)


dbl_token = dbltoken  # set this to your bot's Top.gg token
bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)


@bot.event
async def on_interaction(interaction):
    users = banned.find_one({"get":"get"})
    for i in users["Banned"]:
        if interaction.author.id == i:
            interaction.respond("You are banned from using this bot, sorry for the inconvenience")
            return
    else:
        bot.process_application_commands(interaction)



@bot.slash_command(name="bcount")
async def count(ctx):
    await ctx.respond(f"Bot is in {len(bot.guilds)} guilds!")

@bot.slash_command(name="vote")
async def vote(ctx):
    """Vote for the bot TopGG"""
    embed = discord.Embed(title="Vote for PrideBot",
                          description="If you're enjoying PrideBot, please consider leaving a review on Top.gg! https://top.gg/bot/1066641327116255333#reviews",
                          color=0xA020F0)
    await ctx.respond(embed=embed)

@bot.event
async def on_autopost_success():
    print(
        f"Posted server count ({bot.topggpy.guild_count}), shard count ({bot.shard_count})"
    )


@bot.event
async def on_guild_join(ctx):
    embed = discord.Embed(title="New server!",
                          description=f"{ctx.name} invited me!",
                          color=0xA020F0)
    channel = await bot.fetch_channel(991806371815243836)
    await channel.send(embed=embed)
    return

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ApplicationCommandInvokeError):
        await ctx.respond("An error occurred, try again please.. 🌈", ephemeral=True)


@bot.slash_command(name="donate")
async def donate(ctx):
    """Donate to the Owners College GoFundMe"""
    embed = discord.Embed(title="Like the bot?",
                          description="If you're enjoying PrideBot, please consider donating to the owners GoFundMe to help them go to college! Thank you so much for your consideration and help to my future!"
                                      "\n--> https://gofund.me/557611f3",
                          colour=0xA020F0)
    await ctx.respond(embed=embed)

@bot.slash_command(name="invite")
async def invite(ctx):
    """Get an invitation for the bot"""
    embed = discord.Embed(title="PrideBot Invite",
                          description="You can invite PrideBot [here](https://discord.com/api/oauth2/authorize?client_id=1066641327116255333&permissions=414464674880&scope=bot%20applications.commands)",
                          colour=0xA020F0)
    await ctx.respond(embed=embed)
    return






def load_cogs():
    bot.add_cog(dic.DictionaryCommands(bot))
    bot.add_cog(pro.pronounCommands(bot))
    bot.add_cog(sup.supportCommands(bot))
    bot.add_application_command(profile)

load_cogs()

bot.run(TOKEN)
