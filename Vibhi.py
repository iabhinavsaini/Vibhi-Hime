import discord
from discord.ext import commands
import os
from decouple import config


print("---> BOT is waking up\n")

bot = commands.Bot(command_prefix=config('BOT_PREFIX'),case_insensitive=True)
bot.remove_command('help')

def load_cogs():
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    print(f'---> Logged in as : {bot.user.name} , ID : {bot.user.id}')
    print(f'---> Total Servers : {len(bot.guilds)}\n')
    activity = discord.Game(name='vibhi',type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    load_cogs()
    print('\n---> BOT is awake\n')
    
    
bot.run(config('BOT_TOKEN'))
