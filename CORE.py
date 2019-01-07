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
status = ['mu!도움 | 한쿸어 지원!', 'mu!토스트 | 빵굽자!' , 'Type mu!help to HELP', 'Discord.js & Discord.py', 'Discord.Net 시범운영중!', 'Python + Node.js + .net Version', 'mu!도박 | 도박 시스탬!', '띠꺼우면 PMH Studio / PMH#0001', 'Open Source', 'github.com/PMHStudio/', 'mubotapi.dothome.co.kr/', 'pmhstudio.co.nf/', 'Created By PMH Studio', ' AI탑제! | mu!(하고싶은말)']
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

# Status Cycle Loop
mu.loop.create_task(change_status())

# Bot Login with Token
mu.run(muto)
