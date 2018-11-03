import os
import discord
from discord.ext import commands

muto = os.getenv("muto")

mu = commands.Bot(command_prefix = 'mp!')

@mu.event
async def on_ready():
	print('MuPy is Here');

mu.run(muto)
