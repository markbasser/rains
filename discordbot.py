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
    
    if now == '00:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone Mornin!Rain☔ is 1min later.<:good01:699581068285706301>51120671>')  
    
    if now == '00:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 200 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:JPYNdisco:698471276498649168>')  

    if now == '00:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:BGPT02:698471366004965406> ')

    if now == '00:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 300 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:benkeicoinsl:698471387064696833>')

    if now == '00:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 250 ActiveUserOnly  <:good01:699581068285706301><:gm:699792760651120671><:JPYNdisco:698471276498649168>')  
  
    if now == '03:38':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:heart02:699580174911668225>Okay,later👋')     

    if now == '01:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 30 3 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')

    if now == '02:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')

    if now == '03:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello:699779689127870514> Rain☔ is 1min later.<:good01:699581068285706301>✨')   
        
    if now == '03:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 1000 ActiveUserOnly  🌈 <:BGPT02:698471366004965406>') 
    
    if now == '03:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 777.77 ActiveUserOnly  🌈 <:BENKEICOIN04:698471407650209832> ')  

    if now == '03:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 333.3 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')    
    
    if now == '03:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain KENJ 1111.11 ActiveUserOnly  ☔<:kenj:700136543003607101>') 
            
    if now == '03:39':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 400 4 EquallyDistributed  <:JPYNdisco:698471276498649168>⚾Pls receive☞/catch')
    
    if now == '03:40':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here 👆/catch <:heart02:699580174911668225>See you later!🌟') 

    if now == '04:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  🌈 <:JPYNdisco:698471276498649168> ')   
        
    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
    
    if now == '05:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly  ☔<:kenj:700136543003607101>')
        
    if now == '06:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
    
    if now == '06:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 77.7 ActiveUserOnly  <:rain:699585875687899247><:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833>')   
   
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 30 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')
  
    if now == '07:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>Good morning everyone.<:gm:699792760651120671>Have a nice day today! [omikuji] or [Fortune] ← for today is fortune🔮')

    if now == '07:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 77.7 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406> ') 

    if now == '08:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 35 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168><:hello:699779689127870514>')
        
    if now == '09:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 40 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247> <:JPYNdisco:698471276498649168> ')
   
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:aloha:699581550777597992>Hello,how are you❓ ') 
      
    if now == '10:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:suika_paku:699072728153587782>After 1min, I”ll ☔Rain a little... ') 
    
    if now == '10:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 100 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:BGPT02:698471366004965406>') 
        
    if now == '10:33':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 80 4 EquallyDistributed  <:good01:699581068285706301><:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch')  

    if now == '10:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone 👆/catch <:heart02:699580174911668225>See you sometimes!<:star1:699582964853375018>')    
        
    if now == '11:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 200 ActiveUserOnly  ☔<:kenj:700136543003607101><:sangras01:699579409220370514>')
    
    if now == '12:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@everyone <:hello:699779689127870514>Rain<:rain:699585875687899247>is 1min later.<:good01:699581068285706301>')  

    if now == '12:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 200 ActiveUserOnly  <:rain:699585875687899247><:JPYNdisco:698471276498649168> ')

    if now == '12:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777.77 ActiveUserOnly  <:rain:699585875687899247><:BGPT02:698471366004965406>')

    if now == '12:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 500 ActiveUserOnly  <:rain:699585875687899247><:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833> ')

    if now == '12:36':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/throw JPYN 39 3 EquallyDistributed  <:JPYNdisco:698471276498649168> ⚾Pls receive☞/catch') 
   
    if now == '12:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(' 👆/catch ok?<:heart02:699580174911668225>see you!<:star1:699582964853375018>')  
        
    if now == '13:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here もうJapanでは22:00頃ですね。今日もあと少しだけRainします。30分後に！It is UTC/13:00. Hello!Rain☔ is 30min later. ')       
        
    if now == '13:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 77.7 ActiveUserOnly   <:rain:699585875687899247><:good:699580636448423936> <:JPYNdisco:698471276498649168>')
    
    if now == '13:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 300 ActiveUserOnly  <:rain:699585875687899247><:good:699580636448423936> <:BENKEICOIN04:698471407650209832><:benkeicoinsl:698471387064696833> ')
    
    if now == '13:35':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 777.77 ActiveUserOnly  <:rain:699585875687899247><:BGPT02:698471366004965406>')
    
    if now == '13:37':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('@here <:zzz:699581950356226058><:gn:699792795363311676> 日本のみんなはそろそろおやすみなさい！It is UTC/13:37. Hello!Rain☔ is 30min later👋 コロナには気を付けて！<:corona:699588627868418070>Watch out for corona!→ #┃covid-19🦠news ')       
                
    if now == '14:47':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  <:good01:699581068285706301><:rain:699585875687899247><:JPYNdisco:698471276498649168><:gn:699792795363311676> ')  

    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 50 ActiveUserOnly  <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247><:gn:699792795363311676> ')

    if now == '19:05':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 10 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168><:rain:699585875687899247>')
    
    if now == '18:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain kenj 50 ActiveUserOnly  ☔<:kenj:700136543003607101><:DISCO:699373482240245892>')
    
    if now == '19:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BEN 5 ActiveUserOnly  <:BENKEICOIN04:698471407650209832><:good01:699581068285706301><:rain:699585875687899247> ')  

    if now == '21:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain BGPT 50 ActiveUserOnly  <:good01:699581068285706301><:BGPT02:698471366004965406> <:rain:699585875687899247>')

    if now == '22:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')
   
    if now == '22:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('Japan <:cafe:699769671234355230> みなさん🌟おはようございます。<:gm:699792760651120671> 今日も良い一日を！【おみくじ】←で運勢をどうぞ')

    if now == '23:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')        
        
    if now == '23:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/rain JPYN 20 ActiveUserOnly  <:good01:699581068285706301>🌈<:JPYNdisco:698471276498649168>HelloAll⭐')
  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
