import os

import discord
from discord.ext import commands

import random
# from dotenv import load_dotenv
# load_dotenv()

tok = 'MTAwNjIyODY5OTI1MjgwNTY3Mg.G3DexK.I0Wlzqo5WvHSmCaqDq_uRhfHmEMmZtdwYd-BqA'
TOKEN = tok #'DISCORD_TOKEN'

client = discord.Client()
client = commands.Bot(command_prefix='<=3')

my_file = open("truth.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
truth_list = data.split('\n')
print(truth_list)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def ping(ctx):
    await ctx.send('titi')

@client.command()
async def truth(ctx):
    question = random.choice(truth_list)
    embed = discord.Embed(title="You picked truth!", description=str(question), colour=0xE5E242)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

client.run(TOKEN)
