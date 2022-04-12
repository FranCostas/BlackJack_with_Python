import random

# Creamos las cartas existentes en nuestro mazo
valorCartas = ['AS', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Los palos existentes
paloCartas = ['♦ Diamantes', '♠ Picas', '♥ Corazones', '♣ Tréboles']


def repartirCarta():
    # Elegimos una carta y un palo aleatorio, le damos un valor numérico según la carta y retornamos una lista con la carta, valor y palo

    # Elegimos una carta y un palo aleatorio
    carta = random.choice(list(valorCartas))
    palo = random.choice(paloCartas)
    
    # Le damos un valor numérico según la carta
    if carta == 'J' or carta == 'Q' or carta == 'K':
        valor = 10
    elif carta == 'AS':
        valor = 999
    else:
        valor = int(carta)

    # Retornamos una lista con la carta, valor y palo
    return [carta, valor, palo]


def sacarValorCartas(lista):
    # Esta función saca el valor de la sumatoria de las cartas
    valorJugador = 0
    for x in lista:
        valorJugador += x[1]

    return valorJugador


def decidirAsJugador(cartasJugador):
    # Esta funcion sirve para que el usuario elija el valor de su AS
    for x in cartasJugador:
        if (x[0] == 'AS' and x[1] == 999):
            valorAS = 0
            while valorAS != 1 and valorAS != 11:
                valorAS = int(input('Vaya suerte! Te tocó un AS, elije su valor (11/1): '))
            #return 
            print(f'Excelente decisión, ahora tu AS de {x[2]} valdrá {valorAS}')
            x[1] = valorAS


def jugarBlackJack():
    opciones = None
    ciclo = None
    #    
    cartasJugador = []
    apuestaJugador = 0
    seguroJugador = None
    #
    cartasCrupier = []

    # Repartimos las cartas iniciales
    cartasJugador.append(repartirCarta())
    cartasCrupier.append(repartirCarta())
    cartasJugador.append(repartirCarta())
    cartasCrupier.append(repartirCarta())

    ######################################################################################
    # Comprobar blackJack
    #cartasJugador[0] = ['K', 10, '♥ Corazones']
    #cartasJugador[1] = ['AS', 999, '♥ Corazones']
    #cartasCrupier[0] = ['AS', 999, '♥ Corazones'] # Le da as al crupier
    #cartasCrupier[1] = ['K', 10, '♥ Corazones'] # 
    ######################################################################################

    cartasCrupier[0][1] = 11 if cartasCrupier[0][0] == 'AS' else cartasCrupier[0][1]

    #print(cartasJugador)
    #print(cartasCrupier)

    # Realizamos la apuesta
    apuestaJugador = float(input('Ingrese su apuesta: '))


    # ESCENARIOS
    if apuestaJugador > 0:

        print(f'''
    Tus cartas son: 
        — {cartasJugador[0][0]} de {cartasJugador[0][2]}
        — {cartasJugador[1][0]} de {cartasJugador[1][2]}

        · Valor sumatoria jugador: {sacarValorCartas(cartasJugador)}

    La carta del crupier: 
        — {cartasCrupier[0][0]} de {cartasCrupier[0][2]}
        ''')

        if cartasJugador[0][1] == cartasJugador[1][1]:
            # POSIBILIDAD DE DIVIDIR
            print('######Podes dividir')
            pass

        if (cartasJugador[0][0] == 'AS' and cartasJugador[1][1] == 10) or (cartasJugador[0][1] == 10 and cartasJugador[1][0] == 'AS'):
            print('Ganaste, te tocó BLACKJACK')
            ciclo = 1

        if sacarValorCartas(cartasJugador) >= 9 and sacarValorCartas(cartasJugador) <= 11:
            # POSIBILIDAD DE DOBLAR APUESTA

            duplicarApuesta = input('Tiene la posibilidad de doblar su apuesta (SI/NO)')
            if duplicarApuesta.lower() == 'si':
                print(f'El monto de su apuesta se elevó a ${apuestaJugador*2}')

        if cartasCrupier[0][0] == 'AS':
            seguroJugador = None

            x = input('El crupier sacó AS en su primer carta, quieres pagar un seguro? (SI/NO): ')
            if x.lower() == 'si':
                
                while seguroJugador == None or seguroJugador > (apuestaJugador/2):
                    seguroJugador = float(input(f'Ingrese el monto a asegurar (no puede ser mayor a la mitad de la apuesta[{apuestaJugador}]): '))

            if cartasCrupier[1][1] == 10 and seguroJugador == None:
                print('BLACKJACK del crupier, MALA SUERTE!')
                ciclo = 1
            elif cartasCrupier[1][1] == 10 and seguroJugador != None:
                print(f'BLACKJACK del crupier, te pagamos {seguroJugador*2} por tu seguro!')
                ciclo = 1

        decidirAsJugador(cartasJugador)
        
        while ciclo == None:

            opciones = int(input('\n· Ingrese su opción: [1: Pedir nueva carta, 2: Plantarse, 3: Retirarse]: '))

            if opciones == 1:

                nuevaCarta = repartirCarta()
                cartasJugador.append(nuevaCarta)

                # Si la nueva carta es AS elije el valor
                if nuevaCarta[0] == 'AS':
                    decidirAsJugador(cartasJugador)
                    
                valorJugador = sacarValorCartas(cartasJugador)
                if sacarValorCartas(cartasJugador) > 21:
                    for x in cartasJugador:
                        print(f'— {x[0]} de {x[2]}')
                    print(f'Te pasaste de 21 ({valorJugador}), suerte la próxima!')
                    ciclo = 1
                else:
                    for x in cartasJugador:
                        print(f'— {x[0]} de {x[2]}')
                    print(f'Valor sumatoria jugador: {valorJugador}')

            elif opciones == 2:

                valorCrupier = sacarValorCartas(cartasCrupier)
                
                print(f'— {cartasCrupier[0][0]} de {cartasCrupier[0][2]}')
                print(f'— {cartasCrupier[1][0]} de {cartasCrupier[1][2]}')

                while sacarValorCartas(cartasCrupier) <= 16:
                    x = sacarValorCartas(cartasCrupier)
                    nuevaCarta = repartirCarta()

                    if nuevaCarta[0] == 'AS':
                        if (x + 11) > 21:
                            nuevaCarta[1] = 1
                        else:
                            nuevaCarta[1] = 11

                        print(f'El crupier sacó un AS y le otorgó el valor de {nuevaCarta[1]}')

                    cartasCrupier.append(nuevaCarta)
                    print(f'El crupier sacó una nueva carta {nuevaCarta[1]} de {nuevaCarta[2]}\t(Sumatoria crupier {sacarValorCartas(cartasCrupier)})')

                valorJugador = sacarValorCartas(cartasJugador)
                valorCrupier = sacarValorCartas(cartasCrupier)

                if valorJugador == valorCrupier:
                    #EMPATE
                    print('Hubo un empate')
                    ciclo = 1

                elif (valorJugador > valorCrupier and valorJugador <= 21):
                    #GANA JUGADOR
                    print(f'\t— Felicitaciones ganaste ({valorJugador} - {valorCrupier}) ${apuestaJugador*(1.5)}')

                elif (valorCrupier > valorJugador and valorCrupier <= 21):
                    #GANA CRUPIER
                    print(f'\t— El crupier tuvo mejor suerte que vos! ({valorJugador} - {valorCrupier})')
                    pass
                else: 
                    print(f'\t— Felicitaciones ganaste ({valorJugador} - {valorCrupier}) ${apuestaJugador*(1.5)}')

                ciclo = 1

            elif opciones == 3:
                print(f'Te retiraste xd te devolvemos la mitad ${apuestaJugador/2}')

                ciclo = 1
    else:
        print(f'Para poder jugar esta ronda su apuesta debe ser superior a $0')

jugarBlackJack()
