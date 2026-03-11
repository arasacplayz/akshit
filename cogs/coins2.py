import discord
from discord.ext import commands
import json
import random
import asyncio
from datetime import date, datetime, timedelta
from discord import app_commands

class coinsys(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  def inter(self, amount, msg):
    flag = 0
    mul = 1
    if amount.isdigit():
        return int(amount)
    
    elif '.' in amount and 'k' not in amount and 'm' not in amount:
      amount = 'galat'
      return amount
    
    elif amount.lower() in ('nan', 'inf', 'infinity'):
      amount = 'galat'
      return amount
    
    elif amount.isalpha() and amount.lower() not in ('max', 'all', 'half'):
      amount = 'galat'
      return amount
    
    elif amount.lower() in ('max', 'all') and str(msg.command.qualified_name) in ('with', 'withdraw'):
      with open('./coins.json', 'r') as f:
          data = json.load(f)
      amount = data[str(msg.author.id)]['bank']
      return amount
    elif amount.lower() in ('max', 'all'):
      with open('./coins.json', 'r') as f:
          data = json.load(f)
      amount = data[str(msg.author.id)]['wallet']
      return amount
    
    elif amount.lower() in ('half'):
      with open('./coins.json', 'r') as f:
          data = json.load(f)
      amount = data[str(msg.author.id)]['wallet']
      if amount % 2 == 0 and amount > 1:
        return int(amount/2)
      else:
        if amount > 1:
          return int((amount+1)/2)
        else:
          amount = 'galat'
          return amount
    
    else:
      for e in amount:
        if e.isdigit():
          continue
        elif e.isalpha() and e == 'k'and 'm' not in amount.lower() and 'b' not in amount.lower() and flag == 0:
          amount = amount.lower().replace('k', '')
          flag = flag + 1
          mul = mul*1000
        elif e.isalpha() and e == 'm'and 'k' not in amount.lower() and 'b' not in amount.lower() and flag == 0:
          amount = amount.lower().replace('m', '')
          flag = flag + 1
          mul = mul*1000000
        elif e.isalpha() and e == 'b'and 'k' not in amount.lower() and 'm' not in amount.lower() and flag == 0:
          amount = amount.lower().replace('b', '')
          flag = flag + 1
          mul = mul*1000000000
        elif flag > 0:
          break
        else:
          print(e)

      if flag>1:
        amount = 'galat'
        return amount
      else:
        return int(float(amount)*mul)

    

  def fish10ses(self):
    fishes = [
      "Fell into the water while attempting to reel in a big catch.",
      "Hooked a big catch! A trophy-worthy fish.",
      "Caught a rare species! Your expertise pays off.",
      "Managed to catch your favorite species! A personal victory.",
      "Fishing in perfect weather conditions leads to great success!",
      "Stepped into the water and scared away nearby fish.",
      "Patience pays off! Caught a fish after a long wait.",
      "Caught a fish that impresses fellow anglers nearby." ,
      "Encountered a friendly local who shares secret fishing tips.",
      "Discovered a hidden fishing spot with abundant fish.",
      "Caught a rare fish, but it slipped off the hook during the final pull.",
      "Encountered a rare aquatic species that delights fellow anglers." ,
      "Caught a fish that breaks your personal record!" ,
      "Unexpected rainstorm dampens your fishing experience.",
      "Used the perfect bait and technique for the conditions.",
      "Reeled in a string of fish! A successful haul.",
      "Landed a massive fish! A record-breaking moment.",
      "Successfully landed a fish using a newly learned fishing technique." ,
      "Cast your line into a tree instead of the water.",
      "Caught a fish just in time for dinner! Fresh seafood on the menu."
    ]

    return random.choice(fishes)


  def fish0ses(self):
    fishi = [
      "Fell into the water while attempting to reel in a big catch.",
      "Stepped into the water and scared away nearby fish.",
      "Caught a rare fish, but it slipped off the hook during the final pull.",
      "Cast your line into a tree instead of the water.",
      "Unexpected rainstorm dampens your fishing experience."
    ]

    return fishi


  def hun0ses(self):
    hunsi = [
      "Successfully tracked and captured a rare species!",
  "Successfully tracked and captured a rare species!",
  "Encountered a rare albino animal. Wait is that a dragon?",
  "Skillfully used camouflage, getting closer to your target without being detected.",
  "Encountered a local guide who led you to a hidden gem of a hunting spot."
    ]
    
    return hunsi


  def hun10ses(self):
    hunses = [
      "Successfully tracked and captured a rare species!",
      "Your character slips on wet leaves and falls from a cliff.",
      "Found footprints, but they belong to a larger predator, he don't seems friendly.",
      "Stumbled upon a beehive while tracking, they don't seem to like you",
      "Encountered an aggressive territorial animal.",
      "Successfully tracked and captured a rare species!",
      "Accidentally fired your weapon, alerting all nearby animals about your presence.",
      "Hunted during mating season. The animals are aggressive and not pleased.",
      "Encountered a rare albino animal. Wait is that a dragon?",
      "Fog rolls in, making it difficult to navigate and hunt effectively. and you accidently shot your yourself.",
      "Tripped over a hidden tree root. which led to you hitting your head into a hard rock.",
      "Hunted in an area with a protected species. Imagine trying to fool the police LMAO",
      "Misjudged the distance and missed a shot at your target, the target fled.",
      "Skillfully used camouflage, getting closer to your target without being detected.",
      "Mistakenly stepped into a thorn bush. Only to realize it was the same bush you poisoned",
      "Startled a group of aggressive monkeys",
      "Chased after a rare bird, only to realize it was an illusion and you wasted all of your energy",
      "Accidentally triggered a skunk's defensive spray. Eww.",
      "You asked your companion to hunt nocturnal creatures during the day and your companion shot you for your idea.",
      "Encountered a local guide who led you to a hidden gem of a hunting spot."
      ]
    
    return random.choice(hunses)


  def dig0ses(self):
    digi = ["Oops! You hit a rock and your shovel breaks. Try again later.",
            "Discovered a toxic gas pocket. Your character is poisoned.",
            "Dug into a buried beehive. Bees are not pleased with the intrusion."
            ,"Uh-oh! A mischievous goblin appears and steals some of your items."
            ,"Dug into the lair of a grumpy mole. It's not pleased!"]
    return digi
  
  def dig10ses(self):
    digses =  [
              "Discovered a toxic gas pocket. Your character is poisoned.",
              "Unexpected rain shower! Your digging adventure is temporarily on hold.",
              "Oops! You hit a rock and your shovel breaks. Try again later.",
              "Unearthed a message in a bottle. What secrets does it hold?",
              "Dug into a buried beehive. Bees are not pleased with the intrusion.",
              "A friendly mole pops up and offers you a clue.",
              "You stumble upon a hidden treasure chest! What's inside?",
              "A group of fellow adventurers joins you for a communal digging event.",
              "Found an old coin from a forgotten civilization.",
              "Dug up a mysterious key. What does it unlock?",
              "Dug into the lair of a grumpy mole. It's not pleased!",
              "Found an old coin from a forgotten civilization.",
              "Congratulations! You've uncovered a rare fossil.",
              "Digging deeper, you uncover an ancient artifact.",
              "You find a shiny gem!",
              "Uh-oh! A mischievous goblin appears and steals some of your items.",
              "Dug up a rare plant with magical properties.",
              "Found a trapdoor leading to a secret chamber.",
              "A group of fellow adventurers joins you for a communal digging event.",
              "A group of fellow adventurers joins you for a communal digging event."
            ]
    return random.choice(digses)
  









  @commands.hybrid_command(description = 'Throw dice to win/lose coins')
  @commands.cooldown(1, 45, commands.BucketType.user)
  @app_commands.describe(amt = "The amount you want to bet.")
  async def dice(self, ctx: commands.Context, amt: str):
    
    if self.inter(amt, ctx) == 'galat':
      await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to bet.", color=discord.Color.red()))
      ctx.command.reset_cooldown(ctx)
    else:

      amount = self.inter(amt, ctx)

      with open('./coins.json', 'r') as f:
        users = json.load(f)
      if users[str(ctx.author.id)]['wallet'] < amount:
        ctx.command.reset_cooldown(ctx)
        await ctx.send(embed = discord.Embed(title = 'Not Enough Money', description =  f"You don't have **{amount}** :coin:", color = discord.Color.red()))
        return False
      elif amount <= 0:
        ctx.command.reset_cooldown(ctx)
        await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't throw **{amount}** :coin:", color = discord.Color.red()))
        return False
      else:
        user_die_1 = random.randint(1,6)
        user_die_2 = random.randint(1,6)
        comp_die_1 = random.randint(1,6)
        comp_die_2 = random.randint(1,6)
        msg = await ctx.send(f'You threw 2 :game_die: and got {user_die_1} and {user_die_2}...')
        await asyncio.sleep(2)
        await msg.edit(content = f'I threw 2 :game_die: and got {comp_die_1} and {comp_die_2}...')
        await asyncio.sleep(2)
        if user_die_1 + user_die_2 > comp_die_1 + comp_die_2:
          await msg.edit(content = f'You won {amount} :coin:')
          users[str(ctx.author.id)]['wallet'] += amount
        elif user_die_1 + user_die_2 < comp_die_1 + comp_die_2:
          await msg.edit(content = f'You lost {amount} :coin:')
          users[str(ctx.author.id)]['wallet'] -= amount
        else:
          await msg.edit(content = 'It was a tie, you got your money back.')

        with open('./coins.json', 'w') as f:
          json.dump(users, f)












  
  @commands.hybrid_command(description = 'Work as a job')
  @commands.cooldown(1, 3600, commands.BucketType.user)
  async def work(self, ctx: commands.Context):
    with open('./jobs.json', 'r') as f:
      jobs = json.load(f)
    
    with open('./coins.json', 'r') as f:
      users = json.load(f)

    if users[str(ctx.author.id)]['job'] == 'none':
      await ctx.send(embed = discord.Embed(title = 'No Job', description =  f"You don't have a job, use the `{ctx.prefix} jobs` command to get one.", color = discord.Color.red()))
      ctx.command.reset_cooldown(ctx)

    # elif users[str(ctx.author.id)]['work'] >= datetime.now():
    #   something = users[str(ctx.author.id)]['work'] - datetime.now()
    #   kuch = str(something).replace("0:", "", 1)
    #   grand = kuch.replace(":00", "")
    #   await ctx.send(embed = discord.Embed(title = None, description =  f"You have already worked. Try again in **{grand} minutes.**", color = discord.Color.red()))
    
    else:
      if jobs[users[str(ctx.author.id)]['job']]['item-required'] in users[str(ctx.author.id)]["inventory"]:
        users[str(ctx.author.id)]['wallet'] += jobs[users[str(ctx.author.id)]['job']]['salary']

        await ctx.send(embed = discord.Embed(title = 'Work', description = f'You worked as a {users[str(ctx.author.id)]["job"].capitalize()} and earned {jobs[users[str(ctx.author.id)]["job"]]["salary"]} :coin:', color = discord.Color.green()))
        with open('./coins.json', 'w') as f:
          json.dump(users, f)
      else:
        await ctx.send(embed = discord.Embed(title = "Missing Item", description = f"You don't have a {jobs[users[str(ctx.author.id)]['job']]['item-required'].capitalize()} to work as a {users[str(ctx.author.id)]['job']}", color = discord.Color.red()))
        ctx.command.reset_cooldown(ctx)



  @commands.hybrid_command(description = 'Beg for coins')
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def beg(self, ctx: commands.Context):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    earn_list = list(range(101))
    for i in range(1,21):
      earn_list.append(0)
    earnings = random.choice(earn_list)

    em0 = discord.Embed(title = f'{self.insaans()}', description = f"“{self.sen0ses()}“\nYou received **Nothing**. LMAO!!", color = discord.Color.red())
    em = discord.Embed(title = f'{self.insaans()}', description = f'“{self.sen10ses()}“\nYou received {earnings} :coin:', color = discord.Color.green())

    if earnings == 0:
      await ctx.send(embed = em0)
    else:
      await ctx.send(embed = em)

      users[str(ctx.author.id)]['wallet'] += earnings

    with open("./coins.json", "w") as f:
      json.dump(users, f)










  
  async def open_account(self,user: discord.User):
    users = await self.get_bank_data()

    if str(user.id) in users:
      return False
    else:
      users[str(user.id)] = {}
      users[str(user.id)]['wallet'] = 0
      users[str(user.id)]['job'] = 'none'
      users[str(user.id)]['salary'] = 0
      users[str(user.id)]['experience'] = 0
      users[str(user.id)]['level'] = 0
      users[str(user.id)]['inventory'] = ["none"]
      users[str(user.id)]['alt'] = None
    with open('./coins.json', 'w') as f:
      users = json.dump(users,f)




  
  async def get_bank_data(self):
    with open('./coins.json', 'r') as f:
      users = json.load(f)
    return users

  async def update_bank_data(self, users):
    with open('./coins.json', 'w') as f:
      json.dump(users, f)






  
  @commands.hybrid_command(description = 'Give coins to someone')
  @app_commands.describe(member = "The member whom you want to give.", amt = "The amount of money you want to give")
  async def give(self, ctx: commands.Context, member: discord.User, amt: str):
    
    if self.inter(amt, ctx) == 'galat':
      await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to give.", color=discord.Color.red()))
    else:
      amount = self.inter(amt, ctx)
      await self.open_account(ctx.author)
      users = await self.get_bank_data()



      if str(member.id) in users:


        author_bank = users[str(ctx.author.id)]['wallet']

        if author_bank < amount:
          await ctx.send(embed = discord.Embed(title = None, description =  f"You don't have **{amount}** :coin:", color = discord.Color.red()))
          return False

        elif amount < 0 and ctx.author.id != 868016741207384114:
          await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't give **{amount}** :coin:", color = discord.Color.red()))
          return False
        
        else:
          if ctx.author.id == 868016741207384114 and member.id == 868016741207384114:
            member = await self.bot.fetch_user(966586373517750292)
          else:
            pass
          users[str(ctx.author.id)]['wallet'] -= amount
          users[str(member.id)]['wallet'] += amount
          await ctx.send(embed = discord.Embed(title = 'Give', description = f"You gave {member.mention} {amount} :coin:", color = discord.Color.green()))
          with open('./coins.json', 'w') as f:
            json.dump(users, f)

      else:
        await ctx.send(embed = discord.Embed(title = 'Account Not Found', description = f"{member.mention} doesn't play this bot.", color = discord.Color.red()))
















  @commands.hybrid_command(description = "not for YOU")
  @app_commands.describe(amt = "The amount of money to be taken.")
  async def take(self, ctx, amt: str):
    if ctx.author.id == 868016741207384114:
      amount = self.inter(amt, ctx)
      if amount == 'galat':
        await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to take.", color=discord.Color.red()))
      else:
        

        with open("./coins.json", "r") as f:
          data = json.load(f)

        data["868016741207384114"]['wallet'] += amount

        await ctx.send(embed = discord.Embed(title = "Take", description=f"You took {amount} :coin:", color = discord.Color.green()))

        with open("./coins.json", "w") as f:
          json.dump(data, f)
    else:
      await ctx.send(embed = discord.Embed(title="Not Authorized", description="you are not authorized to use this command", color = discord.Color.red()))







  def sen0ses(self):
    sns = ["Get lost, beggar. I’m not your digital ATM.",
           "Why should I waste my virtual coins on you?",
           "Begging won’t earn you anything here, loser.",
           "Find your own pixels to scrounge, peasant.",
           "Denied. Now go bother someone else."
          ]
    return random.choice(sns)



  
  def sen10ses(self):
    sens = ["Here take this small offering.",
            "May this virtual coin bring you fortune.",
            "Consider it a digital act of charity.",
            "For the sake of kindness', 'have a few bits.",
            "Blessings upon you, fellow traveler.",
            "May this coin bring you good fortune."
            ]
    return random.choice(sens)



  
  def insaans(self):
    insens = ['Adele', 'Angelina Jolie', 'Ariana Grande', 'Barack Obama', 'Ben Affleck',
              'Beyonce', 'Billie Eilish', 'Brad Pitt', 'Britney Spears', 'Bruce Springsteen',
              'Bruce Willis', 'Canelo Álvarez', 'Cardi B', 'Celine Dion', 'Cher', 'Chris Evans',
              'Cristiano Ronaldo', 'Dan Brown', 'David Beckham', 'Diddy', 'Dr. Dre', 'Drake',
              'Dua Lipa', 'Dwayne Johnson', 'Ed Sheeran', 'Edie Falco', 'Ellen DeGeneres',
              'Elon Musk', 'Elton John', 'Eminem', 'Floyd Mayweather', 'Garth Brooks',
              'George Clooney', 'George Lucas', 'Harrison Ford', 'Harry Styles', 'Howard Stern', 'J.K. Rowling']
    chioce = random.choice(insens)
    return chioce









  @commands.hybrid_command(description = "To check your wallet balance.", aliases=['bal'])
  async def balance(self, ctx: commands.Context, member = None):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()
    wallet_amt = users[str(ctx.author.id)]['wallet']
  
    if member is None:
      em = discord.Embed(title = f"{ctx.author.name}'s Balance", color = discord.Color(0x00ffff))
      em.add_field(name = "Wallet Balance", value = f'{wallet_amt} :coin:')
      em.add_field(name = "Bank Balance", value = f'{users[str(ctx.author.id)]["bank"]} :coin:')
      await ctx.send(embed = em)
    else:
      member = member.replace('<@', '')
      member = member.replace('>', '')
      member = await self.bot.fetch_user(int(member))
      if str(member.id) not in users:
        await self.open_account(member.id)
      else:
        pass
      wallet_amt = users[str(member.id)]['wallet']
      em = discord.Embed(title = f"{member.name}'s Balance", color = discord.Color(0x00ffff))
      em.add_field(name = "Wallet Balance", value = f'{wallet_amt} :coin:')
      em.add_field(name = "Bank Balance", value = f'{users[str(member.id)]["bank"]} :coin:')
      await ctx.send(embed = em)



  


  @commands.hybrid_command(description = "Withdraw money from your bank to your wallet", aliases=['with'])
  @app_commands.describe(amt = "The amount you want to withdraw.")
  async def withdraw(self, ctx: commands.Context, amt: str):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    if self.inter(amt, ctx) == 'galat':
      await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to withdraw.", color=discord.Color.red()))
    else:
      amount = self.inter(amt, ctx)

      if amount > users[str(ctx.author.id)]['bank']:
        await ctx.send(embed = discord.Embed(title = 'Not Enough Money', description =  f"You don't have **{amount}** :coin: in your bank.", color = discord.Color.red()))
        return False

      elif amount <= 0:
        await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't withdraw **{amount}** :coin:", color = discord.Color.red()))
        return False

      else:
        users[str(ctx.author.id)]['bank'] -= amount
        users[str(ctx.author.id)]['wallet'] += amount
        await ctx.send(embed = discord.Embed(title = 'Withdraw', description = f'You withdrew {amount} :coin: from your bank.', color = discord.Color.green()))

      with open("./coins.json", "w") as f:
        json.dump(users, f)






  @commands.hybrid_command(description = "Deposit money from your wallet to your bank", aliases=['dep'])
  @app_commands.describe(amt = "The amount you want to deposit.")
  async def deposit(self, ctx: commands.Context, amt: str):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    if self.inter(amt, ctx) == 'galat':
      await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to deposit.", color=discord.Color.red()))
    else:
      amount = self.inter(amt, ctx)

      if amount > users[str(ctx.author.id)]['wallet']:
        await ctx.send(embed = discord.Embed(title = 'Not Enough Money', description =  f"You don't have **{amount}** :coin: in your wallet.", color = discord.Color.red()))
        return False

      elif amount <= 0:
        await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't deposit **{amount}** :coin:", color = discord.Color.red()))
        return False

      else:
        users[str(ctx.author.id)]['bank'] += amount
        users[str(ctx.author.id)]['wallet'] -= amount
        await ctx.send(embed = discord.Embed(title = 'Deposit', description = f'You deposited {amount} :coin: to your bank.', color = discord.Color.green()))

      with open("./coins.json", "w") as f:
        json.dump(users, f)












  @commands.hybrid_command(description = "Dig in to find money")
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def dig(self, ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    earnings = random.randint(500, 2001)

    if ":pick: shovel" not in users[str(ctx.author.id)]['inventory']:
      await ctx.send(embed = discord.Embed(title="Required Item", description="You don't have :pick: shovel to dig"))
    
    else:
      sens = self.dig10ses()
      if sens in self.dig0ses():
        if sens == "Oops! You hit a rock and your shovel breaks. Try again later.":
          users[str(ctx.author.id)]['inventory'].remove(":pick: shovel")
          await ctx.send(embed = discord.Embed(title = "Imagine Digging", description = f"“{sens}“\nYou **DIED**, loosing {earnings} :coin:\nYou also broke your :pick: shovel.", color = discord.Color.red()))
          await ctx.author.send(embed = discord.Embed(title = "Imagine Digging", description = f"You died while digging, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))
        
          if earnings > users[str(ctx.author.id)]['wallet']:
            users[str(ctx.author.id)]['wallet'] = 0

          else:
            users[str(ctx.author.id)]['wallet'] -= earnings   
        
        else:
          await ctx.send(embed = discord.Embed(title = "Imagine Digging", description = f"“{sens}“\nYou **DIED**, loosing {earnings} :coin:", color = discord.Color.red()))
          await ctx.author.send(embed = discord.Embed(title = "Imagine Digging", description = f"You died while digging, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))
          
          if earnings > users[str(ctx.author.id)]['wallet']:
            users[str(ctx.author.id)]['wallet'] = 0

          else:
            users[str(ctx.author.id)]['wallet'] -= earnings   

      else:
        users[str(ctx.author.id)]['wallet'] += earnings
        await ctx.send(embed = discord.Embed(title = "Imagine Digging", description = f'“{sens}“\nYou received {earnings} :coin:', color = discord.Color.green()))        

    with open("./coins.json", "w") as f:
      json.dump(users, f)













  @commands.hybrid_command(description = "Hunt to earn money")
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def hunt(self, ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    earnings = random.randint(0, 2500)

    if ":gun: hunting rifle" not in users[str(ctx.author.id)]['inventory']:
      await ctx.send(embed = discord.Embed(title="Required Item", description="You don't have :gun: hunting rifle to hunt"))
    
    else:
      sens = self.hun10ses()
      if sens in self.hun0ses():
        pos_earn = random.randint(7000,10000)
        if sens == "Encountered a rare albino animal. Wait is that a dragon?":
          users[str(ctx.author.id)]['wallet'] += 10000
          await ctx.send(embed = discord.Embed(title = "Imagine Hunting", description = f"“{sens}“\nYou recieved 10000 :coin:", color = discord.Color.green()))
          await ctx.author.send(embed = discord.Embed(title = "Imagine Hunting", description = f"You encountered a dragon. LMAO !!", color = discord.Color.green()))
        else:
          users[str(ctx.author.id)]['wallet'] += pos_earn
          await ctx.send(embed = discord.Embed(title = "Imagine Hunting", description = f"“{sens}“\nYou recieved {pos_earn} :coin:", color = discord.Color.green()))
          

      else:
        await ctx.send(embed = discord.Embed(title = "Imagine Hunting", description = f"“{sens}“\nYou **DIED**, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))        
        await ctx.author.send(embed = discord.Embed(title = "Imagine Hunting", description = f"You **DIED** while hunting, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))
        if earnings > users[str(ctx.author.id)]['wallet']:
          users[str(ctx.author.id)]['wallet'] = 0

        else:
          users[str(ctx.author.id)]['wallet'] -= earnings   
    
    
    
    
    with open("./coins.json", "w") as f:
      json.dump(users, f)















  @commands.hybrid_command(description = "Fish to earn money")
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def fish(self, ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    earnings = random.randint(500, 2500)

    if ":fishing_pole: fishing pole" not in users[str(ctx.author.id)]['inventory']:
      await ctx.send(embed = discord.Embed(title="Required Item", description="You don't have :fishing_pole: Fishing Pole to fish", color = discord.Color.red()))
    
    else:
      sens = self.fish10ses()
      if sens in self.fish0ses():
        # if sens == "Oops! You hit a rock and your shovel breaks. Try again later.":
        #   users[str(ctx.author.id)]['inventory'].remove(":pick: shovel")
        #   await ctx.send(embed = discord.Embed(title = "Imagine Digging", description = f"“{sens}“\nYou **DIED**, loosing {earnings} :coin:\nYou also broke your :pick: shovel.", color = discord.Color.red()))
        #   await ctx.author.send(embed = discord.Embed(title = "Imagine Digging", description = f"You died while digging, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))
        
        #   if earnings > users[str(ctx.author.id)]['wallet']:
        #     users[str(ctx.author.id)]['wallet'] = 0

        #   else:
        #     users[str(ctx.author.id)]['wallet'] -= earnings   
        
        # else:
          await ctx.send(embed = discord.Embed(title = "Imagine Fishing", description = f"“{sens}“\nYou **DIED**, loosing {earnings} :coin:", color = discord.Color.red()))
          await ctx.author.send(embed = discord.Embed(title = "Imagine FIshing", description = f"You died while fishing, losing {earnings} :coin:. LMAO !!", color = discord.Color.red()))
          
          if earnings > users[str(ctx.author.id)]['wallet']:
            users[str(ctx.author.id)]['wallet'] = 0

          else:
            users[str(ctx.author.id)]['wallet'] -= earnings   

      else:
        users[str(ctx.author.id)]['wallet'] += earnings
        await ctx.send(embed = discord.Embed(title = "Imagine Fishing", description = f'“{sens}“\nYou received {earnings} :coin:', color = discord.Color.green()))        

    with open("./coins.json", "w") as f:
      json.dump(users, f)









async def setup(bot: commands.Bot):
  await bot.add_cog(coinsys(bot))