import os
import random
from datetime import datetime

import aiocron
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

# Channel ID SET
ALERT_01 = os.environ['ALERT_01']
ALERT_02 = os.environ['ALERT_02']
ALERT_03 = os.environ['ALERT_03']
ALERT_04 = os.environ['ALERT_04']

intents = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=intents)

Glenn_Bearna_SAT = 0
Glenn_Bearna_SUN = 0

Glenn_Bearna_SAT_user = []
Glenn_Bearna_SUN_user = []

Glenn_Bearna_Alarm = ''


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.\n({datetime.now()})')


@client.event
async def on_member_join(member):
    await member.guild.get_channel(int(ALERT_03)) \
        .send(member.mention + "은(는) 동료가 되었다!!")


@client.event
async def on_raw_reaction_add(payload):
    global Glenn_Bearna_SAT
    global Glenn_Bearna_SUN

    if payload.message_id == Glenn_Bearna_Alarm:
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)

        if payload.emoji.name == "1️⃣":
            Glenn_Bearna_SAT = reaction.count
            if client.user.id != payload.user_id:
                Glenn_Bearna_SAT_user.append(payload.user_id)
        elif payload.emoji.name == "2️⃣":
            Glenn_Bearna_SUN = reaction.count
            if client.user.id != payload.user_id:
                Glenn_Bearna_SUN_user.append(payload.user_id)


@client.command(name="channel")
async def channel(ctx):
    index = random.randrange(1, 24)
    while True:
        if index == 11:
            index = random.randrange(1, 24)
            print('my index is failed')
        else:
            await ctx.channel.send(file=discord.File('fuckers.webp'))
            await ctx.channel.send("**아이쿠 손↗이↗ 미끄러졌네↘ **   \n\n내 선택은... " + str(index) + "채널이라네!!")
            break


'''
Code to send a Discord notification message at a set time.

example
 @aiocron.crontab('20 17 * * *')

Runs repeatedly every 17:20 every day.
Time depends on server setting time.
'''


@aiocron.crontab('00 01 * * *', start=True)
async def alarm01():
    print(f'[{datetime.now()}] alert alarm 01')
    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_01))

    index = random.randrange(1, 24)
    while True:
        if 10 < index < 16:
            index = random.randrange(1, 24)
            print('my index is failed')
        else:
            embed = discord.Embed(title="밍고 하시딤 모집 안내", description="밍고-봇 알람 ⏰", color=0xff0000)
            embed.add_field(name="⏱️ 오늘 딤 시간은?", value="오후 10시 00분!", inline=False)
            embed.add_field(name="🗺️ 오늘 딤 채널은?", value=str(index) + " 채널!", inline=False)
            embed.add_field(name="📌 오늘 딤 위치는?", value="항상 그 위치 😎", inline=False)
            embed.add_field(name="🚫 딤 차단 채널은?", value="11, 12, 13, 14, 15 채널! ", inline=False)
            embed.set_footer(text="내용 추가 및 기타 수정 문의는 '김비누'")

            await channel.send(embed=embed)
            break


@aiocron.crontab('30 12 * * *', start=True)
async def alarm02():
    print(f'[{datetime.now()}] alert alarm 02')
    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_01))
    messages = await channel.history(limit=1).flatten()

    total = 0

    for message in messages:
        x = message.content[0:2]
        if x.isdigit():
            total = int(x)

    if total >= 11:
        embed = discord.Embed(title="밍고 하시딤 시작 30분 전 안내", description="밍고-봇 알람 ⏰")
        embed.set_footer(text="내용 추가 및 기타 수정 문의는 '김비누'")
        await channel.send(embed=embed)
    else:
        embed = discord.Embed(title="밍고 하시딤 쫑 안내", description="밍고 딤이 쫑 났습니다...")
        embed.set_footer(text="내용 추가 및 기타 수정 문의는 '김비누'")
        await channel.send(embed=embed)


@aiocron.crontab('00 01 * * 2', start=True)
async def alarm04():
    print(f'[{datetime.now()}] alert alarm 04')
    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_02))

    embed = discord.Embed(title="크롬바스 스케줄 마감 안내", description="📢 필 독 안 내"
                                                              "\n\n* 인원이 많아진 관계로 스케줄 관리가 어렵게 되어 google sheet로 관리하게 되었습니다."
                                                              "\n* 참여하실 분들만 작성하시되, 이슈가 없을 경우 '이슈 없음' 이라 작성 부탁드립니다."
                                                              "\n* 크롬 스케줄 마감은 수요일 마감이며, 신청하지 않을 경우 제외 됩니다. 🙏🙏🙏 "
                                                              "\n* 매주 스케줄이 동일한 경우 '매주 동일'이라 작성해주시면 자동으로 다음주도 반영됩니다."
                                                              "\n\nP.S. 스케줄 제약이 많으면 원하는 릴수 보다 적어질 수 있습니다."
                                                              "\n\v\v\v\v\v\v\vex : Q. 10릴 하고 싶은데 토요일만 되요 "
                                                              "\n\v\v\v\v\v\v\v\v\v\v\v\v\vA. 센세,, 되겠습니까? 🤬 "
                                                              "\n\n\n")
    embed.set_footer(text="내용 추가 및 기타 수정 문의는 '김비누'")


'''
    Glenn-Bearna Recruit Alarm Setting
'''


# Glenn-Bearna Recruit alarm
@aiocron.crontab('00 01 * * 3', start=True)
async def glenn_bearna_recruit():
    print(f'[{datetime.now()}] (discord-bot by amiro) : Call Function Glenn Bearna Recruit')

    global Glenn_Bearna_Alarm

    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_04))

    embed = discord.Embed(title="글렌 베르나 파티 모집 안내 📢",
                          description=""
                                      "**우리.. 글렌 베르나.. 가볼까요?**\n"
                                      "밍고 길드,**글렌 베르나** 소풍 가요!\n\n\n"
                                      "👉 **글렌 베르나 신청 방법**\n\n"
                                      "아래 **이모지**로 신청해주세요!\n"
                                      "1️⃣`토요일` \v\v 2️⃣`일요일`\n"
                                      ""
                          )
    embed.set_thumbnail(url="https://pbs.twimg.com/media/FmvC3_lakAEc8ub?format=jpg&name=900x900")

    alarm = await channel.send(embed=embed)
    Glenn_Bearna_Alarm = alarm.id

    await alarm.add_reaction("1️⃣")
    await alarm.add_reaction("2️⃣")


# Glenn-Bearna start alarm on saturday
@aiocron.crontab('00 01 * * 6', start=True)
async def glenn_bearna_alarm_for_sat():
    print(f'[{datetime.now()}] (discord-bot by amiro) : Call Function Glenn Bearna Alarm On Saturday')

    global Glenn_Bearna_SAT
    global Glenn_Bearna_SAT_user

    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_04))

    total = Glenn_Bearna_SAT - 1

    if total > 0:
        mention = ''

        for user in Glenn_Bearna_SAT_user:
            text = "<@" + str(user) + "> "
            mention += text

        embed = discord.Embed(
            title="글렌 베르나, 시작 안내",
            description=""
                        f"**토요일엔 내가 득템러! 😎**\n"
                        f"글렌 베르나 **토요일** 🙌 \n\n"
                        f"{mention}"
        )

        await channel.send(embed=embed)


# Glenn-Bearna start alarm on sunday
@aiocron.crontab('00 01 * * 7', start=True)
async def glenn_bearna_alarm_for_sun():
    print(f'[{datetime.now()}] (discord-bot by amiro) : Call Function Glenn Bearna Alarm On Sunday')

    global Glenn_Bearna_SUN
    global Glenn_Bearna_SUN_user

    await client.wait_until_ready()

    channel = client.get_channel(int(ALERT_04))

    total = Glenn_Bearna_SUN - 1

    if total > 0:
        mention = ''

        for user in Glenn_Bearna_SUN_user:
            text = "<@" + str(user) + "> "
            mention += text

        embed = discord.Embed(
            title="글렌 베르나, 시작 안내",
            description=""
                        f"**일요일엔 내가 득템러! 😎**\n"
                        f"글렌 베르나 **일요일** 👋 \n\n"
                        f"{mention}"
        )

        await channel.send(embed=embed)


@aiocron.crontab('00 13 * * 7', start=True)
async def reset_all_alarm():
    print(f'[{datetime.now()}] (discord-bot by amiro) : Call Function Reset All Alarm')

    global Glenn_Bearna_Alarm
    global Glenn_Bearna_SAT
    global Glenn_Bearna_SAT_user
    global Glenn_Bearna_SUN
    global Glenn_Bearna_SUN_user

    Glenn_Bearna_Alarm = ''
    Glenn_Bearna_SAT = 0
    Glenn_Bearna_SAT_user = []
    Glenn_Bearna_SUN = 0
    Glenn_Bearna_SUN_user = []


'''
    Glenn-Bearna Recruit Alarm Setting
'''

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
