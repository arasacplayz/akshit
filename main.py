# Imports
import discord
import os
from discord.ext import commands
from discord.ui import View
from discord import ButtonStyle
import cofig

# Making of bot and providing intents
bot = commands.Bot(command_prefix="plej ",case_insensitive = True ,intents=discord.Intents.all())

def getprefix(bot, msg):
  return ['plej ', 'plej']

exts = [
    'cogs.level',
    'cogs.timepass',
    'cogs.welcomer',
    'cogs.error',
    'cogs.meme',
    'cogs.hmm',
    'cogs.coins',
    'cogs.coins2',
    'cogs.mod',
    'cogs.buttons'
]


@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  for ext in exts:
    await bot.load_extension(ext)
    print(f'{ext} loaded')
  print('All cogs loaded')
  await bot.tree.sync()
  print('Synced slash commands')
  await bot.change_presence(activity=discord.Game(name = "GTA VI"))
  
@bot.event
async def on_message(msg):
  pfx = getprefix(bot, msg)[1]
  if msg.content.lower().startswith(pfx):
    msg.content = msg.content[:len(pfx)].lower() + msg.content[len(pfx):]
  await bot.process_commands(msg)
  





bot.run(cofig.token)
