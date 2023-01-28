import random
import discord
from discord.ext import commands
from tokens import *
profile = discord.SlashCommandGroup("profile", "Let everyone know who you are!")


@profile.command(name="create")
async def create(ctx, preferred_name: discord.Option(description="Your name"), sexuality: discord.Option(description="Sexuality you indentify as"),
                 pronouns: discord.Option(description="Pronouns you prefer"), gender: discord.Option(description="Gender you indentify as"), closeted: discord.Option(description="Are you in the closet or open?")):
    check = profiles.find_one({"ID": ctx.author.id})
    if check is not None:
        await ctx.respond("You already have a profile made!", ephemeral=True)
        return
    await ctx.send("Creating profile...", delete_after=5)
    user = {
        "ID": ctx.author.id,
        "Name": preferred_name,
        "Sexuality": sexuality,
        "Pronouns": pronouns,
        "Gender": gender,
        "Closet": closeted
    }
    profiles.insert_one(user)
    await ctx.respond(f"Profile made for {preferred_name.title()}!")


@profile.command(name="check")
async def check(ctx, user: discord.Option(discord.User, description="User who's profile you wish yo look at") = None):
    """Check out other users accounts or don't put a user to see your own"""
    if user is None:
        check = profiles.find_one({"ID": ctx.author.id})
        if check is None:
            await ctx.respond("No account found for this user! Please use /create first!")
            return
        embed = discord.Embed(title=f"{check['Name']}'s Profile",
                              description=f":name_badge:Name:name_badge:: {check['Name']}"
                                          f"\n----------------------\n\n📃Pronouns📃: {check['Pronouns']}"
                                          f"\n----------------------\n\n🌈Sexuality🌈: {check['Sexuality']}"
                                          f"\n----------------------\n\n♀Gender♂: {check['Gender']}"
                                          f"\n----------------------\n\nIn the closet?🚪: {check['Closet']}\n----------------------",
                              colour=0xA020F0)
        embed.set_footer(text=f"Welcome to {check['Name']}'s Profile")
        embed.set_thumbnail(url=ctx.author.avatar)
    else:
        check = profiles.find_one({"ID": user.id})
        if check is None:
            await ctx.respond("No account found for this user! Please use /create first!")
            return
        embed = discord.Embed(title=f"{check['Name']}'s Profile",
                              description=f":name_badge:Name:name_badge:: {check['Name']}"
                                          f"\n----------------------\n\n📃Pronouns📃: {check['Pronouns']}"
                                          f"\n----------------------\n\n🌈Sexuality🌈: {check['Sexuality']}"
                                          f"\n----------------------\n\n♀Gender♂: {check['Gender']}"
                                          f"\n----------------------\n\nIn the closet?🚪: {check['Closet']}\n----------------------",
                              colour=0xA020F0)
        embed.set_footer(text=f"Welcome to {check['Name']}'s Profile")
        embed.set_thumbnail(url=user.avatar)
    return await ctx.respond(embed=embed)


@profile.command(name="Name")
async def Name(ctx, name: discord.Option(discord.User, description="Update name status")):
    """Update the name on your profile"""
    user = profiles.find_one({"ID": ctx.author.id})
    if user is None:
        await ctx.respond("No account found for this user! Please use /create first!")
        return

    profiles.update_one({"ID":ctx.author.id}, {"$set":{"name": name}})
    await ctx.respond("Successfully updated your Name status")

@profile.command(name="pronouns")
async def pronouns(ctx, pronouns: discord.Option(discord.User, description="Update pronouns")):
    """Update the pronouns on your profile"""
    user = profiles.find_one({"ID": ctx.author.id})
    if user is None:
        await ctx.respond("No account found for this user! Please use /create first!")
        return

    profiles.update_one({"ID":ctx.author.id}, {"$set":{"Pronouns": pronouns}})
    await ctx.respond("Successfully updated your pronouns")


@profile.command(name="sexuality")
async def sexuality(ctx, sexuality: discord.Option(discord.User, description="Update sexuality")):
    """Update your profile sexuality"""
    user = profiles.find_one({"ID": ctx.author.id})
    if user is None:
        await ctx.respond("No account found for this user! Please use /create first!")
        return

    profiles.update_one({"ID":ctx.author.id}, {"$set":{"Sexuality": sexuality}})
    await ctx.respond("Successfully updated your Sexuality")


@profile.command(name="closeted")
async def Closested(ctx, closet: discord.Option(discord.User, description="Update closet status")):
    """Update the closet on your profile"""
    user = profiles.find_one({"ID": ctx.author.id})
    if user is None:
        await ctx.respond("No account found for this user! Please use /create first!")
        return

    profiles.update_one({"ID":ctx.author.id}, {"$set":{"Closet": closet}})
    await ctx.respond("Successfully updated your Closet status")


@profile.command(name="gender")
async def Gender(ctx, gender: discord.Option(discord.User, description="Update gender status")):
    """Update the gender on your profile"""
    user = profiles.find_one({"ID": ctx.author.id})
    if user is None:
        await ctx.respond("No account found for this user! Please use /create first!")
        return

    profiles.update_one({"ID":ctx.author.id}, {"$set":{"Gender": gender}})
    await ctx.respond("Successfully updated your Gender status")