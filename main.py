# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import os
import sys, traceback

# 自分のBotのアクセストークンに置き換えてください
TOKEN = "NzM0MDExNjY2Nzg1ODk0NDUx.XxLfog.c_HZjCQBJkaxprF7Y0V7wDBIE8U"
#TOKEN = os.environ["DISCORD_BOT_TOKEN"]
voice = None

# 接続に必要なオブジェクトを生成
client = discord.Client()
url = "https://youtu.be/nnBw3H7OBu4"
kaomozi_1 = "（´・ω・`）.;:…（´・ω...:.;::..（´・;::: .:.;: ｻﾗｻﾗ.."
botchannel = 637253650258984967
channelmusic_id = 740892276154171402



askii_art1 = "\n  _   _                ____        _   \n | \ | |              |  _ \      | |  \n |  \| | ___  ___ ___ | |_) | ___ | |_ \n | . ` |/ _ \/ __/ _ \|  _ < / _ \| __|\n | |\  |  __| (_| (_) | |_) | (_) | |_ \n |_| \_|\___|\___\___/|____/ \___/ \__|\n"

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '<<neko':
        await message.channel.send('にゃーん')

    if message.content == '太郎':
        message.author = client.get_user(533256175123300393)
        mention = message.author.mention
        await message.channel.send(mention + 'fate')

    if message.content == "<<help":
        await message.channel.send("```\n___コマンド一覧___\n<<neko--にゃーん\n太郎--太郎にメンション\njoin or jn--bot入室\nleave or lv--退出\n<<down--bot停止\nYouTube_URL--音楽リクエスト\n<<askii_art--NecoBot\n```")

    if message.content == '<<anison':
        await message.channel.send(";;p " + url)

    if message.content == "<<askii_art":
        await message.channel.send("```" + askii_art1 + "```")

    if message.content == ("<<down"):
        if message.author.guild_permissions.administrator:
            channel = client.get_channel(botchannel)
            await channel.send("終了中～" + kaomozi_1)
            await client.logout()
            await sys.exit()
        else:
            await message.channel.send("あたに権限がありません")

    if message.content.startswith("https://youtu.be/"):
        if message.channel.id == channelmusic_id:
            channel = [message.id for message in message.author.voice.channel.members]
            if (client.user.id in channel):
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
            else:
                voice_state = message.author.voice
                channel = voice_state.channel
                await channel.connect()
                print("connected to:",channel.name)
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
        else:
            channelm = client.get_channel(740892276154171402)
            embed = discord.Embed(description="音楽のリクエストは" + channelm.mention + "ここへ", color=0x2e3cff)
            await message.channel.send(embed=embed)
            
    if message.content.startswith("https://www.youtube.com/"):
        if message.channel.id == channelmusic_id:
            channel = [message.id for message in message.author.voice.channel.members]
            if (client.user.id in channel):
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
            else:
                voice_state = message.author.voice
                channel = voice_state.channel
                await channel.connect()
                print("connected to:",channel.name)
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
        else:
            channelm = client.get_channel(740892276154171402)
            embed = discord.Embed(description="音楽のリクエストは" + channelm.mention + "ここへ", color=0x2e3cff)
            await message.channel.send(embed=embed)

    if message.content.startswith("https://m.youtube.com/"):
        if message.channel.id == channelmusic_id:
            channel = [message.id for message in message.author.voice.channel.members]
            if (client.user.id in channel):
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
            else:
                voice_state = message.author.voice
                channel = voice_state.channel
                await channel.connect()
                print("connected to:",channel.name)
                channel_txt = client.get_channel(637253650258984967)
                message.author = client.get_user(348386897795612672)
                await channel_txt.send(";;p " + message.content)
        else:
            channelm = client.get_channel(740892276154171402)
            embed = discord.Embed(description="音楽のリクエストは" + channelm.mention + "ここへ", color=0x2e3cff)
            await message.channel.send(embed=embed)

    if message.content == ("join") or message.content == ("jn"):
        voice_state = message.author.voice
        if (not voice_state) or (not voice_state.channel):
            await message.channel.send("先にボイスチャンネルに入っている必要があります。")
            return

        channel = voice_state.channel

        await channel.connect()
        print("connected to:",channel.name)


    if message.content == ("leave") or message.content == ("lv"):
        voice_client = message.guild.voice_client

        if not voice_client:
            await message.channel.send("Botはこのサーバーのボイスチャンネルに参加していません。")
            return

        await voice_client.disconnect()
        await message.channel.send("ボイスチャンネルから切断しました。")

    


@client.event
async def on_vc_start(member,channel):
    print(f"{member.name}が{channel.name}でボイスチャットを開始しました。")


@client.event
async def on_vc_end(member,channel):
    print(f"{member.name}が{channel.name}のボイスチャットを終了しました。")
    

@client.event
async def on_voice_state_update(member,before,after):
    if before.channel != after.channel:
        # before.channelとafter.channelが異なるなら入退室
        if after.channel and len(after.channel.members) == 1:
            # もし、ボイスチャットが開始されたら
            print("a")
            client.dispatch("vc_start",member,after.channel) #発火！

        if before.channel and len(before.channel.members) == 0:
            # もし、ボイスチャットが終了したら
            print("b")
            await member.guild.voice_client.disconnect()
            client.dispatch("vc_end",member,before.channel) #発火！
# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(botchannel)
    await channel.send('おはようっ!!')


# 起動時に動作する処理
@client.event
async def on_ready():
    print(askii_art1)
    print('Logged in as')
    print("ver-1.7")
    print(client.user.name)
    print(client.user.id)
    print('------')
    await greet()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
