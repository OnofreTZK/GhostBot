from .client import *


# For random choices ( dice, coin, etc )
import random


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # just for tests
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$teste'):
        await message.channel.send('Hello!')
    #---------------------------------------------------------------------------------------------
  
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$tiago'):
        await message.channel.send('One of my creators!')
    #---------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$victor'): 
        await message.channel.send('Ainda nao fez nada.')
    #---------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$pedro'): 
        await message.channel.send('https://www.youtube.com/watch?v=xrUQrSDF3XY')
    #---------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$lascaoverbo'):
        await message.channel.send(random.choice(StateManager.get_phrases()))
    #---------------------------------------------------------------------------------------------
    
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$triputo'): 
        await message.channel.send('https://www.youtube.com/watch?v=mMoF5WuBrkI')
    #---------------------------------------------------------------------------------------------
    
    # $roll_coin ( heads or tails || cara ou coroa )
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$roll_coin'):
        #if message.author.id == "id":
        coin = random.randint(1, 2)
        if coin == 1:
            await message.add_reaction('🙂')
        elif coin == 2:
            await message.add_reaction('👑')
    #---------------------------------------------------------------------------------------------

    # $roles ( minimal role manager )
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$roles'):
        table = discord.Embed(
                title="Choose your role",
                color=0xB8AFEE,
                description= "- Nuvem = ☁️\n"
                             "- Trovão = ⚡\n"
                             "- Tempestade = 🌩\n"
                             "- Nevoa = 🌫️\n"
                             "- Chuva = 🌧️\n"
                             "- Sol = ☀️\n" )
        
        botmsg = await message.channel.send(embed=table)

        # reactions to the bot message
        await botmsg.add_reaction('☁️')
        await botmsg.add_reaction('⚡')
        await botmsg.add_reaction('🌩')
        await botmsg.add_reaction('🌫️')
        await botmsg.add_reaction('🌧️')
        await botmsg.add_reaction('☀️') 
        
        # Changing globals
        # show the id of the message and user for other events
        #global botmsg_id
        #botmsg_id = botmsg.id 
        StateManager.set_msg_id(botmsg.id)

        #global user_id 
        #user_id = message.author.id
        StateManager.set_user_id(message.author.id)
    #----------------------------------------------------

 
    # $ghost_in
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$ghost_in'):
        try:
            
            target = message.author.voice.channel # member->voicestate->channel
            StateManager.create_voice_client(await target.connect()) # this VoiceChannel method returns a Voice Client
        
        except AttributeError:
            
            await message.channel.send('Entre em um canal de voz carai')

    #---------------------------------------------------------------------------------------------
    
    # $ghost_out
    #---------------------------------------------------------------------------------------------
    if message.content.lower().startswith('$ghost_out'):
        await StateManager.quit_voice_client().disconnect()
    #---------------------------------------------------------------------------------------------
