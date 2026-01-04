import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
BACKEND_URL = os.getenv('BACKEND_URL')

logging.basicConfig(
  level=logging.ERROR,
  format='%(asctime)s - %(levelname)s - %(message)s',
  handlers=[
    logging.FileHandler('discord.log', encoding='utf-8', mode='a'),
    logging.StreamHandler()
  ]
)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'{bot.user.name} is ready to be used!')

@bot.command()
async def wa(ctx):
  try:
    async with aiohttp.ClientSession() as session:
      async with session.get(f'{BACKEND_URL}/characters/1') as res:
        data = await res.json()
        await ctx.send(data['name'])
  except Exception as e:
    await ctx.send('Mikudae is going through tough times right now. 😔')
    logging.error(f'{e}') 

bot.run(token, log_handler=handler, log_level=logging.ERROR)