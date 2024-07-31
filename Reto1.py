import random

#num_random = random.randint(1,50)
Oraciones_si_bajo = ['Estas como el valor del Bolivar','Estas por debajo del número','El número esta por encima tuyo','En competencia, el numero es el ganador y tu el segundo',
'Recuerda apuntar para arriba','Si subes la mirada lo encuentras','El numero= nariz, tu=pies','Vercia pero estas como que abajo']
Oraciones_si_arriba = ['Estas como la inflación de Venezuela','Casi llegas al cielo con lo alto que estas','Baja baja que estas arriba',
'Casi llegas solo apunta abajo','Que apuntes abajo','El numero te esta oliendo los pies','Estas como que arriba','Tu opción esta arriba del número']

def leer_entero(): #Validar la entrada 
    while True:
        opcion = input('Ingrese un número entero-> ')
        try:
            numero = int(opcion)
            return numero
        except ValueError:
            print('No es un número entero, intente nuevamente')

def jugar(): #Si desea jugar
    jugar = str(input('Desea jugar?\ny/n\n->'))

    if jugar == 'y':
        juego()
    else:
        print('Bueno feliz dia')


def juego():
    num_random = random.randint(1,50)
    while True:
        opcion_user = leer_entero()
        if opcion_user < num_random:
            Oracion = random.choice(Oraciones_si_bajo)
            print(Oracion)
        elif opcion_user > num_random:
            oracion_arriba = random.choice(Oraciones_si_arriba)
            print(oracion_arriba)
        elif opcion_user == num_random:
            print('felicidades')
            jugar()
            break
            

print('''Bienvenido al juego #1 el cual fue creado por el grupo 3\n
Este se trata un juego de adivinar un número del 1 al 50\n''')
jugar()