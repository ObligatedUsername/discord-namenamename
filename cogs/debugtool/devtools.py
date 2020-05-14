import discord
from discord.ext import commands

# std lib
import os

# external lib
from pythonping import ping as pyping

class DevTools(commands.Cog, name='developer tools'):
    '''a quickly bodged together toolbox for debugging and whatnot'''
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

    # test commands
    @commands.command(brief='pongs pinger', aliases=['p'])
    async def ping(self, ctx):
        '''pings the bot and pongs the pinger'''
        response_time_ms = pyping('8.8.8.8', size=40, count=10).rtt_avg_ms
        await ctx.send(f'pong in {response_time_ms}')

    @commands.command(brief='message yourself', aliases=['msg'])
    async def reply(self, ctx, *, message):
        '''sends the specified message to yourself'''
        await ctx.send(f'{message}')

    # user specific commands (owner)
    @commands.command(brief='logs bot out', aliases=['shutdown'])
    async def logout(self, ctx):
        '''shuts down this bot'''
        if ctx.author.id == bot_info.owner.id:
            await ctx.send('see ya')
            await self.bot.logout()
            print('logged out by owner')
        else: await ctx.send('nice try')

    @commands.command(brief='reloads bot', aliases=['rel'])
    async def reload(self, ctx):
        '''reloads the bot without messing with cmd'''
        if ctx.author.id == bot_info.owner.id:
            await ctx.send('reloading..')
            await self.bot.logout()
            print('starting new process..')
            os.system('py bot.py')
        else: await ctx.send('how \'bout no?')

def setup(bot):
    bot.add_cog(DevTools(bot))