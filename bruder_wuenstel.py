import discord
from discord.ext import commands
import random
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()

bot_key = os.getenv("KEY")

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

def random_zitat():
    afile = open('zitate.txt')
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    return line

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @classmethod
    async def play(self, ctx, query):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    @commands.command()
    async def curb(self, ctx):
        await self.play(ctx, 'sounds/curb.mp3')
    
    @commands.command()
    async def doubt(self, ctx):
        await self.play(ctx, 'sounds/doubt.mp3')
    
    @commands.command()
    async def drum(self, ctx):
        await self.play(ctx, 'sounds/drum.mp3')
 
    @commands.command()
    async def error(self, ctx):
        await self.play(ctx, 'sounds/error.mp3')

    @commands.command()
    async def egal(self, ctx):
        await self.play(ctx, 'sounds/egal.mp3')

    @commands.command()
    async def standard(self, ctx):
        await self.play(ctx, 'sounds/standard.mp3')

    @commands.command()
    async def kot(self, ctx):
        await self.play(ctx, 'sounds/kot.mp3')


    @commands.command()
    async def zitat(self, ctx):
        zitat = random_zitat()
        output = gTTS(zitat, lang='de')
        output.save('temp.wav')
        await ctx.send(zitat)
        await self.play(ctx, 'temp.wav')
 

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.add_cog(Music(bot))
bot.run(bot_key)
