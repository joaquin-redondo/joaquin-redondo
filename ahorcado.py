import random

# Lista de palabras 
words = ["python", "programacion", "tecnologia", "computadora", "inteligencia"]

def select_word():
    #palabra al azar de la lista
    return random.choice(words)

def mostrar_board(word, letter_guessed):
    # Mostrar el tablero
    board = ""
    for letter in word:
        if letter in letter_guessed:
            board += letter
        else:
            board += "_"
    return board

def jugar():
    word_secret = select_word()
    maximum_attempts = 6
    guessed_letters = []
    
    print("¡Bienvenido al juego del ahorcado!")
    
    while True:
        # Muestra el tablero actual
        tablero_actual = mostrar_board(word_secret, guessed_letters)
        print("\n" + tablero_actual)
        
        # Pedir al jugador una letra
        letter = input("Ingresa una letra: ").lower()
        
        # Verificar si la letra ya ha sido adivinada
        if letter in guessed_letters:
            print("Ya adivinaste esa letra.")
            continue
        
        # Verifica si la letra está en la palabra secreta
        if letter in word_secret:
            guessed_letters.append(letter)
            print("Adivinaste una letra correctamente.")
        else:
             maximum_attempts -= 1
             print(f"Letra incorrecta, te quedan {maximum_attempts} intentos.")
        
        # Verificar si el jugador ganó
        if all(letter in guessed_letters for letter in word_secret):
            print(f"\n¡Felicidades! ¡Adivinaste la palabra '{word_secret}'!")
            break
        
        # Verificar si el jugador perdió
        if maximum_attempts == 0:
            print(f"\n¡Perdiste! La palabra secreta era '{word_secret}'.")
            break

if __name__ == "__main__":
    jugar()