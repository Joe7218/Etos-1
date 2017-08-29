import discord
import asyncio

client = discord.Client()

client.event
async def on_ready():  
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')




@client.event
async def on_message(message):  
	# Per the discord.py docs this is to not have the bot respond to itself
	if message.author == client.user:
		return
	#If the bot sees the command !hello we will respond with our msg string
	if message.content.startswith('.hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('.twat'):
		zevsmsg = 'Did you mean <@!173547110388465664>'
		await client.send_message(message.channel, zevsmsg)
	if message.content.startswith('.retarded'):
		prsmsg = 'Did you mean <@188952933323243520>'
	if message.content.startswith(message.server.me.mention):
		prefixmsg = 'The prefix for this server is .'
		
	


client.run('MzUwMDg5MjMwNTEwMzI1Nzgw.DIJFgA.qv4QopLej0r24wME64W4vbIppX0')
