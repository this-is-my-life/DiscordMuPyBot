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
	itab = input.content.split()
	ichannel = input.channel

	# Logging
	print('{}/{}> {}'.format(ichannel, iuser, input.content))

	if input.content.startwith('mp!ping') or input.content.startwith('mp!p'):
		await mu.send_message(channel, 'Pong')

	if input.content.startwith('뮤파!핑') or input.content.startwith('뮤파!핑크'):
		await mu.send_message(channel, '퐁!')

	if input.content.startwith('mp!say') or input.content.startwith('mp!s') or input.content.startwith('뮤파!말') or input.content.startwith('뮤파!말해줘'):
		output = ''
		for word in itab[1:]:
			output += word
			output += ' '
		await mu.send_message(channel, output)

# When Message Deleted___________________________
@mu.event
async def on_message_delete(input):
	iuser = input.author
	ichannel = input.channel
	await mu.send_message(channel, '\'{}\' Said \'{}\'\nBut, Deleted.'.format(iuser, input.content))

# Bot Login with Token
mu.run(muto)
