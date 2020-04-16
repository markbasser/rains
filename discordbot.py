#coding:UTF-8
import os
import traceback
import discord
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID
client = discord.Client()  # 接続に使用するオブジェクト


@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


@client.event
# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '09:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly <:good01:699581068285706301><:JPYNdisco:698471276498649168> <:gm:699792760651120671> ')  

    if now == '09:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 100 ActiveUserOnly <:good01:699581068285706301><:BGPT02:698471366004965406> <:gm:699792760651120671> ')

    if now == '09:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 20 ActiveUserOnly <:good01:699581068285706301><:BENKEICOIN04:698471407650209832><:gm:699792760651120671> ')

    if now == '09:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 15 3 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 6 ActiveUserOnly 🌈 <:JPYNdisco:698471276498649168> ')

    if now == '12:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly 🌈 <:BGPT02:698471366004965406>') 
    
    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 30 ActiveUserOnly  🌈 <:BENKEICOIN04:698471407650209832> ')  

    if now == '12:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 20 4 EquallyDistributed <:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')

    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 300 ActiveUserOnly ☔<:kenj:700136543003607101> ')

    if now == '16:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly ☔<:JPYNdisco:698471276498649168> ')

    if now == '18:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 25 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247> <:JPYNdisco:698471276498649168> ')

    if now == '18:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406> ') 
        
    if now == '18:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 24 4 EquallyDistributed <:good01:699581068285706301><:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch')  

    if now == '20:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 321 ActiveUserOnly ☔<:kenj:700136543003607101><:sangras01:699579409220370514> ')

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')

    if now == '21:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 170 ActiveUserOnly <:rain:699585875687899247><:BGPT02:698471366004965406>')

    if now == '21:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 20 ActiveUserOnly <:rain:699585875687899247><:BENKEICOIN04:698471407650209832> ')

    if now == '21:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 24 3 EquallyDistributed <:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch') 
        
    if now == '00:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 25 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247><:JPYNdisco:698471276498649168><:gn:699792795363311676> ')  

    if now == '00:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247><:gn:699792795363311676> ')

    if now == '15:55':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly <:good01:699581068285706301>🌈 <:JPYNdisco:698471276498649168><:rain:699585875687899247>')
        
        

#ループ処理実行
loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(token)
