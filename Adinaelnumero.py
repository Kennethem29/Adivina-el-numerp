import random

def iniciar_juego():
    print("\n\nBienvenido al juego de Adivinar el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tienes 10 intentos para adivinarlo.")

    # Generar número aleatorio
    numero_a_adivinar = random.randint(1, 100)
    intentos_restantes = 10

    while intentos_restantes > 0:
        try:
            # Pedir al usuario un número
            intento = int(input(f"\nTe quedan {intentos_restantes} intentos. Ingresa tu número: "))

            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            # Comparar el intento con el número a adivinar
            if intento == numero_a_adivinar:
                print("\n¡Correcto! Has adivinado el número.")
                break
            elif intento < numero_a_adivinar:
                print("Demasiado bajo. Intenta con un número más alto.")
            else:
                print("Demasiado alto. Intenta con un número más bajo.")

            # Reducir intentos restantes
            intentos_restantes -= 1

            if intentos_restantes == 0:
                print(f"\nLo siento, te has quedado sin intentos. El número correcto era {numero_a_adivinar}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

    # Preguntar si quiere reiniciar
    reiniciar = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if reiniciar == 's':
        iniciar_juego()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

if __name__ == "__main__":
    iniciar_juego()
