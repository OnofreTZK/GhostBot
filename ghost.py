# Main module
import discord

''' It is strongly recommended that the logging module is configured, 
as no errors or warnings will be output if it is not set up. '''
import logging

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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Teste'):
        await message.channel.send('Hello!')

client.run('NjkyMDEzNDU3MTIxNDc2NzA5.XnojQg.iRpw8wOXqLsknm0hSClnyeL3FFE')
