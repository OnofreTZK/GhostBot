from .client import *

@client.event
async def on_member_join(member): # welcome message in text channel
    await client.wait_until_ready()
    welcome = client.get_channel(695350664175550494)
    msg = "Bem vindo(a), {}, por favor leias as regras.".format(member.mention)
    await welcome.send(msg)

@client.event
async def on_member_remove(member): # Goodbye message in dm
    canaldm = await member.create_dm()
    msg = "Não tenho ciência dos motivos de sua saida, entretanto, lhe desejo o melhor dos destinos! Adeus, {}.".format(member.mention)
    await canaldm.send(msg)
