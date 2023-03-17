import requests
import json
import utility
import asyncio

async def start_game(message, client):
  await message.channel.send('Starting new game - classic')
  response = requests.get("http://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions.json")
  champions = json.loads(response.text)
  current_champion = utility.get_random_champion(champions)
  print(current_champion["name"])
  await message.channel.send("Please type in your guess below:")
  guessCount = 0
  try:
    def check(m):
      return m.content.startswith('guess') and m.channel == message.channel and m.author == message.author
    guess = await client.wait_for('message', check=check, timeout=90.0)
    guessCount = 1
    guessed_champion = utility.get_champion(champions, guess.content[guess.content.find(' ')+1:])
    await utility.show_match(guessed_champion, current_champion, message.channel)
  except KeyError:
    await message.channel.send('Not a champion, please make sure that spaces and special symbols, if any, are correct.')
  except asyncio.TimeoutError:
    await message.channel.send('Timed out!')
    await message.channel.send(f"Excruciating defeat after {guessCount} tries!")
    return
  finally:
    while(guess.content[guess.content.find(' ')+1:].lower() != current_champion["name"].lower()):
      await message.channel.send(":x:")
      await message.channel.send("Please try again!")
      try:
        def check(m):
          return m.content.startswith('guess') and m.channel == message.channel
        guess = await client.wait_for('message', check=check, timeout=90.0)
        guessed_champion = utility.get_champion(champions, guess.content[guess.content.find(' ')+1:])
        await utility.show_match(guessed_champion, current_champion, message.channel)
      except KeyError:
        await message.channel.send('Not a champion, please make sure that spaces and special symbols, if any, are correct.')
      except asyncio.TimeoutError:
        await message.channel.send("Timed out!")
        await message.channel.send(f"Excruciating defeat after {guessCount} tries!")
        return
      finally:
        guessCount = guessCount+1
    await message.channel.send(":white_check_mark:")
    await message.channel.send(f"You got it! Number of attempts: {guessCount}")