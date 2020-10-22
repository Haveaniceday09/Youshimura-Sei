import discord

client = discord.Client()

@client.event
async def on_ready():
	print('Успешно: {0.user}'.format(client))

@client.event
async def on_message(msg):
	if msg.author == client.user:
		return

	if msg.content.startswith('bot):
		await message.channel.send('ready')
			
client.run('NzY4MDU5OTA3MTgxNjQxNzM4.X469hw.SSyQCTYNRAUf7jYR80BfStpjsjk')
