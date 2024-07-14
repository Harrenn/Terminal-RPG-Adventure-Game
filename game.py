import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.hp -= damage
        return damage

    def heal(self):
        heal_amount = random.randint(1, 8)
        self.hp += heal_amount
        return heal_amount

def player_turn(player, enemy):
    print(f"\nYour HP: {player.hp}")
    print(f"{enemy.name} HP: {enemy.hp}")
    print("1. Attack")
    print("2. Block")
    print("3. Heal")

    choice = input("Choose an action: ")
    if choice == '1':
        damage = player.attack(enemy)
        print(f"You attacked {enemy.name} and dealt {damage} damage.")
    elif choice == '2':
        print("You block and reduce incoming damage.")
    elif choice == '3':
        heal_amount = player.heal()
        print(f"You heal yourself for {heal_amount} HP.")
    else:
        print("Invalid choice. You lose your turn.")

def enemy_turn(enemy, player):
    action = random.choice(['attack', 'attack', 'heal'])
    if action == 'attack':
        damage = enemy.attack(player)
        print(f"{enemy.name} attacked you and dealt {damage} damage!")
    elif action == 'heal':
        heal_amount = enemy.heal()
        print(f"{enemy.name} heals itself for {heal_amount} HP.")

def game():
    player = Character("Hero", 30, 10)
    enemy = Character("Goblin", 20, 6)

    print("Welcome to the RPG Adventure!")
    print("A wild Goblin has appeared!")

    while player.hp > 0 and enemy.hp > 0:
        player_turn(player, enemy)
        if enemy.hp <= 0:
            print(f"\n{enemy.name} has been defeated! You win!")
            break
        enemy_turn(enemy, player)
        if player.hp <= 0:
            print("\nYou have been defeated by the Goblin. Game Over!")
            break

if __name__ == "__main__":
    game()
