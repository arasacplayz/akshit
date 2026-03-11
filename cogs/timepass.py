import discord
from discord.app_commands.commands import describe
from discord import app_commands
from discord.ext import commands
import random
import json
import google.generativeai as genai
from google.generativeai import types


class tp(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  genai.configure(api_key="AIzaSyCS4PfDCuopSVoqibFSRWpFZP1-Tn89qvY") 
  model = genai.GenerativeModel("gemini-2.5-flash")
  
  @commands.hybrid_command(name = 'ask', description = 'Ask anything to AI')
  @describe(question = "The question you want to ask to AI")
  async def ask(self, ctx, *, question: str):
    await ctx.defer()
    await ctx.send_typing()
    response = self.model.generate_content(contents=question, generation_config=types.GenerationConfig(max_output_tokens=5000))
    r = response.text
    for i in r:
      if i == "$":
        r = r.replace("$", "")
    await ctx.send(embed = discord.Embed(title = "Ask", description = r, color = discord.Color(0x00ffff)))

  @commands.hybrid_command(name = 'anime', description = 'Gives a list of animes to watch')
  async def anime(self, ctx):
    await ctx.send(embed = discord.Embed(title="Popular Animes",
                                         description="1.Naruto\n2.One Piece\n3.JoJo's Bizarre Adventure\n4.Dragon Ball\n5.Death Note\n6.Attack on Titan\n7.Hunter x Hunter\n8.Bleach\n9.Demon Slayer\n10.My Hero Academia\n11.Jujutsu Kaisen\n12.Suzae San \n13.Monster \n14.One Piece \n15.Chainsaw Man",
                                         color = discord.Color(0x00ffff)))



  # Slash command send a pic of a dog.
  @commands.hybrid_command(description='Generates a random pic of a dog')
  async def dog(self, ctx):
    dog = [
      "d0.jpeg", "d1.jpeg", "d2.jpeg", "d3.jpeg", "d4.jpeg", "d5.jpeg",
      "d6.jpeg", "d7.jpeg", "d8.jpeg", "d9.jpeg"
    ]
    a = random.choice(dog)
    with open(f'dog_img/{a}', 'rb') as f:
      picture = discord.File(f)
    await ctx.send(file=picture)


  # Slash command send a pic of a cat.
  @commands.hybrid_command(description='Generates a random pic of a cat')
  async def cat(self, ctx):
    cat = [
      "c0.jpeg", "c1.jpeg", "c2.jpeg", "c3.jpeg", "c4.jpeg", "c5.jpeg",
      "c6.jpeg", "c7.jpeg", "c8.jpeg", "c9.jpeg"
    ]
    a = random.choice(cat)
    with open(f'Cat_Img/{a}', 'rb') as f:
     picture = discord.File(f)
    await ctx.send(file=picture)


  # Slash command to show to mc servers
  @commands.hybrid_command(name='servers', description='Shows the minecraft servers')
  async def mc_servers(self, ctx):
    await ctx.send(embed = discord.Embed(title="Minecraft Servers",
                                        description="1. Mob Fight:                 MobFight.aternos.me:22378 \n2. PVP:                             PVP12.aternos.me:12940 \n3. Slenderman :             Slender212.aternos.me:62887 \n4. Pvp using mana :      PVPCHAMP.aternos.me:44874 \n5. Lucky block race :    LuckyGo.aternos.me:63965",
                                        color = discord.Color(0x00ffff)))


  # Slash command to send the link of the channel.
  @commands.hybrid_command(name='link', description='Sends the link of the channel')
  async def link(self, ctx):
    if ctx.author.id in (868016741207384114, 810724561850859520, 885361344440844338):
      await ctx.send(embed = discord.Embed(title="Arasac Playz",
                                         description="Link to our YouTube Channel [Arasac Playz](https://www.youtube.com/@ArasacPLayz)",
                                         color = discord.Color(0x00ffff)))
    else:
     await ctx.send(embed = discord.Embed(title = 'Mod Only',
                                           description = "Sry, you cannot use this command", 
                                           color = discord.Color.red()))


  # Slash command to send the link of a Google Meet.
  @commands.hybrid_command(name='meet', description='Sends the link of the Google Meet')
  async def meet(self, ctx):
    if ctx.author.id in (868016741207384114, 810724561850859520, 885361344440844338, 939439082612871218):
      await ctx.send(embed = discord.Embed(title="Google Meet", 
                                         description="[Click here](https://meet.google.com/ffj-yptd-mqs) to join the meet",
                                         color = discord.Color(0x00ffff)))
    else:
      await ctx.send(embed = discord.Embed(title = 'Mod Only',
                                           description = "Sry, you cannot use this command", 
                                           color = discord.Color.red()))


  # Slash command to suggest games.
  @commands.hybrid_command(name='suggest', description='Suggests games')
  async def suggest(self, ctx):
    await ctx.send(embed = discord.Embed(title="Popular Games",
                                         description='Here are some games you can play:\n1. Minecraft \n2. Apex Legends \n3. Ironsight \n4. Warframe \n5. A Plague Tale \n6. Valorant \n7. Fortnite \n8. Genshin Impact \n9. Call of Duty \n10. Rocket League \n11. Fall Guys',
                                         color = discord.Color(0x00ffff)))


  # Slash command to sugget high level games.
  @commands.hybrid_command(name='suggest_high', description='Suggests games which require high end pc')
  async def suggest_high(self, ctx):
    await ctx.send(embed = discord.Embed(title="High End Games",
                                         description='Here are some games you can play:\n1. GTA V \n2. Cyberpunk \n3. Farcry \n4. RDR II \n5. Elden Ring \n6. Horizon Zero Dawn \n7. The Last of Us \n8. The Witcher \n9. Resident Evil \n10. Uncharted 4',
                                         color = discord.Color(0x00ffff)))


  # Slash command to spam a specific message.
  @commands.hybrid_command(name= 'spam', description='Spams a message')
  async def spam(self, ctx, number: int, *, message: str):
    try:
      if message.lower() == 'x':
        for i in range(0, number):
            await ctx.send('<a:khoonright:913401708422520832><a:rickroll:913403675899211776><a:khoonleft:913401708699353108>')

      elif message.lower() == 'anything':
        data = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
            'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
            '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*',
            '(', ')', '_', '-', '=', '+', '[', ']', '{', '}', ':', ';', '"', "'",
            ',', '.', '?', '/', '|', '~', '`', '>', '<'
        ]
        n = random.randint(551, 601)
        for j in range(1, number + 1):
          Fspam = []
          for i in range(1, n + 1):
            spam = random.choice(data)
            Fspam.append(spam)
            VFspam = ''.join(Fspam)
          await ctx.send(VFspam)

      else:
        z = 0
        for j in message.split(' '):
          if j == '<@868016741207384114>':
            z = 1
          else:
            pass
        if z == 0:   
          for i in range(0, number):
            await ctx.send(message)
        else:
          for i in range(1, 11):
            await ctx.send(message)
    except:
      await ctx.send(f'U missed the `number` argument. \nUsage: `{ctx.prefix}spam <number> {message}`')
   


  @commands.hybrid_command(name = 'maal')
  async def m(self, ctx):
    if ctx.author.id in (810724561850859520, 868016741207384114):
      await ctx.send(embed = discord.Embed(title = 'Padhai ka Maal Paani', description = '[Click here](https://drive.google.com/drive/folders/1TVwLLxEqQ1mnmoW8K5_P4x_f6KBFKWLj?usp=drive_link) to access the you **Maal Paani**', color = discord.Color(0x00ffff)))
    else:
      await ctx.send(embed = discord.Embed(title="Not Authorized", description="you are not authorized to use this command", color = discord.Color.red()))
  
  
  @commands.hybrid_command(name = 'count', aliases = ['cnt'])
  async def akshit(self, ctx):
    
    with open('./coins.json', 'r') as f:
      data = json.load(f)

    await ctx.send(embed = discord.Embed(title = "Akshiting Count", description = f"You have spoken 'Akshit' `{data[str(ctx.author.id)]['akshit']}` times nooiice!! :thinking:", color = discord.Color(0x00ffff)))

  

async def setup(bot: commands.Bot):
  await bot.add_cog(tp(bot))