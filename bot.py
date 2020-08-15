import discord
import os
from discord.ext import commands

#initiate bot
bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Pornhub'))
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome')
    await channel.send(f'Welcome {member.mention} to {member.guild.name}')

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='welcome')
    await channel.send(f'{member.mention} left the server')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

bot.run(token)



