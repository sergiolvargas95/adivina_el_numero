import random

numero_de_intentos = 1
numero_a_adivinar = random.randint(1, 10)

numero_usuario = int(input('Adivina un número entre el 1 y el 10: '))
while numero_usuario != numero_a_adivinar:
    print('¡No has acertado!')
    if numero_de_intentos == 4:
        break
    elif numero_usuario > numero_a_adivinar:
        print('tu número esta por encima del numero a adivinar')
    else: 
        print('Tu número está por debajo al número a adivinar')
    numero_usuario = int(input('por favor, intentalo de nuevo: '))
    numero_de_intentos += 1

if numero_usuario == numero_a_adivinar:
    print('!Bien hecho! Has adivinado.')
    print('Te ha tomado', numero_de_intentos, 'intentos para ganar el juego' )
else:
    print('Lo siento, has perdido.')
    print('el número de intentos que has tenido es', numero_de_intentos)
    print('el número era: ', numero_a_adivinar)
    print('Game Over')
