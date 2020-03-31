from .message import *


@client.event
async def on_reaction_add(reaction, user):
    msg= reaction.message
   
    # $roles ( add roles )
    #---------------------------------------------------------------------------------------------
    # this was hard to fixed, due to a good documentaton and, of course, Stack Overflow i was able to do.
    if reaction.emoji == '☁️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Nuvem", msg.guild.roles)
        # this is the only way that i found to get a Member...
        # add_roles() it is a Member object method.
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '⚡' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Trovão", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌩' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Tempestade", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌫️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Névoa", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '🌧️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Chuva", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)

    if reaction.emoji == '☀️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Sol", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).add_roles(role)
    #---------------------------------------------------------------------------------------------


@client.event
async def on_reaction_remove(reaction, user):
    msg= reaction.message

    # $roles ( remove role )
    #---------------------------------------------------------------------------------------------
    if reaction.emoji == '☁️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Nuvem", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)
    
    if reaction.emoji == '⚡' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Trovão", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌩' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Tempestade", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌫️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Névoa", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '🌧️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Chuva", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)

    if reaction.emoji == '☀️' and msg.id == StateManager.get_msg_id() and user.id == StateManager.get_user_id():
        role = discord.utils.find(lambda r : r.name == "Sol", msg.guild.roles)
        await discord.utils.find(lambda m: m.id == user.id, msg.guild.members).remove_roles(role)
    #---------------------------------------------------------------------------------------------
