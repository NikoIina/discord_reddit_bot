import discord
from discord.ext import commands
from config import bot_config, reddit_config
from reddit import *

bot = commands.Bot(command_prefix=bot_config['prefix'])

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.content.startswith('-'):
        parts = message.content.split(' ')
        if parts[0] == '-top':
            text = await get_top(message, parts)
            for i in text:
                await message.channel.send(i)
        if parts[0] == '-hot':
            text = await get_hot(message, parts)
            for i in text:
                await message.channel.send(i)
        if parts[0] == '-new':
            text = await get_new(message, parts)
            for i in text:
                await message.channel.send(i)
        if parts[0] == '-help':
            await message.channel.send('Ask for reddit posts with -new/-top/-hot directory name number of posts. '
                                       'If you want to read specific post from those I sent you, send me a number')
    else:
        try:
            int(message.content)
            text = await get_body(message)
            if not text:
                await message.channel.send('This is it, that is the post!')
            else:
                await message.channel.send(text)
        except:
            if message.content == 'Try asking for help with -help':
                pass
            elif message.content == 'Ask for reddit posts with -new/-top/-hot directory name number of posts. ' \
                                  'If you want to read specific post from those I sent you, send me a number':
                pass
            else:
                await message.channel.send('Try asking for help with -help')


bot.run(bot_config['token'])