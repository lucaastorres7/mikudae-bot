import discord

async def marry_card(name, serie, gender, category, image_url, kakera_value):
  gender_emoji = '♀️♂️'
  category_class = 'Game & Animanga'

  if gender == 'WAIFU':
    gender_emoji = '♀️'
  elif gender == 'HUSBANDO':
    gender_emoji = '♂️'

  if category == 'ANIME':
    category_class = 'Animanga'
  elif category == 'GAME':
    category_class = 'Game'

  embed = discord.Embed(
    title=name,
    description=f'{serie} {gender_emoji}\n{category_class} • **{kakera_value}** 💷',
    color=0xf2a11f
  )

  embed.set_image(url=image_url[0])

  embed.set_footer(text=f'1 / {len(image_url)}')

  return embed