# importing all module files
from pkgs import *


# For random choices ( dice, coin, etc )
import random

# global vars zone( migth change in events )
botmsg_id = 'id' 

user_id = 'id'
#------------------------------------------


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
        global botmsg_id
        botmsg_id = botmsg.id 

        global user_id 
        user_id = message.author.id
        # ----------------------------------------------------
    #---------------------------------------------------------------------------------------------


@client.event
async def on_reaction_add(reaction, user):
    msg= reaction.message
   
    # $roles ( add roles )
    #---------------------------------------------------------------------------------------------
    # this was hard to fixed, due to a good documentaton and, of course, Stack Overflow i was able to do.
    if reaction.emoji == '☁️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Nuvem", msg.guild.roles)
        # this is the only way that i found to get a Member...
        # add_roles() it is a Member object method.
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '⚡' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Trovão", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌩' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Tempestade", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌫️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Névoa", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌧️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Chuva", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '☀️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Sol", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)
    #---------------------------------------------------------------------------------------------


@client.event
async def on_reaction_remove(reaction, user):
    msg= reaction.message

    # $roles ( remove role )
    #---------------------------------------------------------------------------------------------
    if reaction.emoji == '☁️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Nuvem", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)
    
    if reaction.emoji == '⚡' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Trovão", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌩' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Tempestade", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌫️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Névoa", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌧️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Chuva", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '☀️' and msg.id == botmsg_id and user.id == user_id:
        role = discord.utils.find(lambda r : r.name == "Sol", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)
    #---------------------------------------------------------------------------------------------


# RUN
# ALERT --> THIS TOKEN CANNOT BE SHARE!!!
client.run(GHOST_BOT_TOKEN)
