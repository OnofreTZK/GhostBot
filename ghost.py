# importing all module files
from pkgs import *


# For random choices ( dice, coin, etc )
import random


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # just for tests
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
