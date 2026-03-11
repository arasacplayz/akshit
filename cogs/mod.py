import asyncio
import discord
from discord.ext import commands
from datetime import timedelta
from discord import app_commands
from discord import Embed
from discord.ext.commands import has_permissions


class Mod(commands.Cog):

  def __init__(self, bot: commands.Bot):
    self.bot = bot


  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  @app_commands.describe(member = "Member to kick", reason = "Reason to kick")
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    if ctx.guild.me.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "My role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    elif ctx.author.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "Your role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    else:
      try:
        if reason is None:
          reason = "Not reason provided."
        else:
          pass
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(
            title="KICK",
            description=
            f"{member.mention} has been kicked.\n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author.mention}",
            color=discord.Color.green()))
      except:
        await ctx.send(embed=discord.Embed(
            description="I Don't have enough permissions to kick this member.",
            color=discord.Color.red()))






  @commands.hybrid_command(name = 'id', description = "Get a user's ID", aliases = ['userid'])
  @app_commands.describe(user = "User to get ID of")
  async def id(self, ctx, user: discord.User = None):
    if user is None:
      user = ctx.author
    await ctx.send(embed = discord.Embed(title = f"{user}'s ID", description = f"{user.id}", color = discord.Color(0x00ffff)))









  @commands.hybrid_command(description='Bans a member')
  @commands.has_permissions(ban_members=True)
  @app_commands.describe(member = "Member to ban", reason = "Reason to ban")
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    if ctx.guild.me.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "My role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    elif ctx.author.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "Your role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    else:
      try:
        await member.ban(reason=reason)
        if reason is None:
          reason = "Not reason provided."
        else:
          pass
        await ctx.send(embed=discord.Embed(
            title='BAN',
            description=
            f'{member.mention} has been banned.\n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author.mention}',
            color=discord.Color.green()))
      except:
        await ctx.send(embed=discord.Embed(
            description="I do not have enough permissions to kick this member.",
            color=discord.Color.green()))









  @commands.hybrid_command(description='Unbans a member')
  @commands.has_permissions(ban_members=True)
  @app_commands.describe(user = "Member to unban", reason = "Reason to unban")
  async def unban(self, ctx, user: discord.User, *, reason=None):
    await ctx.guild.unban(user, reason=reason)
    if reason is None:
      reason = "Not reason provided."
    else:
      pass
    await ctx.send(embed=discord.Embed(
        description=
        f'Unbanned {user.mention}.\n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author.mention}',
        color=discord.Color.green()))




  @commands.hybrid_command(description='Timeout a member', aliases = ['tm'])
  @commands.has_permissions(moderate_members=True)
  @app_commands.describe(member = "Member to timeout", reason = "Reason to timeout")
  async def timeout(self,
                    ctx,
                    member: discord.Member,
                    str_minutes: str,
                    *,
                    reason=None):
    if ctx.guild.me.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "My role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    elif ctx.author.top_role <= member.top_role:
      await ctx.send(embed=discord.Embed(
          description=
          "Your role isn't high enough in the role hierarchy to moderate this member.",
          color=discord.Color.red()))
    else:
      try:
        if str_minutes.isdigit():
          minutes = int(str_minutes)
          delta = timedelta(minutes=minutes)
          await member.timeout(delta, reason=reason)
          if reason is None:
            reason = "No reason provided."
          else:
            pass
          await ctx.send(embed=discord.Embed(
              title='TIMEOUT',
              description=
              f'{member.mention} has been timed out.\n**Time:** {minutes} minutes.\n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author.mention}',
              color=discord.Color.green()))
        else:
          await ctx.send(embed=discord.Embed(
              description="Please only enter number of minutes",
              color=discord.Color.red()))

      except:
        await ctx.send(embed=discord.Embed(
            description="I do not have enough permissions to kick this member.",
            color=discord.Color.red()))





  @commands.hybrid_command(description='Clears messages')
  @commands.has_permissions(manage_messages=True)
  @app_commands.describe(number = "Number of messages to clear")
  async def clear(self, ctx, number: int):
    await ctx.channel.purge(limit=number + 1)
    await ctx.send(f'Cleared {number} past messages')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)




  @commands.hybrid_command(name='dm', description='Dm someone')
  @app_commands.describe(user='User to dm', message='Message to send')
  async def dm(self, ctx, user: discord.User, *, message: str):
    if ctx.author.id == 868016741207384114:
      await user.send(embed=discord.Embed(title = "Message", description = f"{message}", color = discord.Color(0x00ffff)))
      await ctx.send(
          embed=discord.Embed(description=f"Sent a DM to {user.mention}",
                              color=discord.Color.green()))
    else:
      await ctx.send(embed=discord.Embed(
          description="You are not authorized to use this command.",
          color=discord.Color.red()))
      



  @commands.hybrid_command(name = 'ids', description = "Everyones user ids.")
  async def UserID(self, ctx):
    if ctx.author.id in (810724561850859520, 868016741207384114, 885361344440844338):
      await ctx.send(embed = discord.Embed(title = "Important ID's", 
                                     description = '- **Me:** 868016741207384114 \n- **Arnav:** 810724561850859520 \n- **Bot:** 947831182157053972 \n- **Raghav:** 885361344440844338 \n- **Jummy:** 898197677756547102 \n- **Jimmy:** 1115693354076864634 \n- **Darshi:** 583249593186123788 \n- **Alt:** 966586373517750292 \n- **Motu:** 939439082612871218 ', 
                                     color = discord.Color(0x00ffff)))
    else:
      await ctx.send(embed = discord.Embed(title = 'Mod Only', description =  "You are not authorized to use this command", color = discord.Color.red()))
 


  @commands.hybrid_command(description='U cannot use this')
  async def reset(self, ctx, cmnd):
    if ctx.author.id == 868016741207384114:
      await ctx.command.reset_cooldown(cmnd)
      await ctx.reply(embed = discord.Embed(title = 'Reset', description = f"Cooldown of command `{ctx.prefix}{cmnd}` has been reset", color = discord.Color.green()))
    else:
      await ctx.reply(embed = discord.Embed(title = 'Missing Perms', description = "You are not authorized to use this command", color = discord.Color.red()))
        


  @commands.hybrid_command(name = "suggestion", description = 'Any changes u want in this bot', aliases = ['sugs'])
  async def segs(self, ctx, *, msg: str):
    channel = self.bot.get_channel(int(1256167205318692955))
    await ctx.send(embed = discord.Embed(
      title = 'Suggestion Notes',
      description = 'Thanks for you suggestion. \nWe will surely work on it.',
      color = discord.Color(0x00ffff)
    ))
    await channel.send(embed = discord.Embed(
      title = f'From {ctx.author}({ctx.author.id})',
      description = msg,
      color = discord.Color(0x00ffff)
    ))



async def setup(bot: commands.Bot):
  await bot.add_cog(Mod(bot))
