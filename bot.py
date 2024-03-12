import os
import random

import discord

from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guild_messages = True
client = discord.Client(intents=intents)
channel = None


@client.event
async def on_ready():
  #guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
  #even a better way is using the get() function
  global channel
  guild = discord.utils.get(client.guilds, name=GUILD)
  print(
      f'{client.user} has connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
  )
  channel = [str(channel) for channel in guild.channels]
  print(channel)
  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members: \n - {members}')

#send a message to welcome new users
@client.event
async def on_member_join(member: discord.Member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi {member.name}, welcome to my Discord server youngings!'
  )

@client.event
async def on_message(message: discord.Message):
  if message.author == client.user:
    return
  brooklyn_99_quotes = [
    'I\'m the human of the 100 emoji',
    'Bingpot!',
    (
      'Cool. cool cool cool cool cool, ',
      'no doubt no doubt no doubt no doubt.'
    )
  ]
  if message.content == '99!':
    response = random.choice(brooklyn_99_quotes)
    await message.channel.send(response)


client.run(TOKEN)
