from typing_extensions import Required
import hikari
import lightbulb

import json

plugin = lightbulb.Plugin('reaction_roles')

@plugin.command
@lightbulb.command("reaction", "this is a command group about reaction roles")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def reaction_roles(ctx):
    pass

@reaction_roles.child
@lightbulb.option("channel", "which channel do you want to put this in?", required=True)
@lightbulb.command("make", "create an embed message where they can react to get a role.")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def create(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond("titi")

def load(bot):
    bot.add_plugin(plugin)