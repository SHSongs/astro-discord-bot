
import discord
from discord.ext.commands import Bot
from env import Tocken

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

bot.run(Tocken)
