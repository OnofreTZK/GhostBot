# importing all module files
from pkgs import *

@client.event
async def on_socket_raw_receive(msg):
    await StateManager.next()

@client.event
async def on_socket_raw_send(payload):
    await StateManager.next()

# RUN
# ALERT --> THIS TOKEN CANNOT BE SHARE!!!
client.run(GHOST_BOT_TOKEN)


