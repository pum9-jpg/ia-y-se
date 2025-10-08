import tkinter as tk
from tkinter import messagebox
import openai
import random

# --- Configuración Groq API ---
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="TU API_KEY_AQUI"  # Reemplaza con tu clave de API real de groq
)

# --- Variables globales ---
tablero = [[" " for _ in range(3)] for _ in range(3)]
botones = []
jugador = "X"
game_over = False

# --- Funciones de lógica ---
def verificar_ganador():
    # filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    # diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    # empate
    if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
        return "Empate"
    return None

def mostrar_resultado(resultado):
    if resultado == "X":
        msg = "¡Ganaste! 🎉"
    elif resultado == "O":
        msg = "La IA ganó 🤖"
    else:
        msg = "¡Empate!"
    messagebox.showinfo("Resultado", msg)

def reiniciar():
    global tablero, jugador, game_over
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    for fila in botones:
        for b in fila:
            b.config(text=" ", state="normal")
    jugador = "X"
    game_over = False

# --- Movimiento IA con Groq ---
def movimiento_ia():
    global jugador, game_over
    tablero_texto = "\n".join([" ".join(fila) for fila in tablero])
    prompt = f"""Eres una IA que juega Tres en Raya. Tablero actual:

{tablero_texto}

Las posiciones van del 1 al 9 de izquierda a derecha y de arriba a abajo.
Responde solo con un número (1-9) donde colocarías tu 'O'."""

    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        respuesta = resp.choices[0].message.content.strip()
    except Exception as e:
        print("Error API:", e)
        respuesta = None

    if respuesta and respuesta.isdigit():
        pos = int(respuesta)
        if 1 <= pos <= 9:
            f, c = divmod(pos - 1, 3)
            if tablero[f][c] == " ":
                jugar(f, c)
                return
    # fallback aleatorio
    libres = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if libres:
        f, c = random.choice(libres)
        jugar(f, c)

# --- Acción de jugar ---
def jugar(fila, col):
    global jugador, game_over
    if game_over or tablero[fila][col] != " ":
        return
    tablero[fila][col] = jugador
    botones[fila][col].config(text=jugador, state="disabled")

    resultado = verificar_ganador()
    if resultado:
        game_over = True
        mostrar_resultado(resultado)
        return

    jugador = "O" if jugador == "X" else "X"
    if jugador == "O":
        movimiento_ia()
        jugador = "X"

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("3 en Raya con IA (Groq)")

frame = tk.Frame(ventana)
frame.pack()

for i in range(3):
    fila_botones = []
    for j in range(3):
        b = tk.Button(frame, text=" ", font=("Arial", 24), width=5, height=2,
                      command=lambda f=i, c=j: jugar(f, c))
        b.grid(row=i, column=j)
        fila_botones.append(b)
    botones.append(fila_botones)

tk.Button(ventana, text="Reiniciar", command=reiniciar).pack(pady=10)
tk.Button(ventana, text="Salir", command=ventana.quit).pack()

ventana.mainloop()
