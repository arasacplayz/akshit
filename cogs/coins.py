import discord
from discord.ext import commands
import json
import random
import asyncio
from discord import app_commands

class CoinSys(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

  
  

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
      users[str(user.id)]['bank'] = 0
      users[str(user.id)]['inventory'] = ["none"]
    with open('./coins.json', 'w') as f:
      users = json.dump(users,f)




  async def get_bank_data(self):
    with open('./coins.json', 'r') as f:
      users = json.load(f)
    return users




  
  @commands.hybrid_command(description = 'Shows the leaderboard', aliases = ['lb', 'rich'])
  async def leaderboard(self, ctx: commands.Context):
    users = await self.get_bank_data()
    lb = {}
    for a in users:
      Name = int(a)
      amount = users[a]['wallet']
      lb[Name] = amount

    slb = dict(sorted(lb.items(), key=lambda item: item[1], reverse=True))

    em = discord.Embed(title = f'Top {len(slb)} Richest People', description = 'The richest users across all servers', color = discord.Color(0x00ffff))
    index = 1
    for id in slb:
      amt = slb[id]
      member = self.bot.get_user(id)
      name = member.name
      em.add_field(name = f'{index}. {name}', value = f'{amt} :coin:', inline = False)
      if index == 20:
        break
      else:
        index += 1
    await ctx.send(embed = em)
  
  

  @commands.hybrid_command(description = 'List of jobs')
  async def jobs(self, ctx: commands.Context):
    with open("./jobs.json", 'r') as f:
      jobs = json.load(f)
    em = discord.Embed(title = 'Jobs', description = 'List of jobs', color = discord.Color(0x00ffff))
    for job in jobs:
      em.add_field(name = f'{job.capitalize()}', value = f'**Salary:** {jobs[job]["salary"]} :coin:\n**Description:** {jobs[job]["description"]}\n**Level Required:** {jobs[job]["level-required"]}\n**Item Required:** {jobs[job]['item-required']}')
    await ctx.send(embed = em)



  
  @commands.hybrid_command(description = 'Apply for job')
  @app_commands.describe(job = "The job for which You want to apply.")
  async def apply(self, ctx: commands.Context,* , job: str):
    with open("./jobs.json", 'r') as f:
      jobs = json.load(f)

    with open("./coins.json", 'r') as f:
      users = json.load(f)

    if str(ctx.author.id) not in users:
      await ctx.send(embed = discord.Embed(title = None, description =  f"You don't have a wallet, use the `{ctx.prefix} balance` command to get one.", color = discord.Color.red()))
      return False
    if job.lower() not in jobs:
      await ctx.send(embed = discord.Embed(title = 'Invalid Job', description =  f"That job doesn't exist.\n use the `{ctx.prefix} jobs", color = discord.Color.red()))
      return False

    else:
      if users[str(ctx.author.id)]['level'] >= jobs[job.lower()]['level-required']:
        if jobs[job.lower()]['item-required'] in users[str(ctx.author.id)]['inventory']:
          users[str(ctx.author.id)]['job'] = job.lower()
          users[str(ctx.author.id)]['salary'] = jobs[job.lower()]['salary']
          await ctx.send(embed = discord.Embed(title = 'Job Applied', description = f'You are now working as a {job.capitalize()}.', color = discord.Color.green()))
        else:
          await ctx.send(embed = discord.Embed(title = "Item Required", description = f"You need to have {jobs[job.lower()]['item-required']} to work as a {job.capitalize()}", color = discord.Color.red()))
      else:
        await ctx.send(embed = discord.Embed(title = 'Level Required', description = f'You need to be level {jobs[job.lower()]["level-required"]} to work as a {job.capitalize()}.', color = discord.Color.red()))
      
    with open('./coins.json', 'w') as f:
      json.dump(users, f)
  
      





  @commands.hybrid_command(description = 'Market for buying things', aliases = ['shop'])
  async def market(self, ctx):
    with open("./market.json", 'r') as f:
      items = json.load(f)
    em = discord.Embed(title = 'Market', description = 'List of Items', color = discord.Color(0x00ffff))
    for item in items:
      em.add_field(name = f'{items[item]['emoji']} {item.capitalize()}', value = f'**Price:** {items[item]["price"]} :coin:\n**Description:** {items[item]["description"]}')
    em.set_footer(text = f"You can buy items from {ctx.prefix} buy command")
    await ctx.send(embed = em)







  @commands.hybrid_command(description = "To buy items from the market")
  @app_commands.describe(item = "The item you want to buy.")
  async def buy(self, ctx,num: int,* , item: str):
    with open("./coins.json", "r") as f:
      users = json.load(f)

    with open("./market.json", "r") as f:
      items = json.load(f)
    
    if item.lower() not in items:
      await ctx.send(embed = discord.Embed(title = "Item not Found!", description = f"The item {item} don't exist.", color = discord.Color.red()))

    elif users[str(ctx.author.id)]['wallet'] < items[item.lower()]["price"]:
      await ctx.send(embed = discord.Embed(title = "Duh", description=f"You dont have {items[item.lower()]["price"]} :coin: to buy this item.", color= discord.Color.red()))

    else:
      for i in range(0, num):
        users[str(ctx.author.id)]["inventory"].append(f"{items[item.lower()]['emoji']} {item.lower()}")
        users[str(ctx.author.id)]['wallet'] -= items[item.lower()]["price"]
      await ctx.send(embed = discord.Embed(title = "Sucess", description = f"You bought a `{num}x` {items[item.lower()]['emoji']} {item} for {int(items[item.lower()]["price"])*num} :coin:", color = discord.Color.green()))
        

      with open('./coins.json', 'w') as f:
        json.dump(users, f)









  @commands.hybrid_command(description = "Shows your inventory", aliases = ['inv', 'bag'])
  async def inventory(self, ctx):
    with open('./coins.json', 'r') as f:
      data = json.load(f)
    
    inv = data[str(ctx.author.id)]["inventory"].copy()

    em = discord.Embed(title = f"{ctx.author.name}'s inventory", description = "List of items.", color = discord.Color(0x00ffff))
    if data[str(ctx.author.id)]['inventory'][0] == "none" and len(data[str(ctx.author.id)]["inventory"]) == 1:
      await ctx.send(embed = discord.Embed(title=f"{ctx.author.name}'s Inventory", description="You own nothing!!. **LMAO!!**", color = discord.Color.red()))
    else:
      for item in inv:
        if item == "none":
          pass
        elif inv.count(item) > 1:
          for i in range(1, inv.count(item)):
            inv.remove(item)
          em.add_field(name=f"`{data[str(ctx.author.id)]["inventory"].count(item)}x` {item}", value="", inline=False)
        else:
          em.add_field(name=f"`{data[str(ctx.author.id)]["inventory"].count(item)}x` {item}", value="", inline=False)
      await ctx.send(embed = em)




    


async def setup(bot: commands.Bot):
  await bot.add_cog(CoinSys(bot))
