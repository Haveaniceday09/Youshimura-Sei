#CREATING BOT LOGS
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
#IMPORT LIBRARYES
import random
import discord
import json
import asyncio
import requests
#IMPORT WTF??
from urllib.request import urlopen
from discord.ext import commands
#VARS
client = commands.Bot (command_prefix = '/')
msgl = ['react','bot','stat','stats','бот','статистика','ping','пинг']
CLEAR_MESSAGE_LIMIT = 50
#BOT BEGINNING


@client.event #Console ready display
async def on_ready():
	print('Успешно: {0.user}'.format(client))
	await client.change_presence(activity = discord.Game(name = 'Minecraft'))

@client.command(pass_context = True) #A short-about command
async def о_себе(ctx):
		embed=discord.Embed(title="Информация", url="https://discord.gg/A7CCzU", description="•Моя первая попытка создать что-то на Python•", color=0xaf0fdb)
		embed.set_author(name="Have a nice day", url="", icon_url="https://sun1.48276.userapi.com/uvJAGlAxgu3NPtFeUKWOrOR16hZnuRpMkIbyZw/C0QG4oymgs4.jpg")
		embed.set_thumbnail(url="https://psv4.userapi.com/c856220/u205636037/docs/d12/f7e7af6fd200/wpF7rgpJrcM.jpg?extra=vW1K0cZGZyJEljE2_kj017dluJ0EKVQUx_1MDKH3IMtG0KSWOHONi7HLZQ01J7dFo2pPuyV7o7Osbg3b3xwl5rYowyyth8pX8QtIkXv37FcvlswzOrEQDAcZoNklsK1JyIvckxf0lJUysblWRKQ0FOVBpA")
		await ctx.channel.send(embed=embed)

@client.command(pass_context = True) #Links for learning py and codding bot
async def py_links(ctx):
		embed=discord.Embed(title="Основная информация и полезные ссылки по созданию бота на Python", color=0x2954ff)
		embed.add_field(name="Documentation", value="https://discordpy.readthedocs.io/en/latest/", inline=False)
		embed.add_field(name="Video guide", value="https://www.youtube.com/watch?v=giebaN7jE4I", inline=False)
		embed.add_field(name="Discord developer portal", value="https://discord.com/developers/applications/768928657900830760/information", inline=False)
		embed.set_footer(text="====================================================================")
		await ctx.channel.send(embed=embed)

@client.event #Check ping
async def on_message(message):
		msgc = message.content.lower()
		author = message.author
		await client.process_commands(message)
		if msgc in msgl:
			await message.channel.send(f'{author.mention}')

@client.command(pass_context = True) #Message clearing
async def clear(ctx, *args):
	if len(args) <= 0:
		await ctx.channel.send('Укажите количество сообщений для удаления "/clear #" ')
		return
	amount = int(args[0])
	if amount > 0:
		await ctx.channel.purge(limit=min(CLEAR_MESSAGE_LIMIT, amount))

@client.command(pass_context = True) #Reloading bot?
async def reload(ctx, *args):
	print('Reloaded')
	await connect(reconnect=True)

token = open('token.txt', 'r').readline()
client.run(token)
