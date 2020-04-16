# importing all module files
from pkgs import *

@client.event
async def on_socket_raw_receive(msg):
    if await StateManager.next():
        playnow = discord.Embed( 
                  title="Playing:",
                  description= StateManager.get_metadata() ) 
        await client.get_channel(StateManager.get_msg_id()).send(embed=playnow)

@client.event
async def on_socket_raw_send(payload):
    if await StateManager.next():
        playnow = discord.Embed( 
                  title="Playing:",
                  description= StateManager.get_metadata() ) 
        await client.get_channel(StateManager.get_msg_id()).send(embed=playnow)

# RUN
# ALERT --> THIS TOKEN CANNOT BE SHARE!!!
client.run(GHOST_BOT_TOKEN)


