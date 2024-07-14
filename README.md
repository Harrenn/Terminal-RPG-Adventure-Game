# Terminal RPG Adventure Game

Welcome to the Terminal RPG Adventure Game! This is a simple, text-based role-playing game where you battle against various creatures using basic moves like attack, block, and heal. The goal is to defeat the enemy before your health points (HP) drop to zero.

## How to Play

### Gameplay

1. **Character Creation**: The game starts with a pre-set hero and enemy.
   - Hero: $(\text{HP} = 30)$, $(\text{Attack Power} = 10)$
   - Goblin: $(\text{HP} = 20)$, $(\text{Attack Power} = 6)$

2. **Turns**: Each turn, you will be prompted to choose between three actions:
   - Attack: Deal damage to the enemy.
   - Block: Reduce incoming damage from the enemy's next attack.
   - Heal: Recover a small amount of HP.

3. **Enemy Actions**: The enemy will either attack or heal itself based on a random choice.

4. **Victory Conditions**: The game ends when either the player's or the enemy's HP drops to zero.
   - If the enemy's HP drops to zero, you win.
   - If your HP drops to zero, the game is over and you lose.

### Controls

During each turn, you will be given the following options:
- Type 1 to attack
- Type 2 to block
- Type 3 to heal

## Setup

### Requirements
- Python 3.x

### Running the Game
Save the script as `terminal_game.py` and run it in your terminal with the following command:
