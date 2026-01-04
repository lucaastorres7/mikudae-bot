import discord

class MikudaeControls(discord.ui.View):
  def __init__(self, images, original_embed):
    super().__init__(timeout=120) # pode usar os botões por 2min
    self.images = images
    self.embed = original_embed
    self.current_index = 0

  def update_footer(self):
    self.embed.set_footer(text=f'{self.current_index + 1} / {len(self.images)}')

  @discord.ui.button(emoji='⬅️', style=discord.ButtonStyle.secondary)
  async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.current_index > 0:
      self.current_index -= 1
    else:
      self.current_index = len(self.images) - 1

    self.embed.set_image(url=self.images[self.current_index])
    self.update_footer()

    await interaction.response.edit_message(embed=self.embed, view=self)

  @discord.ui.button(emoji='➡️', style=discord.ButtonStyle.secondary)
  async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.current_index < len(self.images) - 1:
      self.current_index += 1
    else:
      self.current_index = 0

    self.embed.set_image(url=self.images[self.current_index])
    self.update_footer()

    await interaction.response.edit_message(embed=self.embed, view=self)