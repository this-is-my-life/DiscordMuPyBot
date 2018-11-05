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

# Bot Logging_____________________________________
@mu.event
async def on_message(input):

	# Input Checker
	iuser = input.author
	i = input.content
	ichannel = input.channel

	# Logging
	print('{}/{}> {}'.format(ichannel, iuser, i))

# Bot Commanding__________________________________
	await mu.process_commands(input)

@mu.command()
async def ping():
	await mu.say('Pong!')

@mu.command
async def say(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await mu.say(output)

# When Message Deleted___________________________
@mu.event
async def on_message_delete(input):
	iuser = input.author
	i = input.content
	ichannel = input.channel
	await client.send_message(channel, '\'{}\' Said \'{}\'\nBut, Deleted.'.format(iuser, i))

# Bot Login with Token
mu.run(muto)
