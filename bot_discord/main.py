import discord
import random

intents = discord.Intents().all()
client = discord.Client(intents=intents)
keywords = ["#Banword"]

@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_message(message):
    member = message
    role = message.guild.get_role(1051982725340471358)
    numero = random.randint(1, 10000)
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.delete()
                await member.author.add_roles(role)
                await message.channel.send(">>> " + str(member.author.mention) + " __Vous avez été warn !__ " + str(numero))
                print (member.author)
                print (numero)
                print (message.content)



client.run("#Your_Token")
