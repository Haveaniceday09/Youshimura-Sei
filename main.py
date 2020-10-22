import discord
from discord.ext import commands

client = commands.Bot (command_prefix = '/')

msgl = ['react','bot','stat','stats','бот','статистика','ping','пинг']
CLEAR_MESSAGE_LIMIT = 50

@client.event

async def on_ready():
	print('Успешно: {0.user}'.format(client))

@client.command(pass_context = True)
async def о_себе(ctx):
		embed=discord.Embed(title="Информация", url="https://discord.gg/A7CCzU", description="•Моя первая попытка создать что-то на Python•", color=0xaf0fdb)
		embed.set_author(name="BlackSky9", url="", icon_url="https://sun1.48276.userapi.com/uvJAGlAxgu3NPtFeUKWOrOR16hZnuRpMkIbyZw/C0QG4oymgs4.jpg")
		embed.set_thumbnail(url="https://psv4.userapi.com/c856220/u205636037/docs/d12/f7e7af6fd200/wpF7rgpJrcM.jpg?extra=vW1K0cZGZyJEljE2_kj017dluJ0EKVQUx_1MDKH3IMtG0KSWOHONi7HLZQ01J7dFo2pPuyV7o7Osbg3b3xwl5rYowyyth8pX8QtIkXv37FcvlswzOrEQDAcZoNklsK1JyIvckxf0lJUysblWRKQ0FOVBpA")
		await ctx.channel.send(embed=embed)

@client.event	
async def on_message(message):
		msgc = message.content.lower()
		author = message.author
		await client.process_commands(message)
		if msgc in msgl:
			await message.channel.send(f'{author.mention}')

@client.command(pass_context = True)
async def clear(ctx, *args):
    if len(args) <= 0:
        await ctx.channel.send('Укажите количество сообщений для удаления "/clear #" ')
        return
    amount = int(args[0])
    if amount > 0:
        await ctx.channel.purge(limit=min(CLEAR_MESSAGE_LIMIT, amount))
