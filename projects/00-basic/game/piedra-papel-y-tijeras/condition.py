def condition(player,pc):
    if player == pc:
        print('Computadora: ', pc)
        print('Es un empate!')
    elif player == 'papel':
        if pc == 'tijera':
            print('Computadora: ', pc)
            print('Perdiste!')
        if pc == 'piedra':
            print('Computadora: ', pc)
            print('Ganaste!')
    elif player == 'piedra':
        if pc == 'tijera':
            print('Computadora: ', pc)
            print('Ganaste!')
        if pc == 'papel':
            print('Computadora: ', pc)
            print('Perdiste!')
    elif player == 'tijera':
        if pc == 'piedra':
            print('Computadora: ', pc)
            print('Perdiste!')
        if pc == 'papel':
            print('Computadora: ', pc)
            print('Ganaste!')
