# Main module
import discord

# instantianting a client --> our connection to discord.
client = discord.Client()

@client.event
async def on_ready():
    print('Eu entrei no {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pedro é o que?'):
        await message.channel.send('Corno!')

client.run('NjkyMDEzNDU3MTIxNDc2NzA5.XnojQg.iRpw8wOXqLsknm0hSClnyeL3FFE')
