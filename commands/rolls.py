import aiohttp
import logging
import os
import discord
from discord.ext import commands
from utils.rollCard import roll_card
from views.marryView import MarryReact

class Rolls(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.backend_url = os.getenv('BACKEND_URL')

  @commands.command()
  async def wa(self, ctx: commands.Context):
    """Roll an Animanga Waifu"""

    try:
      async with aiohttp.ClientSession() as session:
        payload = {
          'playerId': str(ctx.author.id),
          'serverId': str(ctx.guild.id)
        }

        async with session.post(f'{self.backend_url}/rolls/wa', json=payload) as res:
          data = await res.json()
          print(data)
          if res.status != 200:
            raise Exception({'error': data['message'], 'status': data['statusCode']})
          
          if data["rollSuccess"] is False:
            await ctx.send(f'**{ctx.author.display_name}**, os rolls são limitados a {data["rollsLimit"]} por hora. {data["minutesUntilReset"]} min restante(s).')
            return

          character = data['character']
          serie = character['series'][0]['serie']['name']
          image_url = character['images'][0]

          embed = await roll_card(
            character['name'],
            serie,
            image_url,
            character['kakeraValue']
          )
          view = MarryReact(ctx=ctx, original_embed=embed)
          
          await ctx.send(embed=embed, view=view)
    except Exception as e:
      logging.error(f'{e}')

async def setup(bot):
  await bot.add_cog(Rolls(bot))