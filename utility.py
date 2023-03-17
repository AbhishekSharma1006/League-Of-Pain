import random

def get_random_champion(champions):
  size = len(champions)
  index = random.randint(0, size-1)
  current_champion = list(champions.values())[index]
  return current_champion

def get_champion(champions, champion_name):
  for v in champions.values():
    if v["name"].lower() == champion_name.lower():
      return v
  return champions[champion_name]

async def show_match(guessed_champion, current_champion, channel):
  await print_property(guessed_champion, current_champion, channel, "name")
  await print_property(guessed_champion, current_champion, channel, "attackType")
  await print_property(guessed_champion, current_champion, channel, "resource")
  await print_property(guessed_champion, current_champion, channel, "adaptiveType")
  await print_property(guessed_champion, current_champion, channel, "faction")

async def print_property(guessed_champion, current_champion, channel, property):
  if(guessed_champion[property] == current_champion[property]):
    await print_positive(channel, guessed_champion[property].upper())
  else:
    await print_negative(channel, guessed_champion[property].upper())

async def print_positive(channel, message):
  await channel.send(f"```diff\n+ {message}\n```")

async def print_negative(channel, message):
  await channel.send(f"```diff\n- {message}\n```")