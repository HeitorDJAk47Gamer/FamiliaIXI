import os
import json
import disnake
import json
import asyncio
import datetime
import os
import random
from disnake.ext import commands
from disnake.ui import Select, View

with open('config.json') as e:
  infos = json.load(e)
  token = infos['token']

fml = commands.Bot(command_prefix='fml!', case_insensitive=True, intents=disnake.Intents.all())

@fml.event
async def on_ready():
  calc = fml.latency * 1000
  pong = round(calc)
  print('Online!')
  print(f'Ping: {pong} ms')

class Menu(disnake.ui.View):
  def init (self):
    super()._init_()
    self.value = None

  @disnake.ui.button(label='clique aqui!', style=disnake.ButtonStyle.red)
  async def menu(self, button : disnake.ui.Button, interaction : disnake.Interaction):
    await interaction.response.send_message(f'{interaction.author.mention} Voçê é gay!')

@fml.slash_command(name='hello', description='sla bixo, oi!')
async def hello(inter):
  await inter.response.send_message(f'Comnado fumfando {inter}', view=Menu())

@fml.command()
async def calça(ctx, cal):
  x = eval(cal)
  await ctx.send(f'O cálculo é: {cal} = {x}')

fml.run(token)