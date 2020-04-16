from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =698653628176531478  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '00:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly <:good01:699581068285706301><:JPYNdisco:698471276498649168> <:gm:699792760651120671> ')  

    if now == '00:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 100 ActiveUserOnly <:good01:699581068285706301><:BGPT02:698471366004965406> <:gm:699792760651120671> ')

    if now == '00:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 50 ActiveUserOnly <:good01:699581068285706301><:BENKEICOIN04:698471407650209832><:gm:699792760651120671> ')

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 30 3 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')

    if now == '02:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly 🌈 <:JPYNdisco:698471276498649168> ')

    if now == '03:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 70 ActiveUserOnly 🌈 <:BGPT02:698471366004965406>') 
    
    if now == '03:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 50 ActiveUserOnly  🌈 <:BENKEICOIN04:698471407650209832> ')  

    if now == '03:49':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 40 4 EquallyDistributed <:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')

    if now == '06:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly ☔<:kenj:700136543003607101> ')

    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 50 ActiveUserOnly ☔<:JPYNdisco:698471276498649168> ')

    if now == '09:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 50 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247> <:JPYNdisco:698471276498649168> ')

    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 100 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406> ') 
        
    if now == '10:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 40 4 EquallyDistributed <:good01:699581068285706301><:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch')  

    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly ☔<:kenj:700136543003607101><:sangras01:699579409220370514> ')

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')

    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly <:rain:699585875687899247><:BGPT02:698471366004965406>')

    if now == '12:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 100 ActiveUserOnly <:rain:699585875687899247><:BENKEICOIN04:698471407650209832> ')

    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 30 3 EquallyDistributed <:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch') 
        
    if now == '14:45':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly <:good01:699581068285706301><:rain:699585875687899247><:JPYNdisco:698471276498649168><:gn:699792795363311676> ')  

    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247><:gn:699792795363311676> ')

    if now == '19:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 50 ActiveUserOnly <:good01:699581068285706301>🌈 <:JPYNdisco:698471276498649168><:rain:699585875687899247>')
        
        

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
