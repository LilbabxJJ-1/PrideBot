import random

import discord
from discord.ext import tasks
from tokens import *
from discord.ext import commands as cd
from commands import dictionary as dic, pronouns as pro, support as sup, fun
from commands.profile import profile
import topgg

intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='Myself Being built')
bot = cd.Bot(case_insensitive=True, intents=intents, help_command=None, activity=activity, chunk_guilds_at_startup=False)

dbl_token = dbltoken  # set this to your bot's Top.gg token
bot.topggpy = topgg.DBLClient(bot, dbl_token, autopost=True, post_shard_count=True)


@bot.event
async def on_interaction(interaction):
    count = profiles.find_one({"_id": "total_commands"})
    if count is None:
        new = {
            "_id": "total_commands",
            "Count": 0
        }
        profiles.insert_one(new)
    else:
        profiles.update_one({"_id": "total_commands"}, {"$set": {"Count": count["Count"] + 1}})
    users = banned.find_one({"get": "get"})
    for i in users["Banned"]:
        if interaction.user.id == i:
            await interaction.channel.send("You have been banned from using this bot")
            return
    else:
        await bot.process_application_commands(interaction)


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


@tasks.loop(seconds=40)  # How often the bot should change status, mine is set on every 40 seconds
async def changepresence():
    Owner = await bot.fetch_user(bot.owner_id)
    game = [
            'Myself Being built',
            f"Over {len(bot.users)} users",
            f"Helping {len(bot.guilds)} guilds come out",
            f"Created by {Owner.name}"
        ]
    await bot.change_presence(activity=discord.ActivityType.watching(name=random.choice(game)))


@bot.slash_command(name="support-server")
async def server(ctx):
    """Join the PrideBot support server"""
    embed = discord.Embed(title="Support Server",
                          description="PrideBot Suppport Server Invite [here](https://discord.gg/JsztWV2zMd)",
                          color=0xA020F0)
    await ctx.respond(embed=embed)


@bot.event
async def on_guild_join(ctx):
    embed = discord.Embed(title="New server!",
                          description=f"{ctx.name} invited me!",
                          color=0xA020F0)
    channel = await bot.fetch_channel(991806371815243836)
    await channel.send(embed=embed)
    return


@bot.slash_command(name="bot-info")
async def botinfo(ctx):
    """See information about PrideBot"""
    procount = profiles.count_documents({})
    defcount = mycol.count_documents({})
    count = profiles.find_one({"_id": "total_commands"})
    embed = discord.Embed(title="Bot Info",
                          description=f"**Name**: PrideBot\n**ID**: {bot.user.id}\n**Slash-Commands**: {len(bot.application_commands)}\n**Users**: {len(bot.users)}\n**Servers**: {len(bot.guilds)}"
                                      f"\n**Definitions**: {defcount}\n**Profiles Created**: {procount}\n",
                          color=0xA020F0)
    embed.set_thumbnail(url=bot.user.avatar)
    embed.set_footer(text="Invite me to your server with /invite")
    await ctx.respond(embed=embed)
    return


@bot.slash_command(name="whats-new")
async def newupdate(ctx):
    """Get news on what updates were recently made to PrideBot"""
    new = mycol.find_one({"ID": "Updates"})
    text = new["updateDescription"].replace(r"\n", "\n")
    embed = discord.Embed(title=new["updateTitle"],
                          description=text,
                          color=0xA020F0)
    embed.set_thumbnail(url=bot.user.avatar)
    embed.set_footer(text="Check back anytime for updates")
    await ctx.respond(embed=embed)


@bot.slash_command(name="make-update")
async def makeupdate(ctx, title, update):
    """For bot owner to make updates"""
    if await bot.is_owner(ctx.author) is not True:
        return
    mycol.update_one({"ID":"Updates"}, {"$set":{"updateTitle": title}})
    mycol.update_one({"ID": "Updates"}, {"$set": {"updateDescription": update}})
    await ctx.respond("Successfully updated the what's new page")

@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, discord.ApplicationCommandInvokeError):
        await ctx.author.send("An error occurred, try again please.. 🌈 and make sure i have permission to speak in that channel", ephemeral=True)


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
    bot.add_cog(fun.funCommands(bot))


load_cogs()
# t = Thread(target=partial_run)
# t.start()

bot.run(TOKEN)
