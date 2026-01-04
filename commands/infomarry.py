import aiohttp
from discord.ext import commands
import logging
import os
from utils.marryCard import marry_card

class InfoMarry(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.backend_url = os.getenv('BACKEND_URL')

  @commands.command()
  async def im(self, ctx: commands.Context, *, name=None): # infomarry
    try:
      if not name:
        raise ValueError('No name provided')

      async with aiohttp.ClientSession() as session:
        async with session.get(f'{self.backend_url}/characters?name={name}') as res:
          data = await res.json()
          if res.status != 200:
            raise Exception({'error': data['message'], 'status': data['statusCode']})
          
          embed = await marry_card(
            data['name'],
            'VOCALOID', # Hardcoded for now
            data['gender'],
            data['category'],
            data['images'],
            data['kakeraValue']
          )

          await ctx.send(embed=embed)
    except Exception as e:
      if isinstance(e, ValueError):
        await ctx.send(f'Sintaxe: **!im** <Personagem>')
      else:
        await ctx.send(f'**{ctx.author.display_name}**, deu ruim. Nenhum personagem encontrado.')
      
      logging.error(f'{e}') 

async def setup(bot):
  await bot.add_cog(InfoMarry(bot))