
import discord
#from discord.ext.commands import CommandNotFound
import re
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
from gtts import gTTS
from dotenv import load_dotenv
from os import getenv, listdir
import os
from os.path import isfile, join
import requests

load_dotenv()

bot_key = os.getenv("KEY")

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)
soundpath = './sounds'
files = sorted([f for f in listdir(soundpath) if isfile(join(soundpath, f))])

def random_zitat():
    afile = open('zitate.txt')
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    return line

def was_ist_heute():
    line = requests.get('https://heute-ist.dev.k118.de/?raw').text
    return line

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @staticmethod
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            word = re.findall('"([^"]*)"', str(error))[0]
            print("Wort: " + str(word))
            sounds = [i for i, x in enumerate(files) if x.startswith(word)]
            print("Sound: " + str(sounds))
            if len(sounds) > 1:
                await Music.play(ctx, 'sounds/' + files[random.choice(sounds)])
                print("Datei: " + str(files[random.choice(sounds)]))
            elif len(sounds) == 1:
                await Music.play(ctx, 'sounds/' + files[sounds[0]])
                print("Datei: " + str(files[sounds[0]]))
            else:
                await ctx.send("Das kenne ich nicht, du Hurensohn.") 
                print("Hurensohn");
        else:
            print(error)


    @commands.command()
    async def join(self, ctx):
        print(self)
        channel = ctx.message.author.voice.channel

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @staticmethod
    async def play(ctx, query):
        if ctx.voice_client is None:
            await ctx.send("Der Bot ist nicht mit einem voicechannel verbunden, du Hurensohn.")
            return
        
        if ctx.voice_client.is_playing:
            ctx.voice_client.stop()
        
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    
    @commands.command()
    async def list(self, ctx):
        await ctx.send("Folgendes kann ich sagen: \n```\n" + "\n".join(files) + "\n```")
        await ctx.send("Füge einfach ein`?` vor den Namen. Du musst den Titel nicht mal komplett ausschreiben. Wenn es mehrere mit demselben Anfang gibt, wird zufällig etwas auswählt. \nBspw: `?gzuz` kann zu `gzuz_brrrt.mp3` oder `gzuz_drueckdrueck.mp3` werden.")

    @commands.command()
    async def zitat(self, ctx):
        zitat = random_zitat()
        output = gTTS(zitat, lang='de')
        output.save('temp.wav')
        await ctx.send(zitat)
        await self.play(ctx, 'temp.wav')

    @commands.command()
    async def heute(self, ctx):
        heu = was_ist_heute()
        output = gTTS(heu, lang='de')
        output.save('temp.wav')
        await ctx.send(heu)
        await self.play(ctx, 'temp.wav')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.add_cog(Music(bot))
bot.run(bot_key)
