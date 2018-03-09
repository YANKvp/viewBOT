
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import logging
import random
import chalk

bot=commands.Bot(command_prefix=">")
Odzywkismierci = ["%s Utopił się w odrze 'Przypadkiem':smiling_imp:", "Zestrzeliłem %s ze snajperki RIP :skull_crossbones: ", " %s spotkał gigantycznego smoka.'Było kościste'-smok powiedział :relieved:"]


@bot.event
async def on_ready():
    print("Bot zostal podlaczony pod ViewPoint!")


@bot.command()
async def test():
    await bot.say("test")
@bot.command()
async def dupa():
    await bot.say("dupa")

@bot.command (pass_context = True)
async def echo (ctx, *, echo:str):
    await bot.delete_message(ctx.message)
    await bot.say (" echo: " + echo)

@bot.command (pass_context = True)
async def zabij (ctx, *, member : discord.Member  = None):
    if member is None:
        await bot.say (ctx.message.author.mention + ": Nie możesz kogoś zabic nie mówiąc mi jego nicku!")
        return

    if member.id =="421446462669324288":
        await bot.say(ctx.message.author.mention + ": Jak mnie zabijesz skoro ja zabiję ciebie pierwszy! :knife: :smiley:")
    elif member.id == "418857781244985367" and member.id ==ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": Stworzycielu czy jesteś pewny?")
    elif member.id =="418857781244985367":
        await bot.say(ctx.message.author.mention + ": Czy ty właśnie sprobowałeś zabić mojego mistrza?! :rage:")
    elif member.id == ctx.message.author:
        await bot.say (ctx.message.author.mention + ": Dlaczego miałbym cię zabić?")
    else:
        random.seed(time.time())
        wybor = Odzywkismierci[random.randrange (0, len(Odzywkismierci))] % member.mention
        await bot.say(ctx.message.author.mention + ": " + wybor)

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}Dashboard użytkownika".format(user.name), description="Oto Znalezione informacje.", color=0x00ff00)
    embed.add_field(name="Nick", value=user.name, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Ranga", value=user.top_role)
    embed.add_field(name="Dołączył", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

    
@bot.command(pass_context=True)
async def piwo(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + " Otrzymał piwo od ViewBOT'a.:beer:")
    else:
        if member.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + " Poszedł na piwo! Sam... :beer:")
        else:
            await bot.say(ctx.message.author.mention + " postawił piwo dla" + member.mention +":beer:")

@bot.command(pass_context = True)
async def wybierz(ctx, *, choices: str):
    takisom = choices.split(",")
    chosen= takisom[random.randrange(len(takisom))]
    await bot.say(ctx.message.author.mention + ": Wybieram `" + chosen + "`")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {}Wyleciał z Serwera niczym kruk!!".format(user.name))
    await bot.kick(user)



   
	 
bot.run ("NDIxNDQ2NDYyNjY5MzI0Mjg4.DYNorQ.j3_JBbIu_vOU2LEtjID_y-UIw44")

