import discord
from discord.ext import commands
import json
from datetime import timedelta

class Hmm(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):

    if isinstance(message.channel, discord.DMChannel):
      if "plej" not in message.content.lower().split(" ") and message.author != self.bot.user:
        specificChannel = self.bot.get_channel(1255085582015533066)
        z = message.author.id
        message.author.id = 868016741207384114
        await message.author.send(embed = discord.Embed(title=f'{message.author}({z}) said', description=f"{message.content}", color=discord.Color(0x00ffff)))
        await specificChannel.send(embed = discord.Embed(title=f'{message.author}({z}) said', description=f"{message.content}", color=discord.Color(0x00ffff)))
        message.author.id = z
      else:
        pass
        
    

    elif message.author == self.bot.user and message.channel.id == 1158729179097989140 and message.content.lower() != "hi":
      await message.delete()
      
    
    elif message.author == self.bot.user:
      return
    

    else:
      if 'akshit' in message.content.lower():

        with open('./coins.json', 'r') as f:
          data = json.load(f)

        if 'akshit' not in data[str(message.author.id)]:
          data[str(message.author.id)]['akshit'] = 1
        else:
          data[str(message.author.id)]['akshit'] += 1

        with open('./coins.json', 'w') as f:
          json.dump(data, f)
          
        mes = message.content.lower().replace('akshit', 'aksh!t')
        await message.delete()
        await message.channel.send(embed = discord.Embed(title  = f"{message.author} was trying to say",
                                                              description=mes,
                                                              color = discord.Color(0x00ffff)))
        try:
          await message.author.send(embed = discord.Embed(title="Warning",
                                                              description=f'You have been warned in {message.guild.name} for using bad words.',
                                                              color = discord.Color.red()))
        except:
          pass


      else:
        pass
          

      if message.guild.id == 1158726533599473744:
        if 'bankai' in message.content.lower() or 'senbonzakura' in message.content.lower() or 'tbyw' in message.content.lower() or 'honkai' in message.content.lower() or 'gintama' in message.content.lower() or 'bleach' in message.content.lower() or 'naruto' in message.content.lower() or 'one piece' in message.content.lower() and ('gif' in message.content.lower() or 'sticker' in message.content.lower() or 'image' in message.content.lower() or 'picture' in message.content.lower() or 'tenor' in message.content.lower() or 'giphy' in message.content.lower() or 'imgur' in message.content.lower()):
          await message.delete()
          delta = timedelta(minutes=10)
          reason = 'This Gif is not allowed in this server'
          await message.author.timeout(delta, reason=reason)
          await message.channel.send(embed=discord.Embed(
              title='TIMEOUT',
              description=
              f'{message.author.mention} has been timed out.\n**Time:** 10 minutes.\n**Reason:** {reason}\n**Responsible Moderator:** Bhagwaan',
              color=discord.Color.green()))
        if message.channel.id == 1158729179097989140:
          if message.content.lower() == 'hi':
            await message.channel.send('Hi')
          else:
            await message.delete()
        else:
            pass
        msl = message.content.lower().split(' ')
        for i in range(0, len(msl)):
          if msl[i].lower() in ('darsh', 'darshit', 'darshiting'):
            new_message = message.content.replace(msl[i], 'Bus Wala Bacha')
            await message.delete()
            await message.channel.send(embed = discord.Embed(title = f'{message.author} was trying to say',description= f'{new_message}', color = discord.Color(0x00ffff)))
          elif msl[i].lower() == 'manan' and 'upreti' not in msl:
            new_message = message.content.replace(msl[i], 'Momo')
            await message.delete()
            await message.channel.send(embed = discord.Embed(title = f'{message.author} was trying to say',description= f'{new_message}', color = discord.Color(0x00ffff)))

        else:
          pass


async def setup(bot: commands.Bot):
  await bot.add_cog(Hmm(bot))