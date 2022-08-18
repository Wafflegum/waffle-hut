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
    with open("./extensions/afk.json") as f:
        data = json.load(f)
    
    if data[str(ctx.member.guild_id)][0]["afk role"] not in str(ctx.member.role_ids):
        if(ctx.options.baket == None):
            embed = hikari.Embed(title=f"{ctx.member.display_name} is now afk")
            embed.set_footer("/unafk to afk or just chat anything.")
            await ctx.respond(embed)
        else:
            embed = hikari.Embed(title=f"{ctx.member.display_name} is now afk because {ctx.options.baket}")
            embed.set_footer("/unafk to afk or just chat anything.")

            await ctx.respond(embed)

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
    
    if data[str(ctx.member.guild_id)][0]["afk role"] in str(ctx.member.role_ids):
        guild_id = str(ctx.guild_id)

        with open("./extensions/afk.json") as f:
            data = json.load(f)
        if str(ctx.member.display_name).startswith("[AFK]"): # Checks if the user has [AFK] before of it's nickname
            await ctx.member.edit(nickname=ctx.member.display_name[6:])

        await ctx.member.remove_role(data[guild_id][0]["afk role"]) # This will remove AFK role on the member.

        bubu = ['Dapat di ka na bumalik', 'Nayswan', 'Bonak', 'Hayst.', 'Pake ko?', '']
        mura = random.choice(bubu)
        embed = hikari.Embed(title=f"{ctx.member.display_name} is back. {mura}")
        embed.set_footer("/AFK to afk again")
        await ctx.respond(embed)
    else:
        embed = hikari.Embed(title=f"Di ka afk tanga")
        embed.set_footer("/afk to afk")
        await ctx.respond(embed)

    
@plugin.listener(hikari.GuildMessageCreateEvent)
async def unafk_activity(event: hikari.GuildMessageCreateEvent) -> None:
    with open("./extensions/afk.json") as f:
        data = json.load(f)
    
    if data[str(event.member.guild_id)][0]["afk role"] in str(event.member.role_ids):
        try:
            if str(event.member.display_name).startswith("[AFK]"):
                await event.member.edit(nickname=event.member.display_name[6:])
        except:
            pass
        # member_roles = await event.member.fetch_roles()
        # print(await event.member.fetch_roles())
        await event.member.remove_role(data[str(event.member.guild_id)][0]["afk role"]) # This will remove AFK role on the member.
        bubu = ['Dapat di ka na bumalik', 'Nayswan', 'Bonak', 'Hayst.', 'Pake ko?', '']
        mura = random.choice(bubu)
        embed = hikari.Embed(title=f"{event.member.display_name} is back. {mura}")
        embed.set_footer("/unafk to afk or just chat anything.")
        
        await event.message.respond(embed)
        # if data[str(guild.id)][0]["afk role"] == member_roles[0]["id"]:
        #     print(f"{event.author.display_name} is afk")

def load(bot):
    bot.add_plugin(plugin)