import discord
import os
import requests
import json





client = discord.Client()
in_testing = 'This program is currently in testing, but we appreciate your patience'

sad_words = ["sad", "depressed", "suicide", "unhappy", "upset"]

starter_encouragements = [
  "Give up",
  "You don't matter",
  "I would curse at you, but censor bot doesn't let me",
  "Stop whining",
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random/")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -' + json_data[0]['a']
  return(quote)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Greetings Mere Mortal')




@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))



inspire = '$inspire'
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == inspire:
    await message.channel.send(get_quote())

@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  if message.content.startswith('$bye'):
    await message.channel.send('Bye, come back soon!')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    pass
  if message.content.startswith('$getrole'):
    await message.channel.send(in_testing)



client.run(os.getenv('Token'))
