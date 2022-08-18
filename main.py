import os

import discord
from discord.ext import commands

import random
import dotenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') # Create a .env containing and setting your discord token. DISCORD_TOKEN = token

bot = commands.Bot(command_prefix='<=3')

my_file = open("truth.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
truth_list = data.split('\n')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_command(description="bot response tester")
async def ping(ctx):
    await ctx.send('titi')

@bot.command()
async def truth(ctx):
    question = random.choice(truth_list)
    embed = discord.Embed(title="You picked truth!", description=str(question), colour=0xE5E242)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.slash_command(descrition="Truth or dare but no dare. This will give you random questions.")
async def truth(ctx):
    question = random.choice(truth_list)
    embed = discord.Embed(title=f"{ctx.author.name} picked truth!", description=str(question), colour=0xE5E242)
    
    embed.set_author(name=ctx.author.name, icon_url=f"{ctx.author.display_avatar}")
    await ctx.respond(embed=embed)

@bot.slash_command()
async def afk(ctx):
    # if reason == None:
    #     reason = "ewan ko kung bakit."
    
    username = ctx.author.name
    await ctx.author.edit(nick = f"[AFK] {username}")
    # except:
    #     await ctx.send("No permission to change nicknames!")
    #     pass
    
    # await ctx.send(f"{member.user} is now afk because {reason}")

# @client.command()
# async def help(ctx):
#     embed = discord.Embed()
#     await ctx.send(embed=embed)

bot.run(TOKEN)