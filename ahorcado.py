### AHORCADO EN PYTHON ###

# Importamos los módulos necesarios
from getpass import getpass

# Bienvenida
print("Bienvenido al ahorcado, si fallas te quedará menos para morir y si aciertas menos para acertar la palabra :)")

# Pedimos una palabra al primer jugador, la escondemos para que el segundo jugador no la vea y la convertimos en lista para operar con ella
print("Ahora que tu compañero no está viendo, elige una palabra:")
word_no = getpass('')
word = list(word_no)

# Queremos saber la longitud de la palabra, para saber cuantos guiones poner
word_lenght = int(len(word))

# Aparición de incógnitas, también la hacemos una lista para iterar con ella más fácil
incognite_wordd = word_lenght*("-")
print(incognite_wordd)
incognite_word = list(incognite_wordd)

# El primer jugador decidirá las vidas del segundo
lifes = int(input("Cuántas vidas le das a tu compañero"))

# Definimos la función que dirá si una letra es válida o no y dirá la victoria
def word_appearance(incognite_word, word, lifes):

    # El juego se ejecutará siempre que el jugador tenga vidas
    while lifes > 0:

        # Se pide una letra en cada ronda
        letter = str(input("Ingresa una letra:\n"))

        # Si la letra está en la plabra, la buscaremos en la palabra para agregarla en el mismo índice a nuestra palabra oculta, además de dar un mensaje de felicitación
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    incognite_word[i] = letter
            print(f"\nMuy buena, has acertado la letra, la palabra queda tal que así: {incognite_word} \n¡Sigue intentándolo!\nTe quedan {lifes} vidas")
            if ''.join(incognite_word) == word_no:  # Verifica si se ha adivinado toda la palabra sin introducirla, solo introduciendo las letras
                print(f"\n¡FELICIDADEEEEEES! Has ganado a tu compañero, la palabra era {word_no}, toda la razón.")
                break

            # Se le da una oportunidad al usuario en cada ronda para intentar acertar la palabra completa, dependiendo de si toca la tecla 1 o 2
            i_know_it = str(input("\tPresiona la tecla <1> para introducir la palabra si ya la sabes, sino, presiona la <2>"))

            if i_know_it == "1":

                # Si el intento de introducir la palabra es la palabra, se gana, sino, se sigue el juego con una vida menos
                tried = str(input("Que palabra crees que es:"))
                if tried == word_no:
                    print(f"\n¡FELICIDADEEEEEES! Has ganado a tu compañero, la palabra era {word_no}, toda la razón.")
                    break
                else:
                    lifes -=1
                    print(f"\nLo siento, has fallado, tu palabra ha quedado tal que así: {incognite_word}\nInténtalo la próxima vez\nTienes {lifes} vidas")
                    continue
            
            # Sino se quiere probar, se puede con la tecla 2
            elif i_know_it == "2":
                continue

        # Si la letra no está en la palabra, se resta una vida y se manda una advertencia, también se sigue el juego.
        else:
            lifes -= 1
            print(f"\nVaya, no has acertado la letra, la palabra está tal que así: {incognite_word} \n¡Sigue intentándolo!\nTe quedan {lifes} vidas")

    # Si las vidas llegan a 0, se pierde el juego
    if lifes == 0:
        print(f"\nLo siento, has perdido, tu palabra ha quedado tal que así: {incognite_word}\nInténtalo la próxima vez\nLa palabra era: {word_no}")

# Ejecutamos la función
word_appearance(incognite_word, word, lifes)