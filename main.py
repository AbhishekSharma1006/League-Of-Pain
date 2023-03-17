import discord
from webserver import keep_alive
import os
import classic
import ability

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('lolguess classic'):
        await classic.start_game(message, client)

    if message.content.startswith('lolguess ability'):
        await ability.start_game(message, client)

keep_alive()
client.run(os.getenv('discord_token'))