import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

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
  try:
    await bot.load_extension('commands.infomarry')
    print('Commands loaded successfully.')
  except Exception as e:
    print(f'Failed to load commands: {e}')

bot.run(TOKEN, log_handler=handler, log_level=logging.ERROR)