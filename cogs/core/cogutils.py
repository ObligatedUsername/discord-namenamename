import discord
from discord.ext import commands

# std lib
import os

class CogUtils(commands.Cog, name='cog utilities'):
    '''a quickly bodged together utilityset for configuring cogs'''
    def __init__(self, bot):
        self.bot = bot
        self.cogdict = {}
    
    # init event
    def update(self):
        '''updates cog dictionary'''
        for ln in os.listdir('./cogs'): self.cogdict[ln] = [cn[:-3] for cn in os.listdir(f'./cogs/{ln}') if cn != '__pycache__']
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.update()
        global bot_info
        bot_info = await self.bot.application_info()

    # updates
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        self.update()

    # error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print('something\'s definitely fucked')
        print('and that thing is:\n', error)

    # cogutils commands
    @commands.command(brief='loads cogs', aliases=['cld'])
    async def load(self, ctx, lib, cog):
        '''loads specified unloaded external cogs'''
        if ctx.author.id == bot_info.owner.id:
            if lib in self.cogdict.keys() and cog in self.cogdict[lib]:
                self.bot.load_extension(f'cogs.{lib}.{cog}')
                self.cogdict[lib].remove(cog)
            else: ctx.send('specified cog library or cog is already loaded or it doesn\'t exist')
        else: ctx.send('ask your parents for one')

    # FIXME: cogdict is for loading only, get another var for keeping track of loaded external cogs
    
    # @commands.command()
    # async def unload(self, ctx, lib, cog, *, _):
    #     '''unloads specified loaded external cogs'''
    #     if ctx.author.id == bot_info.owner.id:
    #         if lib in cogdict.keys() and cog in cogdict[lib]:
    #            bot.unload_extension(f'cogs.{lib}.{cog}')
    #         else: ctx.send('specified cog library or cog is already unloaded or it doesn\'t exist')
    #     else: ctx.send('ask your parents for none')

def setup(bot):
    bot.add_cog(CogUtils(bot))