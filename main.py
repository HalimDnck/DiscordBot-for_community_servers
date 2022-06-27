#Dataset
import numpy as np
import pandas as pd
import difflib #kullanıcının kelime hatası yaptığında düzelten kütüphane
from sklearn.feature_extraction.text import TfidfVectorizer #veri setinde olan text değerlerini mantıklı sayılara dönüştürüyor
from sklearn.metrics.pairwise import cosine_similarity #veriler arasında benzerlik skoru oluşturur
#DiscordBot
import asyncio
import discord
import youtube_dl
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from discord.utils import get
from dotenv import load_dotenv
from youtube_dl import YoutubeDL

#Film önerisi
dataset = pd.read_csv("movies.csv")

features = ["genres","keywords","tagline","cast","director"]

for feature in features:
    dataset[feature] = dataset[feature].fillna("")

combine = dataset["genres"]+ " "+dataset["keywords"]+ " "+dataset["tagline"]

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combine)

similarity= cosine_similarity(feature_vectors)

@client.event
async def on_message(message):
    if message.content.startswith("!film"):
        channel = message.channel
        await channel.send("deneme")

        def check(m):
            return m.content == "hello" and m.channel == channel

        movie_name = await client.wait_for("message", check=check)
        await channel.send(f"hey {msg}")





load_dotenv()
players = {}

client = discord.Client()

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True).all()
bot = commands.Bot(command_prefix="*", intents=intents)


TOKEN = open("token.txt", "r").read()
@bot.event
async def on_ready():
    koalaf1.start()
    await bot.change_presence(activity=discord.Streaming(name="!yardım", url="https://www.twitch.tv/koalaf1rekabetligi"))
    print("Hazır")

#Loop Mesajları
@tasks.loop(hours=6)
async def koalaf1():
    for c in bot.get_all_channels():
        if c.id == 424575536832970753:
            await c.send("Ben RoboKoala, sana yardımcı olmak için buradayım. !yardım komutu ile yapabileceğim işlemleri görebilirsin.")


@tasks.loop(hours=4)
async def koalasosyal():
    for c in bot.get_all_channels():
        if c.id == 424575536832970753:
            await c.send("***KoalaF1 ligi sosyal medya adresleri:\nInstagram: https://www.instagram.com/f1koalaleague/\nTwitch: https://www.twitch.tv/koalaf1rekabetligi\nTwitter: https://twitter.com/koala_league \nYoutube: https://www.youtube.com/channel/UCQxVWLIwz1-AURq6mTK3Dfw***")

#Üye mesajları
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name= "üye-aksiyonları")
    await channel.send(f"** {member} aramıza hoş geldin. Ben RoboKoala, sana yardımcı olmak için buradayım.  Aklındaki soruları bana sorarsan sana ışık hızında yardımcı olabilirim. **")
    print(f"{member} aramıza hoş geldin. Ben RoboKoala, sana yardımcı olmak için buradayım.  Aklındaki soruları bana sorarsan sana ışık hızında yardımcı olabilirim.")

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="üye-aksiyonları")
    await channel.send(f"** {member} bariyerlerde. Umarım yakın zamanda pistlere geri dönersin. **")
    print(f"{member} bariyerlerde. Umarım yakın zamanda pistlere geri dönersin.")


#Mesaj temizleme
@bot.command()
@commands.has_role("FIA")
async def clear(ctx, amount=30):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    print(error)
    print(type(error))
    if isinstance(error, commands.MissingRole):
        await ctx.send("**Bu komutu kullanmak için gerekli yetkiye sahip değilsiniz.**")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("**Lütfen !clear komutundan sonra temizlemek istediğiniz mesaj sayısını giriniz.**")

#Ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"İnternet gecikmeniz {round(bot.latency * 100)}ms")


# Text Kısmı

@bot.command()
async def yardım(ctx):
    await ctx.send("**Komutların listesi: \n!koala : Ligimiz ile ilgili cevaplayabileceğim sorular. \n!ping : İnternet gecikmenizi görüntüleyebilirsiniz. \n!clear : Metin kanalında temizlik yapmak için kullanabilirsiniz. \n!yardım : Size yardımcı olabileceğim konular. \n!join : Ses kanalınıza beni de davet edebilirsiniz. \n!search : Youtube'da istediğiniz şarkıyı arayabilirim. \n!play : Sizin için bir şarkı çalabilirim. \n!iletisim : İletişim bilgilerimiz. **")
@bot.command()
async def koala1(ctx):
    await ctx.send("**KoalaF1 ligi hem eğlence hem de rekabet ortamını yaşamak isteyen bir Formula 1 topluluğudur. 5. sezonumuz ile birlikte sizlere mümkün olabilecek en iyi şekilde hizmet etmeye çalışıyoruz.**")

@bot.command()
async def koala2(ctx):
    await ctx.send("** Ligimize katılmak için  <@252870549682782219> ile iletişim kurabilirsiniz. **")

@bot.command()
async def koala3(ctx):
    await ctx.send("***Perşembe günleri saat 21.00da https://www.twitch.tv/koalaf1rekabetligi Twitch kanalımızda canlı yayında oluyoruz.***")

@bot.command()
async def koala4(ctx):
    await ctx.send("***Instagram: https://www.instagram.com/f1koalaleague/\nTwitch: https://www.twitch.tv/koalaf1rekabetligi\nTwitter: https://twitter.com/koala_league \nYoutube: https://www.youtube.com/channel/UCQxVWLIwz1-AURq6mTK3Dfw***")

@bot.command()
async def koala5(ctx):
    await ctx.send("**16 Mart İspanya GP 🇪🇸 \n 24 Mart Macaristan GP 🇭🇺 \n 31 Mart Bahreyn GP 🇧🇭 \n 7 Nisan İmola GP  🇮🇹\n 14 Nisan Azerbaycan GP 🇦🇿 \n 21 Nisan Portekiz GP 🇵🇹 \n 28 Nisan Hollanda GP  🇳🇱\n 5 Mayıs Avusturya GP 🇦🇹 \n 12 Mayıs Japonya GP 🇯🇵 \n 19 Mayıs Kanada 🇨🇦 \n 26 Mayıs Suudi Arabistan GP 🇸🇦 \n 2 Haziran İngiltere GP 🇬🇧 \n 9 Haziran Belçika GP 🇧🇪 \n 16 Haziran Brazilya GP 🇧🇷**")

@bot.command()
async def koala6(ctx):
    await ctx.send("***Şu anda ligimizin pilot kadrosunda her hangi bir boşluk yoktur. Yedek pilot başvurusu için <@252870549682782219> 'a başvurabilirsiniz.***")

@bot.command()
async def koala7(ctx):
    await ctx.send("**7-Yönetim kadromuz:** \n <@252870549682782219> \n <@810480024208932894> \n <@535070883614687233> \n <@312659754189324288> \n <@604955586299166722> \n <@284757464467898368> \n <@426363948829376513> \n <@277422455063314442> \n <@397016413014851584>")

@bot.command()
async def koala8(ctx):
    await ctx.send("***Ligimiz başladıktan sonra güncel puan durumu ile karşınızda olacağız***")

@bot.command()
async def koala9(ctx):
    await ctx.send("***Benim adım RoboKoala. Halim Dinçkalmış tarafından yüksek teknoloji kullanılarak tasarlandım. Senin sorularına cevap vermek için buradayım.!yardım komutu ile yapabileceklerimi görebilirsin.***")

@bot.command()
async def koala(ctx):
    await ctx.send("**Merhabalar :hello: \n\n*Size yardımcı olabileceğim konular:* \n\n1- KoalaF1 ligi hakkında genel bilgi. \n2- Lige nasıl katılabilirim? \n3- Yarışları nasıl takip edebilirim? \n4- Sosyal medya hesaplarımız. \n5- Yarış takvimi nedir? \n6- Ligde yer var mı? \n7- Yönetici listesi. \n8- Güncel puan durumu. \n9- Ben kimim? \n\n*Sormak istediğiniz soruya !koala (soru numarası) komutuyla ulaşabilirsiniz.\nÖrnek: !koala2 **")

@bot.command()
async def iletisim(ctx):
    await ctx.send("**Şikayet ve önerlireniz için <@487271147889491978> iletişime geçebilirsiniz. \nMail adresi: halimdinc0@gmail.com**")

#Music Bot


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename


@bot.command(name='play_song', help='To play song')
async def play(ctx, url):

    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")


@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.event
async def on_ready():
    print('Running!')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if str(channel) == "general":
                await channel.send('Bot Activated..')
                await channel.send(file=discord.File('giphy.png'))
        print('Active in {}\n Member Count : {}'.format(guild.name, guild.member_count))


@bot.command(help="Prints details of Author")
async def whats_my_name(ctx):
    await ctx.send('Hello {}'.format(ctx.author.name))


@bot.command(help="Prints details of Server")
async def where_am_i(ctx):
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc = ctx.guild.description

    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members = []
    async for member in ctx.guild.fetch_members(limit=150):
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name, str(member.status),
                                                                       str(member.joined_at)))


@bot.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if str(channel) == "general":
            on_mobile = False
            if member.is_on_mobile() == True:
                on_mobile = True
            await channel.send("Welcome to the Server {}!!\n On Mobile : {}".format(member.name, on_mobile))

        # TODO : Filter out swear words from messages


@bot.command()
async def tell_me_about_yourself(ctx):
    text = "My name is WallE!\n I was built by Kakarot2000. At present I have limited features(find out more by typing !help)\n :)"
    await ctx.send(text)


@bot.event
async def on_message(message):
    # bot.process_commands(msg) is a couroutine that must be called here since we are overriding the on_message event
    await bot.process_commands(message)
    if str(message.content).lower() == "hello":
        await message.channel.send('Hi!')

    if str(message.content).lower() in ['swear_word1', 'swear_word2']:
        await message.channel.purge(limit=1)









"""# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


# command to play sound from a youtube URL
@bot.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return


# command to resume voice if it is paused
@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


# command to pause voice if it is playing
@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


# command to stop voice
@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')

"""


bot.run(TOKEN)

