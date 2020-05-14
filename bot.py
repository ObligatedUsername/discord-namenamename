import discord
from discord.ext import commands

# std lib
import os

# bot init
desc = 'a quickly bodged together bot with weird ass functionality'
def_prefix = '..'
bot = commands.Bot(command_prefix=def_prefix, description=desc)
def_cogs = ['devtools', 'cogutils', 'botpack-1']

def update():
    '''updates cog dictionary'''
    global cogdict
    cogdict = {}
    for ln in os.listdir('./cogs'): cogdict[ln] = [cn[:-3] for cn in os.listdir(f'./cogs/{ln}') if cn != '__pycache__']
update()

for clib, clist in cogdict.items():
    for cog in clist:
        if cog in def_cogs:
            bot.load_extension(f'cogs.{clib}.{cog}')

# misc init

# event handling
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name}')

@bot.event
async def on_command_completion(ctx):
    update()

bot.run('NzA1ODA1MzMyMjE1MTAzNDk4.XqxGfw.Dde6mdSRfAjUvTOHmMT1Z_jT9ms')