#Esta versión incluye conteo para intentos y manejo en caso de que se coloque un número fuera del rango
import random #liberia que permite crear cosas random

def jugar(): #Juego
    n_intentos = 0
    adivinanza_alta = ["Estás arriba😦", "Baja más🙃",'Estas como la inflación de Venezuela','Casi llegas al cielo con lo alto que estas','Baja baja que estas arriba',
'Casi llegas solo apunta abajo','Que apuntes abajo','El numero te esta oliendo los pies','Estas como que arriba','Tu opción esta arriba del número'] #Lista con oraciones random si estas por encima del num
    adivinanza_baja = ["Estás abajo🤣","Sube más🥲",'Estas como el valor del Bolivar','Estas por debajo del número','El número esta por encima tuyo','En competencia, el numero es el ganador y tu el segundo',
'Recuerda apuntar para arriba','Si subes la mirada lo encuentras','El numero= nariz, tu=pies','Vercia pero estas como que abajo'] #Lista con oraciones random si estas por debajo del num
    num_random = random.randint(1,50) #Numero random

    while True:
        try: #Excepciones
            num_user = int(input("Ingresa un número: ")) #1er entrada de datos
            if num_user < 1 or num_user > 50:
                print("Error. Estás fuera de rango")
            else:
                if num_user > num_random:
                    print((random.choice(adivinanza_alta)))
                elif num_user < num_random:
                    print((random.choice(adivinanza_baja)))
                else:
                    print("Correcto!")
                    break
                n_intentos += 1 #contar intentos
        except ValueError: 
            print("Error. Ingresa un número")
    print(f"Tuviste {n_intentos} intentos")  #mostrar los intentos
  

def volver_jugar(): #Entrada de datos
    while True:
        seguir_jugando = input("Quieres seguir jugando? Y/N: ").strip().upper()
        if seguir_jugando == "Y":
            jugar()
        elif seguir_jugando == "N" :
            print("Gracias por jugar!")
            break
        else:
            print("Error. Input inválido") 

print("Adivina el número!") 
jugar()
volver_jugar()


