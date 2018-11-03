import system
import discord
from discord.ext import commands

muto = System.getenv("muto")

mu = commnads.Bot(command_prefix = 'mp!')

@mu.event
async def on_ready():
	print('MuPy is Here');

mu.run(muto)
