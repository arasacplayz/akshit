import discord
from discord.ext import commands

class ErrorCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot

 
  @commands.Cog.listener()
  async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
      ctx.command.reset_cooldown(ctx)
      return await ctx.send(embed = discord.Embed(description = f'You missed the `{error.param.name}` argument.\n\nDo it like: `{ctx.prefix}{ctx.command.qualified_name} {ctx.command.signature}`', color = discord.Color.red()))

    elif isinstance(error, commands.CommandNotFound):
      return await ctx.send(embed = discord.Embed(description = 'Command not found', color = discord.Color.red()))

    elif isinstance(error, commands.MissingPermissions):
      perms = ''
      for perm in error.missing_permissions:
        perms += f'{perm}, '
      return await ctx.send(embed = discord.Embed(description = f'You need {perms} to use this command', color = discord.Color.red()))

    elif isinstance(error, commands.BotMissingPermissions):
      return await ctx.send(embed = discord.Embed(description = "I dont have permissions to do so.", color = discord.Color.red()))

    elif isinstance(error, commands.BadArgument):
      ctx.command.reset_cooldown(ctx)
      return await ctx.send(embed = discord.Embed(description = f'You entered a wrong argument. \n\nThe command works like: `{ctx.prefix}{ctx.command.qualified_name} {ctx.command.signature}`', color = discord.Color.red()))

    elif isinstance(error, commands.CommandOnCooldown):
      if ctx.command.qualified_name == 'work' or ctx.command.qualified_name == 'worky':
        await ctx.send(embed = discord.Embed(title = None, description =  f"You have already worked. Try again in **{error.retry_after//60} minutes and {round(error.retry_after%60,0)} seconds**", color = discord.Color.red()))
      else:
        return await ctx.send(embed = discord.Embed(description = f"You are on cooldown. Try again in {str(round(error.retry_after, 0)).replace('.0', '')} seconds", color = discord.Color.red()))


    else:
      raise error

async def setup(bot: commands.Bot):
  await bot.add_cog(ErrorCog(bot))