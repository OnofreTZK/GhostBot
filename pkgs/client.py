# Main module --> discord API
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
    print('\033[93m{0.user} is OnLine!\033[0m'.format(client))
    print(client.user.name)
    print(client.user.id)
