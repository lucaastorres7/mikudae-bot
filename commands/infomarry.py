import aiohttp
from discord.ext import commands
import logging
import os
from utils.marryCard import marry_card
from utils.serieEmbed import serie_embed
from views.controls import MikudaeControls

class InfoMarry(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.backend_url = os.getenv('BACKEND_URL')

  @commands.command()
  async def im(self, ctx: commands.Context, *, name=None): # infomarry
    try:
      if not name:
        raise ValueError('No character name provided')

      async with aiohttp.ClientSession() as session:
        async with session.get(f'{self.backend_url}/characters?name={name}') as res:
          data = await res.json()
          if res.status != 200:
            raise Exception({'error': data['message'], 'status': data['statusCode']})
          
          serie = data['series'][0]['serie']['name']
          images = data['images']

          embed = await marry_card(
            data['name'],
            serie,
            data['gender'],
            data['category'],
            images,
            data['kakeraValue']
          )

          if len(images) == 1:
            await ctx.send(embed=embed)
          else:
            view = MikudaeControls(images=images, original_embed=embed)
            await ctx.send(embed=embed, view=view)

    except Exception as e:
      if isinstance(e, ValueError):
        await ctx.send(f'Sintaxe: **!im** <Personagem>')
      else:
        await ctx.send(f'**{ctx.author.display_name}**, deu ruim. Nenhum personagem encontrado.')
      
      logging.error(f'{e}') 

  @commands.command()
  async def ima(self, ctx: commands.Context, *, serie=None): # infomarryseries
    try:
      if not serie:
        raise ValueError('No serie provided')
      
      async with aiohttp.ClientSession() as session:
        async with session.get(f'{self.backend_url}/series?name={serie}') as res:
          data = await res.json()
          if res.status != 200:
            raise Exception({'error': data['message'], 'status': data['statusCode']})

          embed = await serie_embed(data)

          await ctx.send(embed=embed)

    except Exception as e:
      if isinstance(e, ValueError):
        await ctx.send(f'Sintaxe: **!ima** <série>')
      else:
        await ctx.send(f'**{ctx.author.display_name}**, Alô meu patrão? Tá na disney? Verifique a ortografia.')
      
      logging.error(f'{e}')

async def setup(bot):
  await bot.add_cog(InfoMarry(bot))