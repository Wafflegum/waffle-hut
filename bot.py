from doctest import debug_script
import hikari
import lightbulb
import os

import random

import dotenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') # Create a .env containing and setting your discord token. DISCORD_TOKEN = token
bot = lightbulb.BotApp(token=TOKEN, prefix='<=3', intents=hikari.Intents.ALL)

bot.load_extensions_from('./extensions/')

my_file = open("truth.txt", "r")
  
data = my_file.read() # reading the file

# replacing end splitting the text 
# when newline ('\n') is seen.
truth_list = data.split('\n')

@bot.command 
@lightbulb.command('ping', 'mumurahin ka')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('tanginamo')

@bot.command
@lightbulb.command('truth', 'truth or dare kaso truth lang')
@lightbulb.implements(lightbulb.SlashCommand)
async def truth(ctx: lightbulb.SlashContext) -> None:
    question = random.choice(truth_list)

    embed = hikari.Embed(
        title=question
    )
    embed.set_footer("/truth for more")
    embed.set_author(name=ctx.author.username, icon=ctx.author.display_avatar_url)
    await ctx.respond(embed)

@bot.command
@lightbulb.option('msg', "your message")
@lightbulb.command('embed', 'embed a message')
@lightbulb.implements(lightbulb.SlashCommand)
async def embed(ctx: lightbulb.SlashContext) -> None:

    em = hikari.Embed(title=str(ctx.options.msg))
    await ctx.respond(em)


bot.run()