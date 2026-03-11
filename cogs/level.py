import discord
from discord import user
from discord.ext import commands
import random
import json
import asyncio

class lvl(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
    

  @commands.Cog.listener()
  async def on_message(self, message):
    exp = random.randint(20,70)
    with open('./coins.json', 'r') as f:
      data = json.load(f)

    if message.author == self.bot.user:
      pass

    
    elif str(message.author.id) not in data:
      pass

    else:

      data[str(message.author.id)]['experience'] += exp

      if data[str(message.author.id)]['experience'] >= (data[str(message.author.id)]['level'] + 1) * 1000:
        data[str(message.author.id)]['experience'] -= (data[str(message.author.id)]['level'] + 1) * 1000
        data[str(message.author.id)]['level'] += 1
        await message.channel.send(embed = discord.Embed(title = 'Level Up', description = f"{message.author.mention} has leveled up to level {data[str(message.author.id)]['level']}!", color = discord.Color(0x00ffff)))
      else: 
        pass
    with open('./coins.json', 'w') as f:
      json.dump(data, f)


  
    
  @commands.hybrid_command(name='level', description='Check your level')
  async def level(self, ctx, member = None):
    with open('./coins.json', 'r') as f:
      data = json.load(f)
    if member is None:
      try:  
        await ctx.send(embed = discord.Embed(title = f"{ctx.author.name}'s level", description = f"You are **level {data[str(ctx.author.id)]['level']}!**\n**EXP:** {data[str(ctx.author.id)]['experience']}/{(data[str(ctx.author.id)]['level'] + 1) * 1000}", color = discord.Color(0x00ffff)))
      except:
        await ctx.send(embed = discord.Embed(description = f"You haven't stated playing\nUse `{ctx.prefix}balance` to start", color = discord.Color.red()))
    else:
      member = member.replace('<@', '')
      member = member.replace('>', '')
      member = await self.bot.fetch_user(int(member))
      try:
        await ctx.send(embed = discord.Embed(title = f"{member.name}'s level", description = f"You are **level {data[str(member.id)]['level']}!**\n**EXP:** {data[str(member.id)]['experience']}/{(data[str(member.id)]['level'] + 1) * 1000}", color = discord.Color(0x00ffff)))
      except:
        await ctx.send(embed = discord.Embed(description = f"You haven't stated playing\nUse `{ctx.prefix}balance` to start", color = discord.Color.red()))
async def setup(bot: commands.Bot):
  await bot.add_cog(lvl(bot))