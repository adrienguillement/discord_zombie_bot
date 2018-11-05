import discord
import os

from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    # Do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Zombies channel id
    if message.channel.id == '508933891671851028':
      
      # Voyage of despair
      if message.content.lower().startswith('voyage'):
          msg = 'Voyage of despair'
          await client.send_message(message.channel, msg)

      # IX
      if message.content.lower().startswith('ix'):
          msg = 'IX'
          await client.send_message(message.channel, msg)
      
      # Blood of the dead
      if message.content.lower().startswith('blood'):
          msg = 'Blood of the dead'
          await client.send_message(message.channel, msg)

    return

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

# Use https://uptimerobot.com to ping to no shutdown
