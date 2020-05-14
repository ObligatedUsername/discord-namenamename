import discord
from discord.ext import commands

# std lib
import os

# ext lib
import lib.botlib as bl

class Utils(commands.Cog, name='bot utils'):
    '''a set of (probably)useful functions
    
    running on: botlib by toast'''
    def __init__(self, bot):
        self.bot = bot

    # init event
    @commands.Cog.listener()
    async def on_ready(self):
        global bot_info
        bot_info = await self.bot.application_info()

    # updates
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        pass

    # error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print('something\'s definitely fucked')
        print('and that thing is:\n', error)
    
    # overwriting help command

    # commands
    @commands.command(help=bl.wikiSearch.__doc__, brief='search subject on wikipedia', aliases=['ws'])
    async def wikiSearch(self, ctx, lang, *, seq):
        res = bl.wikiSearch(lang, seq)
        if 'error' in res:
            erropt = '\n'.join(res[1])
            await ctx.send(f'your search query wasn\'t specific enough, use one of below:\n{erropt}')
        else:
            await ctx.send(f'{res[0]}\n\n{res[1]}\n\n{res[2]}')

    # ADDME: list of operator that can be used in this function
    # ADDME: more math functions and list it too
    @commands.command(help=bl.calculate.__doc__, brief='just a calculator', aliases=['calc', 'c'])
    async def calculate(self, ctx, *, exp):
        await ctx.send(f'={bl.calculate(exp)}')

def setup(bot):
    bot.add_cog(Utils(bot))
