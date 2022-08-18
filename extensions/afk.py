import random
import hikari
import lightbulb

import json


plugin = lightbulb.Plugin('afk')

@plugin.command
@lightbulb.option("baket", "bat ka mag eAFK?", required=False)
@lightbulb.command('afk', 'afk ka')
@lightbulb.implements(lightbulb.SlashCommand)
async def afk(ctx: lightbulb.SlashContext) -> None:
    if str(ctx.member.display_name).startswith("[AFK]") == False:
        if(ctx.options.baket == None):
            await ctx.respond(f"{ctx.author.mention} is now afk")
        else:
            await ctx.respond(f"{ctx.author.mention} is now afk because {ctx.options.baket}")

        ##create a dictionary to dump in a json file that contains all guild IDs, and afk role ids.
        dic = {
            str(ctx.guild_id):[
                {
                    "afk role": ""
                }
            ]
        }
        guild_id = str(ctx.guild_id)
        with open("./extensions/afk.json") as f:
            data = json.load(f)


        if guild_id in data:
            print(f"{guild_id} already exist in database")
        else:
            role = await plugin.bot.rest.create_role( ## create  role >
                ctx.guild_id,
                name="AFK")
            print(f"Created AFK role; role id={role.id}")
            dic[guild_id][0]["afk role"] = str(role.id)## <

            data.update(dic)


        with open("./extensions/afk.json", 'w') as f:
            json.dump(data, f, indent=2)

        await ctx.member.add_role(data[guild_id][0]["afk role"])
        try:
            await ctx.member.edit(nickname=f'[AFK] {ctx.member.display_name}')
        except:
            embed = hikari.Embed(
                title="No permission to change nicknames", 
                description="Either I don't have permission to change nicknames or your role is too high.",
                color='E74C3C')
            await ctx.respond(embed)
            pass

@plugin.command
@lightbulb.command('unafk', 'di ka na afk')
@lightbulb.implements(lightbulb.SlashCommand)
async def unafk(ctx: lightbulb.SlashContext) -> None:
    with open("./extensions/afk.json") as f:
        data = json.load(f)
    guild_id = str(ctx.guild_id)

    if str(ctx.member.display_name).startswith("[AFK]"):
        await ctx.member.edit(nickname=ctx.member.display_name[6:])
    await ctx.member.remove_role(data[guild_id][0]["afk role"]) # This will remove AFK role on the member.

    bubu = ['Dapat di ka na bumalik', 'Nayswan', 'Bonak', 'Hayst.', 'Pake ko?', '', '']
    mura = random.choice(bubu)
    await ctx.respond(f"{ctx.author.mention} is back. {mura}")

def load(bot):
    bot.add_plugin(plugin)
