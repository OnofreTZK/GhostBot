# importing all module files
from pkgs import *

@client.event
async def on_resumed():

    # make queue working
    if not StateManager.voice_status() and not StateManager.queue_empty():
        StateManager.next()

# RUN
# ALERT --> THIS TOKEN CANNOT BE SHARE!!!
client.run(GHOST_BOT_TOKEN)
