# Main module --> discord API
import discord

# For random choices ( dice, coin, etc )
import random

''' It is strongly recommended that the logging module is configured, 
as no errors or warnings will be output if it is not set up. '''
import logging

# import global var with the bot token
from authtoken import *

# log config section
# ------------------------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ------------------------------------------------------------------------------------------

# instantianting the client --> our connection to discord.
client = discord.Client()

@client.event
async def on_ready():
    print('\033[31m{0.user} is OnLine!\033[0m'.format(client))
    print(client.user.name)
    print(client.user.id)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$teste'):
        await message.channel.send('Hello!')
  
    if message.content.lower().startswith('$tiago'):
        await message.channel.send('One of my creators!')
    
    if message.content.lower().startswith('$roll_coin'):
        #if message.author.id == "id":
        coin = random.randint(1, 2)
        if coin == 1:
            await message.add_reaction('🙂')
        elif coin == 2:
            await message.add_reaction('👑')

    if message.content.lower().startswith('$roles'):
        table = discord.Embed(
                title="Choose your role",
                color=0xB8AFEE,
                description= "- Céu = 🌈\n"
                             "- Nuvem = ☁️\n"
                             "- Trovão = ⚡\n"
                             "- Tempestade = 🌩\n"
                             "- Nevoa = 🌫️\n"
                             "- Chuva = 🌧️\n"
                             "- Sol = ☀️\n" )
        botmsg = await message.channel.send(embed=table)

        # reactions to the bot message
        await botmsg.add_reaction('🌈')
        await botmsg.add_reaction('☁️')
        await botmsg.add_reaction('⚡')
        await botmsg.add_reaction('🌩')
        await botmsg.add_reaction('🌫️')
        await botmsg.add_reaction('🌧️')
        await botmsg.add_reaction('☀️') 

# ALERT --> THIS TOKEN CANNOT BE SHARE!!!
client.run(GHOST_BOT_TOKEN)
