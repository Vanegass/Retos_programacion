#Reto de Programación
import random

#Se define el juego en diferentes lenguajes

#Español 
def jugar():
    n_intentos = 0
    adivinanza_alta = ["Estás arriba😦", "Baja más🙃","Estás más inflado que Venezuela💀","Apunta⬇️"]
    adivinanza_baja = ["Estás abajo🤣","Sube más🥲","Estás como el valor del Bolivar🤣", "Apunta⬆️"]
    num_random = random.randint(1,50)

    while True:
        try:
            num_user = int(input("Ingresa un número: ")) 

            #Verifica que el número no esté fuera de rango
            if num_user < 1 or num_user > 50: 
                print("Error. Estás fuera de rango")
       
            #Compara con "num_random" y da pistas usando las listas "adivinanza"
            else: 
                if num_user > num_random:
                    print((random.choice(adivinanza_alta)))
                elif num_user < num_random:
                    print((random.choice(adivinanza_baja)))
                else:
                    print("Correcto!")
                    break
                n_intentos += 1 

        except ValueError: 
            print("Error. Ingresa un número") 
    print(f"Tuviste {n_intentos} intentos")

def volver_jugar():
    while True:
        seguir_jugando = input("Quieres seguir jugando? Y/N: ").strip().upper()
        if seguir_jugando == "Y":
            print() #Agregar espacio entre líneas
            jugar()
        elif seguir_jugando == "N" :
            print() 
            print("Gracias por jugar!")
            break
        else:
            print("Error. Coloca 'Y' para seguir o 'N' para salir.")
 
#Ingles
def play():
    tries = 0
    higher_guess = ["You're too high😦", "Go lower🙃", "You're more inflated than Venezuela💀", "Down⬇️"]
    lower_guess = ["You're too low🤣", "Go higher🥲", "Dude, just go up", "Up⬆️"]
    num_random = random.randint(1,50)

    while True:
        try:
            num_user = int(input("Write a number: ")) 

            #Verifies if "num_user" is out of range
            if num_user < 1 or num_user > 50: 
                print("Error. You're out of range")
       
            #Compares to "num_random" y gives clues using the "guess" lists
            else: 
                if num_user > num_random:
                    print((random.choice(higher_guess)))
                elif num_user < num_random:
                    print((random.choice(lower_guess)))
                else:
                    print("Correct!")
                    break
                tries += 1 

        except ValueError: 
            print("Error. Insert a number") 
    print(f"You had {tries} tries")

def play_again():
    while True:
        keep_playing = input("Play again? Y/N: ").strip().upper()
        if keep_playing == "Y":
            print() #Adds spaces
            play()
        elif keep_playing == "N" :
            print() 
            print("Thanks for playing!")
            break
        else:
            print("Error. Write 'Y' to stay or 'N' to end the game.")    

#Aleman
def play_Ger():
    tries = 0
    higher_guess = ["Du bist zu hoch😦", "Geh niedriger🙃", "Du bist aufgeblasener als Venezuela💀", "Nach unten⬇️"]
    lower_guess = ["Du bist zu niedrig🤣", "Geh höher🥲", "Alter, geh einfach nach oben", "Nach oben⬆️"]
    num_random = random.randint(1,50)

    while True:
        try:
            num_user = int(input("Schreib eine Zahl: ")) 

            # Überprüft, ob "num_user" außerhalb des Bereichs liegt
            if num_user < 1 or num_user > 50: 
                print("Fehler. Du bist außerhalb des Bereichs")
       
            # Vergleicht mit "num_random" und gibt Hinweise mit den "guess"-Listen
            else: 
                if num_user > num_random:
                    print((random.choice(higher_guess)))
                elif num_user < num_random:
                    print((random.choice(lower_guess)))
                else:
                    print("Richtig!")
                    break
                tries += 1 

        except ValueError: 
            print("Fehler. Gib eine Zahl ein") 
    print(f"Du hattest {tries} Versuche")

def play_again_Ger():
    while True:
        keep_playing = input("Noch einmal spielen? J/N: ").strip().upper()
        if keep_playing == "J":
            print() # Fügt Leerzeilen hinzu
            play_Ger()
        elif keep_playing == "N" :
            print() 
            print("Danke fürs Spielen!")
            break
        else:
            print("Fehler. Schreib 'J', um weiterzuspielen oder 'N', um das Spiel zu beenden.")

#Programa principal
languages = ["ENG","ESP","DE"] 
print("Adivina el número! - Guess the number!")

while True:
    user_lang = input("Language - Idioma (ENG, ESP, DE): ").upper()
    if user_lang not in languages:
        print("Error.\n'ENG': English - Inglés - Englisch\n'ESP': Spanish - Español - Spanisch\n'DE': German - Alemán - Deustch")
    else:
        if user_lang == languages[0]:
            print("\nGuess the number!\nI've chosen a number between 1 and 50. Try to guess it😉")
            play()
            play_again()
        elif user_lang == languages[1]:
            print("\nAdivina el número!\nHe elegido un número entre 1 y 50. Intenta adivinarlo😉")
            jugar()
            volver_jugar()
        elif user_lang == languages[2]:
            print("\nErrate die Zahl!\nIch habe eine Zahl zwischen 1 und 50 gewählt. Versuch sie zu erraten😉")
            play_Ger()
            play_again_Ger()
        break
