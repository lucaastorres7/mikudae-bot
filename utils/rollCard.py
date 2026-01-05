import discord

async def roll_card(name, serie, image_url, kakera_value):
  embed = discord.Embed(
    title=name,
    description=f'{serie}\n**{kakera_value}** 💷',
    color=0xf2a11f
  )

  embed.set_image(url=image_url)

  embed.set_footer(text=f'{name} / {serie} - {kakera_value} ka')

  return embed