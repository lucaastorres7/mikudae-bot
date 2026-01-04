import discord

async def serie_embed(data):
  serie_name = data['name']
  total_characters = len(data['characters'])

  name_list = []

  for item in data['characters']:
    character = item['character']
    name = character['name']
    name_list.append(name)

  description = '\n'.join(name_list)
  
  embed = discord.Embed(
    title=f'{serie_name}   0/{total_characters}',
    description=description,
    color=0xbd2424
  )

  embed.set_footer(text='1 / 1')
  return embed