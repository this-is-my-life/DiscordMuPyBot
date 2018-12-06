# Basic Imports__________________________________

# Get Environment Variable System Import
import os

# Discord API Import
import discord

# Discord API Commands Import
from discord.ext import commands

# Async Io Import
import asyncio

# Cycle Import
from itertools import cycle

# Get Token______________________________________

# Get Token From Enviroment Variable or Text
muto = os.getenv("muto") or ' Token Here. Or Get Environment Variable '

# Bot Login______________________________________

# Get Bot Client
mu = commands.Bot(command_prefix = 'mu!')

# Bot Status Cycle
status = ['mu!도움 | 한쿸어 지원!', 'Type mu!help to HELP', 'Discord.js & Discord.py', 'Python + Node.js Version', '띠꺼우면 PMH Studio / PMH#2454', 'Open Source', 'github.com/PMHStudio/', 'mubotapi.dothome.co.kr/', 'pmhstudio.co.nf/', 'Created By PMH Studio', ' AI탑제! | mu!(하고싶은말)']
async def change_status():
	await mu.wait_until_ready()
	msgs = cycle(status)

	while not mu.is_closed:
		current_status = next(msgs)
		await mu.change_presence(game=discord.Game(name=current_status))
		await asyncio.sleep(3)

# Bot Readying___________________________________
@mu.event
async def on_ready():
	print("-----------------------------------------------------------\n\n	μBot is Running Correctly! \n\nInput Log:")

# Bot Cooldown___________________________________
@commands.cooldown(1, 30, commands.BucketType.user)

# Bot Commanding__________________________________
@mu.event
async def on_message(imsg):

	# Input Checker
	iuser = imsg.author
	i = imsg.content
	itab = i.split()
	ichannel = imsg.channel
	iserver = imsg.server
	
	if i.startswith('mu!'):

		# Logging
		print('{}/{}> {}'.format(ichannel, iuser, i))

		if i.startswith('mu!delete') or i.startswith('mu!d'):
			amount = 1
			for a in itab[1:]:
				amount = a
			if int(amount) > 99:
				await mu.send_message(ichannel, 'Mu Can Delete Less than 99 Message!')
			else:
				deletes = []
				async for imsg in mu.logs_from(ichannel, limit=int(amount) + 1):
					deletes.append(imsg)
				await mu.delete_messages(deletes)
				await mu.send_message(ichannel, 'Deleted {} Messages By \'{}\'!'.format(amount, iuser))

		if i.startswith('mu!삭'):
			amount = 1
			for a in itab[1:]:
				amount = a
			if int(amount) > 99:
				await mu.send_message(ichannel, '뮤는 99개의 메시지까지 지울 수 있다뮤!')
			else:
				deletes = []
				async for imsg in mu.logs_from(ichannel, limit=int(amount) + 1):
					deletes.append(imsg)
				await mu.delete_messages(deletes)
				await mu.send_message(ichannel, '\'{}\'의 요청으로\n{}개의 메시지 삭제 완료!'.format(iuser, amount))

		if i.startswith('mu!닉') or i.startswith('mu!nick'):
			output = ''
			for word in itab[1:]:
				output += word
				output += ' '
			await mu.change_nickname(iserver.me, output)
			await mu.send_message(ichannel, '\'{}\'의 요청으로\n\'{}\'로 닉변완료!'.format(iuser, output))


# Status Cycle Loop
mu.loop.create_task(change_status())

# Bot Login with Token
mu.run(muto)
