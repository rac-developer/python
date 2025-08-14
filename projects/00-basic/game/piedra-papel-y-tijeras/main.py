
import random
from condition import condition

list = ['piedra', 'papel', 'tijera']


while True:
    player = None
    pc = random.choice(list)

    while player not in list:
        player = input('piedra, papel, tijera?: ').lower()

    condition(player, pc)

    again = ['si','no']
    new_game = None

    while new_game not in again:
        new_game = input('Quieres jugar de nuevo? (si/no): ').lower()

    if new_game == 'no':
        break

print('Gracias por jugar!')