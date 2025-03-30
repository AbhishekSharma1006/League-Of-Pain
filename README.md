# Loldle Discord Bot

A Python-based Discord bot that simulates the game of **Loldle**, a Wordle-inspired guessing game for **League of Legends** champions. Players can test their knowledge by guessing champions based on given hints.

## Features
- **Classic Mode**: Users receive hints about a random champion and try to guess their identity.
- **Ability Mode**: Users must identify the champion that the ability icon belongs to.
- **Dynamic Hint Updates**: Hints update as players continue guessing.
- **Interactive Commands**: Users can start a game and submit guesses using simple Discord commands.

## Usage
### Commands
| Command | Description |
|---------|-------------|
| `lolguess classic` | Starts a classic mode game |
| `lolguess ability` | Starts an ability mode game |
| `guess <champion_name>` | Submits a guess |

### Example Gameplay
```
User:
lolguess classic
Bot:
Starting new game - classic
Please type in your guess below:

User:
guess Morgana
Bot:
+ RANGED
+ MANA
+ MAGIC_DAMAGE
- DEMACIA
X

User:
guess Zair
Bot:
Not a champion, please make sure that spaces and special symbols, if any, are correct.

User:
guess Azir
Bot:
+ RANGED
+ MANA
+ MAGIC_DAMAGE
+ SHURIMA
✓
You got it! Number of attempts: 3
```

```
User:
lolguess ability
Bot:
Starting new game - ability
What champion has the following ability:
<ability-icon>

User:
guess Viego
Bot:
✓
You got it! Number of attempts: 1
```

## Contributing
Contributions are welcome! If you'd like to improve the bot or add new features, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, reach out via GitHub Issues.
