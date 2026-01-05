import discord
from discord.ext import commands

class MarryReact(discord.ui.View):
  def __init__(self, ctx: commands.Context, original_embed):
    super().__init__(timeout=40) # pode usar os botões por 40s
    self.ctx = ctx
    self.embed = original_embed

  def update_footer(self):
    self.embed.set_footer(text=f'Pertence a {self.ctx.author.display_name}')

  @discord.ui.button(emoji='💕', style=discord.ButtonStyle.secondary)
  async def marry(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.update_footer()
    await interaction.response.edit_message(embed=self.embed, view=self)