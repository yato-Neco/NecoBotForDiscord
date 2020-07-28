# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import os
import sys

# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''
voice = None

# 接続に必要なオブジェクトを生成
client = discord.Client()
url = "https://youtu.be/nnBw3H7OBu4"
kaomozi_1 = "（´・ω・`）.;:…（´・ω...:.;::..（´・;::: .:.;: ｻﾗｻﾗ.."
botchannel = 637253650258984967


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

    if message.content == "<<help":
        await message.channel.send("```\n___コマンド一覧___\n<<neko--にゃーん\njoin or jn--bot入室\nleave or lv--退出\n<<down--bot停止\nYouTube_URL--音楽リクエスト\n<<askii_art--NecoBot\n```")

    if message.content == '<<anison':
        await message.channel.send(";;p " + url)

    if message.content == "<<askii_art":
        await message.channel.send("```" + askii_art1 + "```")

    if message.content == ("<<down"):
        channel = client.get_channel(botchannel)
        await channel.send("終了中～" + kaomozi_1)
        await client.logout()
        await sys.exit()

    if message.content.startswith("https://youtu.be/"):
        channel_txt = client.get_channel(637253650258984967)
        message.author = client.get_user(348386897795612672)
        await channel_txt.send(";;p " + message.content)

    if message.content.startswith("https://www.youtube.com/"):
        channel_txt = client.get_channel(637253650258984967)
        message.author = client.get_user(348386897795612672)
        await channel_txt.send(";;p " + message.content)



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


# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(botchannel)
    await channel.send('おはようっ!!')


# 起動時に動作する処理
@client.event
async def on_ready():
    print(askii_art1)
    print('Logged in as')
    print("ver-1.5")
    print(client.user.name)
    print(client.user.id)
    print('------')
    await greet()


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
