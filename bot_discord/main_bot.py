#Created by Bushay
#03/03/2023
#Question -> Discord : Bushay#8875

from discord.ext import commands
import discord
import asyncio
from discord_slash import SlashCommand
import datetime
from datetime import datetime
from discord.utils import get


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("𝓢𝓽𝓪𝓻𝓔")

@bot.command()
@commands.has_permissions(administrator=True)
async def dlt(ctx, ammount=11): # channels should be a list of discord.Channel objects
    ammount = ammount+2
    ammountback = 1
    await ctx.send(">>> __En chargement__")
    await ctx.send(".")
    await asyncio.sleep(0.1)
    await ctx.channel.purge(limit=ammountback)
    await ctx.send("..")
    await asyncio.sleep(0.1)
    await ctx.channel.purge(limit=ammountback)
    await ctx.send("...")
    await ctx.channel.purge(limit=ammountback)
    await ctx.channel.purge(limit=ammount)
    await ctx.send(">>> __Messages effacés__")

@dlt.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(">>> __Tu as besoin de permissions pour utiliser cette commande__")

@slash.slash(description="Regarde toutes les commandes disponible")
async def commandes(ctx):
    await ctx.reply("#Your_command")
####################################

@slash.slash(description="Report un utilisateur ayant enfreint les règles du serveur")
async def report(ctx, user: discord.Member):
    role = get(ctx.guild.roles, name="Report")
    await user.add_roles(role)
    await ctx.send(">>> __Vous avez bien report__ " + str(user.mention))

##################################

@slash.slash(description="Met toi en mode Afk")
async def afk(ctx):
    member = ctx
    role = get(ctx.guild.roles, name="Afk")
    memberole = get(ctx.guild.roles, name="Membre")
    await member.author.remove_roles(memberole)
    await member.author.add_roles(role)
    await ctx.send(">>> __Vous êtes désormais en mode Afk__")
#################################
@slash.slash(description="Enlève le mode Afk")
async def unafk(ctx):
    member = ctx
    memberole = get(ctx.guild.roles, name="Membre")
    role = get(ctx.guild.roles, name="Afk")
    await member.author.remove_roles(role)
    await member.author.add_roles(memberole)
    await ctx.send(">>> __Vous n'êtes plus en mode Afk__")

###################################

@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = Put_your_MessageID

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == "📦":
            role = discord.utils.get(guild.roles, name="#Role_Name")
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 1052652077114998822

    if ourMessageID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
    if emoji == "📦":
        role = discord.utils.get(guild.roles, name="Drop")
    member = await(guild.fetch_member(payload.user_id))
    if member is not None:
        await member.remove_roles(role)
    else:
        print("Membre non trouvé")




@bot.command()
@commands.has_permissions(administrator=True)
async def react(ctx):
    nmb = 1
    embed = discord.Embed(
        title="__Prend ton rôle **#Role_Name**__",
        description="Clique sur la réaction pour avoir le rôle",
        timestamp=datetime.now(),
        color= 0xffff00
    )
    await ctx.channel.purge(limit=nmb)
    msg = await ctx.send(embed=embed)
    # rôle
    await msg.add_reaction("📦")
##############################

@bot.command()
@commands.has_permissions(administrator=True)
async def reportlist(ctx):
    role = ctx.guild.get_role(#Role_ID)
    await ctx.send(role.members)

@reportlist.error
async def reportlist_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"**__Tu as besoin de permissions pour utiliser cette commande__**")
##############################
@bot.command()
@commands.has_permissions(administrator=True)
async def bed(ctx, embed):
    embed = discord.Embed(
        description=embed,
        color= 0x66b4ff
    )
    await ctx.send(embed=embed)
#############################
@bot.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, titre, embed):
    embed = discord.Embed(
        title=titre,
        description=embed,
        color= 0x66b4ff
    )
    await ctx.send(embed=embed)
##################################
@slash.slash(description="Crée une suggestion")
async def suggestion(ctx, titre, explication):
    embed = discord.Embed(
        title=titre,
        description=explication,
        color= 0x66b4ff
    )
    rea = await ctx.send(embed=embed)
    await rea.add_reaction("☑️")
    await rea.add_reaction("❌")

bot.run("#Your_Token")