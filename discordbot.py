from datetime import datetime
import discord
from dotenv import load_dotenv
import aiocron
import random
import os

load_dotenv()

PREFIX = '!'  # os.environ['PREFIX']
TOKEN = 'MTA3NTA1NzM4NzYyMDI4MjM3OA.Gl5cZz.Zb_vEoSJAFH1_I8OlyCE5NNsSSjWZfw2T6eYnY'  # os.environ['TOKEN']

# Channel ID SET
ALERT_01 = '1080754352463036508'  # os.environ['ALERT_01']
ALERT_02 = '1080754352463036508'  # os.environ['ALERT_02']
ALERT_03 = '1080754352463036508'  # os.environ['ALERT_03']
ALERT_04 = '1080754352463036508'  # os.environ['ALERT_04']

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}.\n({datetime.now()})')


@client.event
async def on_member_join(member):
    await member.guild.get_channel(int(ALERT_03)) \
        .send(member.mention + "은(는) 동료가 되었다!!")


'''
Code to send a Discord notification message at a set time.

example
 @aiocron.crontab('20 17 * * *')

Runs repeatedly every 17:20 every day.
Time depends on server setting time.
'''

@aiocron.crontab('00 03 * * *', start=True)
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


@aiocron.crontab('00 03 * * 3', start=True)
async def alarm03():
    print(f'[{datetime.now()}] alert alarm 03')
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

    embed.add_field(name="👉 크롬 신청서 ", value="[작성하러 가기](https://bit.ly/3y4saSk)", inline=True)
    embed.set_footer(text="신규 밍고분들 크롬바스 스케줄로 다니실 분 크롬바스정보 게시판에서 최소 스펙 확인 후"
                          "\n위 링크 탭에서 '크롬보직' 과 '다음주' 스케줄표 작성요청 드립니다.")

    await channel.send(embed=embed)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
