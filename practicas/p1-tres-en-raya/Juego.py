import tkinter as tk
from tkinter import messagebox
import requests
import json
import threading  # para no bloquear la interfaz mientras se espera la respuesta del API

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya - Jugador vs IA (X = IA, O = Humano)")

        self.turno = "O"  # Empieza el jugador humano
        self.botones = [[None for _ in range(3)] for _ in range(3)]

        # API Info
        self.api_url = "https://api.llm7.io/v1/chat/completions"
        self.api_key = "TU_API_KEY_AQUI"

        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(
                    self.root, text="", font=('Arial', 40), width=5, height=2,
                    command=lambda f=fila, c=col: self.presionar(f, c)
                )
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def presionar(self, fila, col):
        boton = self.botones[fila][col]
        if boton["text"] == "" and self.turno == "O":
            boton["text"] = "O"
            if self.verificar_ganador():
                messagebox.showinfo("Juego terminado", "¡Ganaste! 🎉")
                self.reiniciar_juego()
                return
            elif self.empate():
                messagebox.showinfo("Juego terminado", "¡Empate!")
                self.reiniciar_juego()
                return
            else:
                self.turno = "X"
                # Turno de la IA (llamar a la API en un hilo separado)
                threading.Thread(target=self.jugada_ia).start()

    def jugada_ia(self):
        """Llama a la API para obtener la jugada de la IA."""
        estado_tablero = self.obtener_estado_tablero()
        prompt = f"Estamos jugando tres en raya. El tablero actual es:\n{estado_tablero}\n" \
                 f"Yo soy X y tú O. Es mi turno (X). ¿En qué posición jugarías? " \
                 f"Responde solo con coordenadas en formato (fila,columna) empezando desde 1."

        try:
            response = requests.post(
                self.api_url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                },
                json={
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 100,
                    "temperature": 0.5
                },
                timeout=20
            )

            if response.status_code == 200:
                data = response.json()
                texto = data["choices"][0]["message"]["content"]
                fila, col = self.extraer_coordenadas(texto)
                if fila is not None and col is not None and self.botones[fila][col]["text"] == "":
                    self.marcar_casilla_ia(fila, col)
                else:
                    print("⚠️ La IA dio una jugada inválida o ocupada:", texto)
            else:
                print("Error en API:", response.status_code, response.text)

        except Exception as e:
            print("Error en la jugada de la IA:", e)

    def marcar_casilla_ia(self, fila, col):
        self.botones[fila][col]["text"] = "X"
        if self.verificar_ganador():
            messagebox.showinfo("Juego terminado", "¡La IA ha ganado! 🤖")
            self.reiniciar_juego()
        elif self.empate():
            messagebox.showinfo("Juego terminado", "¡Empate!")
            self.reiniciar_juego()
        else:
            self.turno = "O"

    def extraer_coordenadas(self, texto):
        """Extrae (fila, columna) del texto que devuelve la IA."""
        import re
        match = re.search(r"\(?\s*(\d)\s*[,; ]\s*(\d)\s*\)?", texto)
        if match:
            fila = int(match.group(1)) - 1
            col = int(match.group(2)) - 1
            if 0 <= fila <= 2 and 0 <= col <= 2:
                return fila, col
        return None, None

    def obtener_estado_tablero(self):
        """Devuelve el tablero como texto (para enviar al modelo)."""
        filas = []
        for f in range(3):
            fila = []
            for c in range(3):
                valor = self.botones[f][c]["text"] or "-"
                fila.append(valor)
            filas.append(" ".join(fila))
        return "\n".join(filas)

    def verificar_ganador(self):
        for i in range(3):
            if (self.botones[i][0]["text"] == self.botones[i][1]["text"] == self.botones[i][2]["text"] != ""):
                return True
            if (self.botones[0][i]["text"] == self.botones[1][i]["text"] == self.botones[2][i]["text"] != ""):
                return True

        if (self.botones[0][0]["text"] == self.botones[1][1]["text"] == self.botones[2][2]["text"] != ""):
            return True
        if (self.botones[0][2]["text"] == self.botones[1][1]["text"] == self.botones[2][0]["text"] != ""):
            return True

        return False

    def empate(self):
        for fila in self.botones:
            for boton in fila:
                if boton["text"] == "":
                    return False
        return True

    def reiniciar_juego(self):
        for fila in self.botones:
            for boton in fila:
                boton["text"] = ""
        self.turno = "O"

if __name__ == "__main__":
    root = tk.Tk()
    juego = TresEnRaya(root)
    root.mainloop()
