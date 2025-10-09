import requests
import json
import random
import os  # Para leer variables de entorno

# URL de la API Groq
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Obtener la API_KEY desde una variable de entorno
API_KEY = os.getenv("GROQ_API_KEY")  # Configura en tu terminal o .env

tablero = [" "] * 9

def imprimir():
    for i in range(0, 9, 3):
        print(f" {tablero[i]} | {tablero[i+1]} | {tablero[i+2]} ")
        if i < 6:
            print("---+---+---")

def ganador():
    lineas = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in lineas:
        if tablero[a] == tablero[b] == tablero[c] != " ":
            return tablero[a]
    if " " not in tablero:
        return "Empate"
    return None

def turno_jugador(jugador):
    while True:
        try:
            pos = int(input(f"Turno de {jugador}, elige (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Elige un número del 1 al 9.")
                continue
            if tablero[pos] == " ":
                tablero[pos] = jugador
                break
            else:
                print("Casilla ocupada, elige otra.")
        except ValueError:
            print("Debes ingresar un número válido.")

def jugada_ia(tablero):
    prompt = (
        "Eres un jugador experto de 3 en raya (Tic-tac-toe)."
        "El tablero está numerado del 1 al 9 de izquierda a derecha, arriba a abajo. \n"
        "Tu ficha es 'X' y la del jugador es 'O'."
        "Debes jugar la jugada optima: siempre ganar si puedes,"
        "O bloquear cualquier intento de ganar del jugador."
        "Responde SOLO con el numero (1-9) de la casilla que elegiste."
        "No escribas nada mas.\n\n"
        f"Tablero actual: \n"
        f"{tablero[0:3]}\n{tablero[3:6]}\n\n{tablero[6:9]}"
    )
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "Eres un jugador de tres en raya que responde solo con un número del 1 al 9."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(API_URL, headers=headers, json=data)
        res_json = res.json()
        print("\n--- Respuesta de la IA ---")
        print(json.dumps(res_json, indent=2))

        if "choices" in res_json:
            respuesta = res_json["choices"][0]["message"]["content"]
            print(f"La IA respondió: {respuesta}")
            for c in respuesta:
                if c.isdigit() and 1 <= int(c) <= 9:
                    pos = int(c) - 1
                    if tablero[pos] == " ":
                        return pos
        else:
            print("⚠️ Error en la respuesta de la API:")
            print(res_json.get("error", "Respuesta desconocida."))
    except Exception as e:
        print("⚠️ Error al comunicarse con la IA:", e)

    posibles = [i for i, x in enumerate(tablero) if x == " "]
    return random.choice(posibles) if posibles else 0

def juego_vs_ia():
    global tablero
    tablero = [" "] * 9
    turno = "X"
    while True:
        imprimir()
        if turno == "X":
            turno_jugador("X")
        else:
            print("\nTurno de la IA...\n")
            pos = jugada_ia(tablero)
            tablero[pos] = "O"
        g = ganador()
        if g:
            imprimir()
            print("¡Empate!" if g == "Empate" else f"¡Gana {g}!")
            break
        turno = "O" if turno == "X" else "X"

def juego_dos_jugadores():
    global tablero
    tablero = [" "] * 9
    turno = "X"
    while True:
        imprimir()
        turno_jugador(turno)
        g = ganador()
        if g:
            imprimir()
            print("¡Empate!" if g == "Empate" else f"¡Gana {g}!")
            break
        turno = "O" if turno == "X" else "X"

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Instrucciones")
        print("2) Jugar 2 jugadores")
        print("3) Jugar contra IA (Groq)")
        print("4) Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("\nInstrucciones:")
            print("El tablero tiene 9 casillas numeradas del 1 al 9:")
            print(" 1 | 2 | 3 ")
            print("---+---+---")
            print(" 4 | 5 | 6 ")
            print("---+---+---")
            print(" 7 | 8 | 9 ")
            print("El primero en hacer tres en línea gana.\n")
        elif opcion == "2":
            print("\n--- JUEGO 2 JUGADORES ---")
            juego_dos_jugadores()
        elif opcion == "3":
            print("\n--- JUEGO CONTRA IA (Groq) ---")
            juego_vs_ia()
        elif opcion == "4":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
