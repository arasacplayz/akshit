import discord
from discord.ext import commands
import random
from discord import Embed


class Meme(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  # Slash command to post arnav memes
  @commands.hybrid_command(name='arnav', description="Sends a arnav meme")
  async def arnav(self, ctx):
    if ctx.author.id in (868016741207384114, 810724561850859520, 885361344440844338):
      with open('memes/bakwas.png', 'rb') as f:
        picture = discord.File(f)

      with open('memes/bakwas_2.png', 'rb') as g:
        picture_2 = discord.File(g)

      with open('memes/bakwas_3.png', 'rb') as h:
        picture_3 = discord.File(h)
      arnav_memes = [
          '# Arnav at Sundays \nhttps://tenor.com/bMGPF.gif',
          '# Arnav everyday at school with Aksh*t \nhttps://tenor.com/bSbag.gif',
          '# Arnav when gets bullied in almost every game \nhttps://tenor.com/bwvrW.gif',
          '# Arnav after playing arnav craft \nhttps://tenor.com/flPpVoXziaZ.gif',
          '# when Arnav do coding better than Raghav, then his feeling be like \nhttps://tenor.com/bWYu0.gif',
          '# Arnav after getting 49.5 in SSC half yearly exam \nhttps://tenor.com/lnQh6TsX2yo.gif',
          '# Arnav when finally learns circles',
          '# Arnav after doing botting for only 6 hours be like',
          '# Arnav when he thinks he can be equivalent to Adi if he sleeps and wake up late but the reality is'
      ]
      random_choice = random.randint(0, 8)
      if random_choice == 6:
        await ctx.send(arnav_memes[random_choice], file = picture)

      elif random_choice == 7:
        await ctx.send(arnav_memes[random_choice], file = picture_2)
        
      elif random_choice == 8:
        await ctx.send(arnav_memes[random_choice], file = picture_3)

      else:
        await ctx.send(arnav_memes[random_choice])
    else:
     await ctx.send(embed = discord.Embed(title = 'Mod Only',
                                           description = "Sry, you cannot use this command", 
                                           color = discord.Color.red()))

  # Slash command to post raghav memes.
  @commands.hybrid_command(name='raghav', description="Sends a raghav meme")
  async def raghav(self, ctx):
    if ctx.author.id in (868016741207384114, 810724561850859520, 885361344440844338):
      with open('memes/bwas_6.png', 'rb') as a:
        rag1 = discord.File(a)
      with open('memes/bwas.png', 'rb') as b:
        rag2 = discord.File(b)
      with open('memes/bwas_2.png', 'rb') as c:
        rag3 = discord.File(c)
      with open('memes/bwas_3.png', 'rb') as d:
        rag4 = discord.File(d)
      with open('memes/bwas_4.png', 'rb') as e:
        rag5 = discord.File(e)
      with open('memes/bwas_5.png', 'rb') as z:
        rag6 = discord.File(z)
      with open('memes/thad.mp4', 'rb') as x:
        rag7 = discord.File(x)

      raghav_meme = [
          "# Raghav after writing 'Shiv Ji Ganga hath mein lekar aaye the' in hindi exams \nhttps://tenor.com/view/im-so-proud-of-myself-dante-dangelo-satisfied-pleased-happy-with-myself-gif-26247343",
          "# Raghav after beating someone who is new to the game \nhttps://tenor.com/view/tumara-bhai-pro-hain-bhai-pro-hain-pro-you-are-pro-noob-gif-23317534",
          "# Raghav when trying to talk with someone \nhttps://tenor.com/view/raghav-raghav-sharma-rizz-rizzgav-rizzler-gif-27481075",
          "# Raghav after knowing that he would get 10k if he gets 90%+ in his exams. \nhttps://tenor.com/view/modi-dance-modi-gi-gif-9763089601276552202",
          "# Raghav whenever he gets bored.",
          "# Raghav to every thing he don't like.",
          "# Raghav after finding out his school don't teach coding but give practical work.",
          "# Raghav during science exams.",
          "# Raghav playing games 2 days later after deciding he won't play games.",
          "# Raghav when he wakes up realizing it's his exam tomorrow and he hasn't started.",
          "# Raghav after barely learning Int(input())."
      ]
      random_choice = random.randint(0, 10)
      if random_choice == 4:
        await ctx.send(raghav_meme[random_choice], file=rag1)
      elif random_choice == 5:
        await ctx.send(raghav_meme[random_choice], file=rag2)
      elif random_choice == 6:
        await ctx.send(raghav_meme[random_choice], file=rag3)
      elif random_choice == 7:
        await ctx.send(raghav_meme[random_choice], file=rag4)
      elif random_choice == 8:
        await ctx.send(raghav_meme[random_choice], file=rag5)
      elif random_choice == 9:
        await ctx.send(raghav_meme[random_choice], file=rag6)
      elif random_choice == 10:
        await ctx.send(raghav_meme[random_choice], file=rag7)
      else:
        await ctx.send(raghav_meme[random_choice])
    else:
     await ctx.send(embed = discord.Embed(title = 'Mod Only',
                                           description = "Sry, you cannot use this command", 
                                           color = discord.Color.red()))

  # Slash command of thad thading
  @commands.hybrid_command(description = "Let's Thad Thad")
  async def thad(self, ctx):
    with open('memes/thad.mp4', 'rb') as f:
      video = discord.File(f)
    await ctx.send(file=video)


async def setup(bot: commands.Bot):
  await bot.add_cog(Meme(bot))
