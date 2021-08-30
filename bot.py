
import discord
from discord.ext.commands import Bot
from env import Tocken
import datetime
import moonday

intents = discord.Intents.default()
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 에 로그인하였습니다!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def hello(ctx):
    await ctx.reply('hello!')

@bot.command()
async def today(ctx):
    now=datetime.datetime.now()
    year=now.year
    month=now.month
    day=now.day

    dateString=f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    lunaday=moonday.get_luna_date(year,month,day)

    picture=discord.File(f"moon-img/test{lunaday[8:]}.jpg")
    await ctx.send(dateString+"\n"+lunaday,file=picture)



bot.run(Tocken)
