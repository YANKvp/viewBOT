#Autor-YANK @2018ViewPoint

#import 
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import logging
import random
import chalk

#nadajemy prefix jaki jest potrzebny do dzialania komendy.
bot=commands.Bot(command_prefix=">")

#info do debugu 
@bot.event
async def on_ready():
    print("Bot zostal podlaczony pod ViewPointSerwer!")

#komendy(przyklad)
@bot.command()
async def komendajakas():
    await bot.say("tutaj np link do filmiku Youtube")


#Po prostu echo
@bot.command (pass_context = True)
async def echo (ctx, *, echo:str):
    await bot.delete_message(ctx.message)
    await bot.say (" echo: " + echo)


#Dashboard uzytkownikow	
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}Dashboard użytkownika".format(user.name), description="Oto Znalezione informacje.", color=0x00ff00)
    embed.add_field(name="Nick", value=user.name, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Ranga", value=user.top_role)
    embed.add_field(name="Dołączył", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

  
#system piw
@bot.command(pass_context=True)
async def piwo(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + " Otrzymał piwo od ViewBOT'a.:beer:")
    else:
        if member.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + " Poszedł na piwo! Sam... :beer:")
        else:
            await bot.say(ctx.message.author.mention + " postawił piwo dla" + member.mention +":beer:")

#system wybierania przez bota wpisanych przez uzytkownika tresci
@bot.command(pass_context = True)
async def wybierz(ctx, *, choices: str):
    takisom = choices.split(",")
    chosen= takisom[random.randrange(len(takisom))]
    await bot.say(ctx.message.author.mention + ": Wybieram `" + chosen + "`")

#kick
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: {}Wyleciał z Serwera niczym kruk!!".format(user.name))
    await bot.kick(user)



#podpinanie tokena bota  
bot.run ("---")


#troche syfowo ale caly czas ulepszam (nie wklejalem calego kodu jak cus, bot jest bardziej rozbudowany)
