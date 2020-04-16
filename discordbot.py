#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN'] #トークン
CHANNEL_ID = os.environ['CHANNEL_ID']  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '09:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly :gm::rainbow::JPYNdisco:')  

    if now == '09:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 100 ActiveUserOnly :gm::rainbow::BGPT02:')

    if now == '09:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 20 ActiveUserOnly :gm::rainbow::BENKEICOIN04:')

    if now == '09:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 15 3 EquallyDistributed :JPYNdisco:⚾Pls receive☞/catch')

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 6 ActiveUserOnly :rainbow::JPYNdisco:')

    if now == '12:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly :rainbow::BGPT02:') 
    
    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 30 ActiveUserOnly :rainbow::BENKEICOIN04:')  

    if now == '12:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 20 4 EquallyDistributed :JPYNdisco:⚾Pls receive☞/catch')

    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 300 ActiveUserOnly ☔:kenj:')

    if now == '16:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 5 ActiveUserOnly ☔:JPYNdisco:')

    if now == '18:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 25 ActiveUserOnly :rainbow::rain::JPYNdisco:')

    if now == '18:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly :rainbow::rain::BGPT02:') 
        
    if now == '18:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 24 4 EquallyDistributed :JPYNdisco:⚾Pls receive☞/catch')  

    if now == '20:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 321 ActiveUserOnly ☔:kenj:')

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly :rainbow:☔:JPYNdisco:')

    if now == '21:31':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 170 ActiveUserOnly :rainbow:☔:BGPT02:')

    if now == '21:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 20 ActiveUserOnly :rainbow:☔:BENKEICOIN04:')

    if now == '21:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 24 3 EquallyDistributed :JPYNdisco:⚾Pls receive☞/catch') 
        
    if now == '00:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 25 ActiveUserOnly :rain::JPYNdisco::gn:')  

    if now == '00:31
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 150 ActiveUserOnly :rain::BGPT02::gn:')
          
    if now == '13:45
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 50 ActiveUserOnly :rain::BGPT02::gn:')
        
        

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
