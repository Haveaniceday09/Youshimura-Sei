import discord

client = discord.Client()

@client.event
async def on_ready():
	print('Успешно: {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('ти кто'):
		await message.channel.send('я дима)')
			
client.run('NzY4MDU5OTA3MTgxNjQxNzM4.X469hw.SSyQCTYNRAUf7jYR80BfStpjsjk')
