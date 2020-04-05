
import discord
from discord.ext import commands
import random
from gtts import gTTS
from dotenv import load_dotenv
import os
import requests

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

def was_ist_heute():
    line = requests.get('https://heute-ist.dev.k118.de/?raw').text
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
        if ctx.voice_client is None:
            await ctx.send("Der Bot ist nicht mit einem voicechannel verbunden, du Hurensohn.")
            return
        
        if ctx.voice_client.is_playing:
            ctx.voice_client.stop()
        
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
    async def gzuz_whoop(self, ctx):
        await self.play(ctx, 'sounds/gzuz/gzuz_whoopwhoop.mp3')

    @commands.command()
    async def tobias(self, ctx):
        await self.play(ctx, 'sounds/washatdertobiasgemacht.mp3')

    @commands.command()
    async def cola(self, ctx):
        await self.play(ctx, 'sounds/meinecola.mp3')

    @commands.command()
    async def controller(self, ctx):
        await self.play(ctx, 'sounds/meincontroller.mp3')

    @commands.command()
    async def meinkind(self, ctx):
        await self.play(ctx, 'sounds/meinkind.mp3')

    @commands.command()
    async def normalermensch(self, ctx):
        await self.play(ctx, 'sounds/normalermensch.mp3')

    @commands.command()
    async def meinruf(self, ctx):
        await self.play(ctx, 'sounds/meinruf.mp3')

    @commands.command()
    async def gehirnschaden(self, ctx):
        await self.play(ctx, 'sounds/postanabolegehirnschädigungen.mp3')

    @commands.command()
    async def tagesschau(self, ctx):
        await self.play(ctx, 'sounds/tagesschau.mp3')

    @commands.command()
    async def tagesschauintro(self, ctx):
        await self.play(ctx, 'sounds/tagesschauintro.mp3')
            
    @commands.command()
    async def thotdetected(self, ctx):
        await self.play(ctx, 'sounds/thotdetected.mp3')

    @commands.command()
    async def tiefkuehlpommes(self, ctx):
        await self.play(ctx, 'sounds/tiefkuehlpommes.mp3')

    @commands.command()
    async def aeugh(self, ctx):
        await self.play(ctx, 'sounds/aeugh.mp3')

    @commands.command()
    async def ahfuck(self, ctx):
        await self.play(ctx, 'sounds/ahfuckicantbelieveyouvedonethis.mp3')

    @commands.command()
    async def coronawarus(self, ctx):
        await self.play(ctx, 'sounds/coronawarus.mp3')

    @commands.command()
    async def dannbinichdersohneinerhure(self, ctx):
        await self.play(ctx, 'sounds/dannbinichdersohneinerhure.mp3')

    @commands.command()
    async def freiervogel(self, ctx):
        await self.play(ctx, 'sounds/freiervogel.mp3')

    @commands.command()
    async def hska(self, ctx):
        await self.play(ctx, 'sounds/hska.mp3')

    @commands.command()
    async def iamnotdrunk(self, ctx):
        await self.play(ctx, 'sounds/iamnotdrunk.mp3')

    @commands.command()
    async def inmeinemchat(self, ctx):
        await self.play(ctx, 'sounds/inmeinemchat.mp3')

    @commands.command()
    async def maddin(self, ctx):
        await self.play(ctx, 'sounds/jahalloescheee.mp3')

    @commands.command()
    async def karsten(self, ctx):
        await self.play(ctx, 'sounds/karsten.mp3')

    @commands.command()
    async def machdeinarschzu(self, ctx):
        await self.play(ctx, 'sounds/machdeinarschzu.mp3')

    @commands.command()
    async def disappointment(self, ctx):
        await self.play(ctx, 'sounds/mydisappointmentisimmeasurable.mp3')
        
    @commands.command()
    async def luegenpresse(self, ctx):
        await self.play(ctx, 'sounds/luegenpressehaltdiefresse.mp3')
        
    @commands.command()
    async def youaintthatstraight(self, ctx):
        await self.play(ctx, 'sounds/youaintthatstraight.mp3')
        
    @commands.command()
    async def jaegermeister(self, ctx):
        await self.play(ctx, 'sounds/jaegermeister.mp3')

    @commands.command()
    async def gzuz(self, ctx):
        gzuz_list = [
        'sounds/gzuz/gzuz_brrrt.mp3',
        'sounds/gzuz/gzuz_drueckdrueck.mp3',
        'sounds/gzuz/gzuz_drueckedasgaspedal.mp3',
        'sounds/gzuz/gzuz_fuenfeuroweg.mp3',
        'sounds/gzuz/gzuz_halluzinieren.mp3',
        'sounds/gzuz/gzuz_hautfarbeovomaltine.mp3',
        'sounds/gzuz/gzuz_holmireinenrunter.mp3',
        'sounds/gzuz/gzuz_ichsaufmireinrein.mp3',
        'sounds/gzuz/gzuz_keinekooperation.mp3',
        'sounds/gzuz/gzuz_krachindernacht.mp3',
        'sounds/gzuz/gzuz_krachindernachtohnevacht.mp3',
        'sounds/gzuz/gzuz_krankenwagen.mp3',
        'sounds/gzuz/gzuz_neandertaler.mp3',
        # spanish inquisition
        'sounds/gzuz/gzuz_optimalfall.mp3',
        'sounds/gzuz/gzuz_partyistkomplett.mp3',
        'sounds/gzuz/gzuz_seximmercedes.mp3',
        'sounds/gzuz/gzuz_warumbistdunurso.mp3',
        'sounds/gzuz/gzuz_washastdugedacht.mp3',
        'sounds/gzuz/gzuz_whoopwhoop.mp3',
        'sounds/gzuz/gzuz_wirblubberblubbern.mp3',
        'sounds/gzuz/gzuz_zehneuroweg.mp3',
        ]
        await self.play(ctx, random.choice(gzuz_list))
    
    @commands.command()
    async def kotze(self, ctx):
        gzuz_list = [
        'sounds/kot.mp3',
        'sounds/kotze_wuerg2.mp3',
        'sounds/kotze_wuerg3.mp3',
        'sounds/willsassokotze.mp3'
        ]
        await self.play(ctx, random.choice(gzuz_list))
        
    @commands.command()
    async def knossi(self, ctx):
        gzuz_list = [
        'sounds/knossi/knossi_achttausendeuro.mp3',
        'sounds/knossi/knossi_albinotürke.mp3',
        'sounds/knossi/knossi_givemethemoney.mp3',
        'sounds/knossi/knossi_knossisingtürkisch.mp3',
        'sounds/knossi/knossi_nimmmimitdeuland.mp3',
        'sounds/knossi/knossi_nr1schmetterling.mp3'
        ]
        await self.play(ctx, random.choice(gzuz_list))
        
    @commands.command()
    async def knossi_achttausendeuro(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_achttausendeuro.mp3')
        
    @commands.command()
    async def knossi_albinotürke(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_albinotürke.mp3')
        
    @commands.command()
    async def knossi_givemethemoney(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_givemethemoney.mp3')
        
    @commands.command()
    async def knossi_knossisingtürkisch(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_knossisingtürkisch.mp3')
        
    @commands.command()
    async def knossi_nimmmimitdeuland(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_nimmmimitdeuland.mp3')
        
    @commands.command()
    async def knossi_nr1schmetterling(self, ctx):
        await self.play(ctx, 'sounds/knossi/knossi_nr1schmetterling.mp3')
    
   
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
