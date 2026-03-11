import discord
from discord.ext import commands

import json

class Welcomer(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member: discord.Member):
    with open('./data.json', 'r') as f:
      records = json.load(f)

    try:
      channel_id = records[str(member.guild.id)]
    except KeyError: 
      return
    channel = self.bot.get_channel(int(channel_id))
    await channel.send(f'Welcome {member.mention} to the server!')
      
  
  @commands.hybrid_command(description = "Sets the current channel as the welcome channel")
  async def welcome(self, ctx):
    with open('./data.json', 'r') as f:
      records = json.load(f)

    records[str(ctx.guild.id)] = str(ctx.channel.id)
    with open('./data.json', 'w') as f:
      json.dump(records, f)

    await ctx.send(f'Success!, {ctx.channel.mention} is your welcome channel')



async def setup(bot: commands.Bot):
  await bot.add_cog(Welcomer(bot))