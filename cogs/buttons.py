import discord
from discord.ext import commands
from discord.ui import Button, View
import random
import json
from discord import app_commands
import asyncio


class RPSCog(commands.Cog):
    def __init__(self, bot):
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


    class RPSButton(Button):
        def __init__(self, label, custom_id, user_id,  amount, style):
            super().__init__(label=label, custom_id=custom_id, style=style)
            self.user_id = user_id
            self.amount = amount
            # self.user2_id = user2_id
      
        async def get_bank_data(self):
          with open('./coins.json', 'r') as f:
            users = json.load(f)
          return users

        async def update_bank_data(self, users):
          with open('./coins.json', 'w') as f:
            json.dump(users, f)

        async def convert(self, choice):
            if choice.lower() == 'rock':
               return "✊"
            elif choice.lower() == 'paper':
               return "✋"
            elif choice.lower() == 'scissors':
               return "✌"
            else:
               return False    

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != self.user_id :
                await interaction.response.send_message(embed = discord.Embed(title = "Not For You", description = "These buttons are not for you!", color = discord.Color.red()), ephemeral=True)
                return
            
        
            else:
              user_choice = self.custom_id
              bot_choice = random.choice(["Rock", "Paper", "Scissors"])
              data = await self.get_bank_data()

              if user_choice.lower() == bot_choice.lower():
                await interaction.response.send_message(embed = discord.Embed(title = 'Result', description = f"You chose {await self.convert(user_choice)}, I chose {await self.convert(bot_choice)}. \nIt was a tie"))
              
              elif (user_choice.lower() == "rock" and bot_choice.lower() == "scissors") or \
                  (user_choice.lower() == "scissors" and bot_choice.lower() == "paper") or \
                  (user_choice.lower() == "paper" and bot_choice.lower() == "rock"):
                data[str(interaction.user.id)]['wallet'] += self.amount
                await interaction.response.send_message(embed = discord.Embed(title = 'Result', description = f"You chose {await self.convert(user_choice)}, I chose {await self.convert(bot_choice)}. \nYou won {self.amount} :coin:", color = discord.Color.green()))
              
              else:
                data[str(interaction.user.id)]['wallet'] -= self.amount
                await interaction.response.send_message(embed = discord.Embed(title = 'Result', description = f"You chose {await self.convert(user_choice)}, I chose {await self.convert(bot_choice)}. \nYou lost {self.amount} :coin:", color = discord.Color.red()))
              await self.update_bank_data(data)        


    @commands.hybrid_command(description = "Rock Paper Scissors.... Shoot!!!")
    @commands.cooldown(1, 30, commands.BucketType.user)
    @app_commands.describe(amt = "The amount you want to bet.")
    async def rps(self, ctx, amt: str):
        user_id = ctx.author.id
        amount = self.inter(amt, ctx)
        with open('./coins.json', 'r') as f:
            data = json.load(f)

        if amount == 'galat':
          await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to bet.", color=discord.Color.red()))
          ctx.command.reset_cooldown(ctx)
        
        elif amount > data[str(user_id)]['wallet']:
          ctx.command.reset_cooldown(ctx)
          await ctx.send(embed = discord.Embed(title = 'Not Enough Money', description =  f"You don't have **{amount}** :coin:", color = discord.Color.red()))
          return False
        elif amount <= 0:
          ctx.command.reset_cooldown(ctx)
          await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't throw **{amount}** :coin:", color = discord.Color.red()))
          return False
        else:
          view = View()
          view.add_item(self.RPSButton(label="✊", custom_id="rock", user_id=user_id, amount = amount, style = discord.ButtonStyle.red))
          view.add_item(self.RPSButton(label="✋", custom_id="paper", user_id=user_id, amount = amount, style = discord.ButtonStyle.green))
          view.add_item(self.RPSButton(label="✌", custom_id="scissors", user_id=user_id, amount = amount, style = discord.ButtonStyle.blurple))

          await ctx.send("Choose your move!", view=view)

    # @commands.hybrid_command(description = 'Challenge your friends')
    # @app_commands.describe(user = "The user you want to challenge", amt = "The amount you want to bet.")
    # async def challenge(self, ctx, user: discord.User, amt: str):



    class workButton(Button):
        def __init__(self, label, num, user_id, style, sumyy, msg_id):
            super().__init__(label=label, style=style)
            self.user_id = user_id
            self.num = num
            self.sum = sumyy
            self.msg_id = msg_id
        async def get_bank_data(self):
          with open('./coins.json', 'r') as f:
            users = json.load(f)
          return users

        async def update_bank_data(self, users):
          with open('./coins.json', 'w') as f:
            json.dump(users, f)

        async def callback(self, interaction: discord.Interaction):
            if interaction.user.id != self.user_id :
                await interaction.response.send_message(embed = discord.Embed(title = "Not For You", description = "These buttons are not for you!", color = discord.Color.red()), ephemeral=True)
                return
            
        
  
            else:
              msg = await interaction.channel.fetch_message(self.msg_id)
              await msg.edit(view=None)

              if self.num == self.sum:
                 data = await self.get_bank_data()
                 data[str(self.user_id)]['wallet'] += data[str(self.user_id)]['salary']
                 await msg.edit(embed = discord.Embed(title = 'Success', description = f"You worked and earned {data[str(self.user_id)]['salary']} :coin:", color = discord.Color.green()))
                 await self.update_bank_data(data)
              else:
                  await msg.edit(embed = discord.Embed(title = 'Failed', description = f"You worked but got caught by the boss and earned nothing!", color = discord.Color.red()))

  
      

    @commands.hybrid_command(description = "Work to earn coins")
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def worky(self, ctx):
        user_id = ctx.author.id
        num1 = random.randint(0,100)
        num2 = random.randint(0,100)
        num3 = random.randint(0,100)
        num4 = random.randint(0,100)
        sumy = num1 + num2
        summ = sumy
        choices= [num3, num4, sumy]
        random.shuffle(choices)
        num3 = choices[0]
        num4 = choices[1]
        sumy = choices[2]
        response = await ctx.send(embed = discord.Embed(title = 'Click on the correct answer', description = f"what is {num1} + {num2}", color = discord.Color.blue()))
        view = View()
        view.add_item(self.workButton(label=num3, num = num3, user_id=user_id, style = discord.ButtonStyle.green, sumyy = summ, msg_id = response.id))
        view.add_item(self.workButton(label=num4, num = num4, user_id=user_id, style = discord.ButtonStyle.green, sumyy = summ, msg_id = response.id))
        view.add_item(self.workButton(label=sumy, num = sumy, user_id=user_id, style = discord.ButtonStyle.green, sumyy = summ, msg_id = response.id))
        await response.edit(view=view)
        

    class DICEGUESS(Button):
       def __init__(self, label, user_id, style, amount):
            super().__init__(label=label, style=style)
            self.user_id = user_id           
            self.amount = amount
       async def get_bank_data(self):
          with open('./coins.json', 'r') as f:
            users = json.load(f)
          return users
       async def update_bank_data(self, users):
          with open('./coins.json', 'w') as f:
            json.dump(users, f)

       async def callback(self, interaction: discord.Interaction):
          

            if interaction.user.id != self.user_id :
                await interaction.response.send_message(embed = discord.Embed(title = "Not For You", description = "These buttons are not for you!", color = discord.Color.red()), ephemeral=True)
                return
            
  
            else:
              dice_roll = random.randint(1, 6)
              guess = int(self.label)
              data = await self.get_bank_data()

              await interaction.response.send_message(embed = discord.Embed(description = f"You guessed {guess}, Rolling the :game_die: ....."))
              msg = await interaction.original_response()
              await asyncio.sleep(2)
              await msg.edit(embed = discord.Embed(description = f"You guessed {guess}, The :game_die: rolled {dice_roll}."))
              await asyncio.sleep(2)

              if guess == dice_roll:
                data[str(interaction.user.id)]['wallet'] += self.amount*5
                await msg.edit(embed = discord.Embed(title = 'Result', description = f"You won {self.amount*5} :coin:", color = discord.Color.green()))
              
              else:
                data[str(interaction.user.id)]['wallet'] -= self.amount
                await msg.edit(embed = discord.Embed(title = 'Result', description = f"You lost {self.amount} :coin:", color = discord.Color.red()))
              await self.update_bank_data(data)


    @commands.hybrid_command(description = "Guess the dice number (1-6)")
    @commands.cooldown(1, 30, commands.BucketType.user)
    @app_commands.describe(amt = "The amount you want to bet.")
    async def guess(self, ctx, amt: str):
        user_id = ctx.author.id
        amount = self.inter(amt, ctx)
        with open('./coins.json', 'r') as f:
            data = json.load(f)

        if amount == 'galat':
          await ctx.send(embed = discord.Embed(title="Invalid Input", description="Please enter a valid amount to bet.", color=discord.Color.red()))
          ctx.command.reset_cooldown(ctx)
        
        elif amount > data[str(user_id)]['wallet']:
          ctx.command.reset_cooldown(ctx)
          await ctx.send(embed = discord.Embed(title = 'Not Enough Money', description =  f"You don't have **{amount}** :coin:", color = discord.Color.red()))
          return False
        elif amount <= 0:
          ctx.command.reset_cooldown(ctx)
          await ctx.send(embed = discord.Embed(title = 'Duh', description = f"You can't throw **{amount}** :coin:", color = discord.Color.red()))
          return False
        else:
          view = View()
          view.add_item(self.DICEGUESS(label="1", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))
          view.add_item(self.DICEGUESS(label="2", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))
          view.add_item(self.DICEGUESS(label="3", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))
          view.add_item(self.DICEGUESS(label="4", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))
          view.add_item(self.DICEGUESS(label="5", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))
          view.add_item(self.DICEGUESS(label="6", user_id=user_id, style = discord.ButtonStyle.grey, amount = amount))

          await ctx.send(embed = discord.Embed(title = "Guess the number", description = "Guss what the :game_die: will roll!!"),view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(RPSCog(bot))


















