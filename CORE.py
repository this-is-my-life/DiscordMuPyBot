'''
	μPy! v6.0 Core. 
	---------------------
	PMH Studio / Proj- μBot | Smart & Cute Discord Bot_Mu~☆ 
	Copyright (c) 2018. PMH Studio / PMH. (kok4575@gmail.com) MIT Licensed.
	
	* Requests Node.js & Discord.js
'''

# Basic Imports__________________________________

# Get Environment Variable System Import
import os

# Discord API Import
import discord

# Discord API Commands Import
from discord.ext import commands

# Get Token______________________________________
	
# Get Token From Enviroment Variable or Text
muto = os.getenv("muto") or ' Token Here. Or Get Environment Variable '

# Bot Login______________________________________

# Get Bot Client
mu = commands.Bot(command_prefix = 'mp!')

# Bot Readying___________________________________
@mu.event
async def on_ready():
	print("-----------------------------------------------------------\n\n	μBot is Running Correctly! \n\nInput Log:")

# Bot Commanding__________________________________
@mu.event
async def on_message(input):

	# Input Checker
	iuser = input.author
	i = input.content
	itab = i.split()
	ichannel = input.channel
	
	if i.startswith('mp!') or i.startswith('뮤파!'):

		# Logging
		print('{}/{}> {}'.format(ichannel, iuser, i))

		if i.startswith('mp!ping') or i.startswith('mp!p'):
			await mu.send_message(ichannel, 'Pong')

		if i.startswith('뮤파!핑') or i.startswith('뮤파!핑크'):
			await mu.send_message(ichannel, '퐁!')

		if i.startswith('mp!say') or i.startswith('mp!s') or i.startswith('뮤파!말') or i.startswith('뮤파!말해줘'):
			output = ''
			for word in itab[1:]:
				output += word
				output += ' '
			await mu.send_message(ichannel, output)

		if i.startswith('mp!delete') or i.startswith('mp!d'):
			amount = 99
			for a in itab[1:]:
				amount = a
			if amount > 99:
				await mu.send_message(ichannel, 'MuPy Can Delete Less than 99 Message!')
			else:
				deletes = []
				async for input in mu.logs_from(ichannel, limit=int(amount) + 1):
					deletes.append(input)
				await mu.delete_messages(deletes)
				await mu.send_message(ichannel, 'Deleted!')

		if i.startswith('뮤파!삭') or i.startswith('뮤파!삭제'):
			amount = 99
			for a in itab[1:]:
				amount = a
			if amount > 99:
				await mu.send_message(ichannel, '뮤파이는 99개의 메세지까지 지울 수 있다뮤!')
			else:
				deletes = []
				async for input in mu.logs_from(ichannel, limit=int(amount) + 1):
					deletes.append(input)
				await mu.delete_messages(deletes)
				await mu.send_message(ichannel, '삭제 완료!')

		if i.startswith('뮤파!니코니코니'):
			role = discord.utils.get(iuser.server.roles, name='주갤주')
			await mu.add_roles(iuser, role)

''' When Message Deleted___________________________
@mu.event
async def on_message_delete(input):
	iuser = input.author
	i = input.content
	ichannel = input.channel
	await mu.send_message(ichannel, '\'{}\' Said \'{}\'\nBut, Deleted.'.format(iuser, i))
'''

# Bot Login with Token
mu.run(muto)
