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
mu = commands.Bot()

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

	# Logging
	print('{}/{}> {}'.format(ichannel, iuser, i))

	if i.startwith('mp!ping') or i.startwith('mp!p'):
		await mu.send_message(channel, 'Pong')

	if i.startwith('뮤파!핑') or i.startwith('뮤파!핑크'):
		await mu.send_message(channel, '퐁!')

	if i.startwith('mp!say') or i.startwith('mp!s') or i.startwith('뮤파!말') or i.startwith('뮤파!말해줘'):
		output = ''
		for word in itab[1:]:
			output += word
			output += ' '
		await mu.send_message(channel, output)

# When Message Deleted___________________________
@mu.event
async def on_message_delete(input):
	iuser = input.author
	i = input.content
	ichannel = input.channel
	await client.send_message(channel, '\'{}\' Said \'{}\'\nBut, Deleted.'.format(iuser, i))

# Bot Login with Token
mu.run(muto)
