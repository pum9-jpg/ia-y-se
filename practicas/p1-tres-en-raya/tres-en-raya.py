import tkinter as tk
from tkinter import messagebox
import requests
import json
import random

class TresEnRaya:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title(" Tres en Raya vs IA ")
        self.root.geometry("500x650")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)
        
        # Configuración de la API LLM7.io
        self.API_KEY = "Bearer RXeDtkorCZS5u1whAqChCvAq9Yu1JyKwETDE2lO6iR4E0rOf+NVlRHkDcBoPFU1rgvXd3a60ve3Pr1TbV3QP9519aaLQTNlTYtFzQ1VlS0X2fM0Tw7F/moJ+qpRYpk4DtKC1YBFK8H7Ug"  #"  # ¡REEMPLAZA CON TU API KEY!
        self.API_URL = "https://api.llm7.io/v1/chat/completions"
        
        # Variables del juego
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'  # Jugador humano es X
        self.ia_jugador = 'O'     # IA es O
        self.ganador = None
        self.jugadas = 0
        self.puntuacion = {'Jugador (X)': 0, 'IA (O)': 0, 'Empates': 0}
        self.modo_ia = True  # Activar modo IA
        
        # Crear interfaz
        self.crear_interfaz()
        self.actualizar_interfaz()
        
    def crear_interfaz(self):
        """Crear todos los elementos de la interfaz"""
        
        # Título principal
        titulo_frame = tk.Frame(self.root, bg='#2C3E50')
        titulo_frame.pack(pady=10)
        
        tk.Label(
            titulo_frame,
            text="🎮 TRES EN RAYA vs IA",
            font=('Arial', 20, 'bold'),
            fg='#ECF0F1',
            bg='#2C3E50'
        ).pack()
        
        tk.Label(
            titulo_frame,
            text="By Bustamante Adrian, Mamani Samuel - Práctica 1",
            font=('Arial', 10),
            fg='#BDC3C7',
            bg='#2C3E50'
        ).pack(pady=5)
        
        # Panel de información
        info_frame = tk.Frame(self.root, bg='#34495E', relief='ridge', bd=2)
        info_frame.pack(fill='x', padx=20, pady=10)
        
        self.label_turno = tk.Label(
            info_frame,
            text="Turno del Jugador: X",
            font=('Arial', 14, 'bold'),
            fg='#ECF0F1',
            bg='#34495E'
        )
        self.label_turno.pack(pady=8)
        
        self.label_puntuacion = tk.Label(
            info_frame,
            text="Puntuación: Jugador (X): 0 - IA (O): 0 - Empates: 0",
            font=('Arial', 10),
            fg='#BDC3C7',
            bg='#34495E'
        )
        self.label_puntuacion.pack(pady=5)
        
        # Tablero de juego
        tablero_frame = tk.Frame(self.root, bg='#2C3E50')
        tablero_frame.pack(pady=20)
        
        # Crear botones del tablero
        self.botones = []
        for i in range(3):
            for j in range(3):
                posicion = i * 3 + j
                btn = tk.Button(
                    tablero_frame,
                    text=' ',
                    font=('Arial', 20, 'bold'),
                    width=4,
                    height=2,
                    bg='#ECF0F1',
                    fg='#2C3E50',
                    relief='raised',
                    bd=3,
                    command=lambda pos=posicion: self.jugar(pos)
                )
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.botones.append(btn)
        
        # Controles
        controles_frame = tk.Frame(self.root, bg='#2C3E50')
        controles_frame.pack(pady=15)
        
        # Botón Reiniciar Juego
        btn_reiniciar = tk.Button(
            controles_frame,
            text="🔄 Reiniciar Juego",
            font=('Arial', 10, 'bold'),
            bg='#E74C3C',
            fg='white',
            command=self.reiniciar_juego,
            width=15,
            height=1
        )
        btn_reiniciar.pack(side='left', padx=5)
        
        # Botón Nueva Partida
        btn_nueva = tk.Button(
            controles_frame,
            text="✨ Nueva Partida",
            font=('Arial', 10, 'bold'),
            bg='#27AE60',
            fg='white',
            command=self.nueva_partida,
            width=15,
            height=1
        )
        btn_nueva.pack(side='left', padx=5)
        
        # Botón Activar/Desactivar IA
        self.btn_ia = tk.Button(
            controles_frame,
            text="🤖 IA: Activada",
            font=('Arial', 10, 'bold'),
            bg='#3498DB',
            fg='white',
            command=self.toggle_ia,
            width=15,
            height=1
        )
        self.btn_ia.pack(side='left', padx=5)
        
        # Estado de la IA
        self.label_estado_ia = tk.Label(
            self.root,
            text="Estado: IA conectada y lista",
            font=('Arial', 9),
            fg='#27AE60',
            bg='#2C3E50'
        )
        self.label_estado_ia.pack(pady=5)
        
        # Instrucciones
        instrucciones_frame = tk.Frame(self.root, bg='#34495E', relief='ridge', bd=1)
        instrucciones_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(
            instrucciones_frame,
            text="💡 Instrucciones: Tú eres X, la IA es O. Haz clic en cualquier casilla.\nLa IA responderá automáticamente después de tu movimiento.",
            font=('Arial', 9),
            fg='#BDC3C7',
            bg='#34495E',
            justify='center'
        ).pack(pady=8)
    
    def consultar_ia(self, tablero_actual):
        """Consultar a la IA para obtener su movimiento"""
        try:
            # Convertir tablero a representación visual
            tablero_str = ""
            for i in range(0, 9, 3):
                fila = " | ".join([f"[{tablero_actual[i+j]}]" for j in range(3)])
                tablero_str += fila + "\n"
                if i < 6:
                    tablero_str += "---+---+---\n"
            
            # Preparar el prompt para la IA
            prompt = f"""
            Juego de Tres en Raya. Eres el jugador 'O'. El jugador humano es 'X'.
            
            Tablero actual (posiciones 0-8):
            {tablero_str}
            
            Posiciones disponibles: {[i for i, celda in enumerate(tablero_actual) if celda == ' ']}
            
            Responde SOLO con el número de la posición (0-8) donde quieres jugar.
            No incluyas texto adicional, solo el número.
            Ejemplo de respuesta: 4
            """
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.API_KEY}"
            }
            
            data = {
                "model": "llama-3-8b",  # Puedes cambiar el modelo si es necesario
                "messages": [
                    {
                        "role": "system", 
                        "content": "Eres un experto jugador de Tres en Raya. Analiza el tablero y elige la mejor jugada. Responde únicamente con el número de la posición (0-8) donde quieres colocar tu ficha 'O'."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 10,
                "temperature": 0.1,
                "top_p": 0.9
            }
            
            response = requests.post(self.API_URL, headers=headers, json=data, timeout=15)
            
            if response.status_code == 200:
                result = response.json()
                movimiento_texto = result["choices"][0]["message"]["content"].strip()
                print(f"IA respondió: {movimiento_texto}")  # Debug
                
                # Extraer número del movimiento
                try:
                    # Buscar cualquier número en la respuesta
                    for char in movimiento_texto:
                        if char.isdigit():
                            movimiento = int(char)
                            if 0 <= movimiento <= 8 and tablero_actual[movimiento] == ' ':
                                return movimiento
                    
                    # Si no encuentra número válido, usar movimiento aleatorio
                    return self.movimiento_aleatorio(tablero_actual)
                    
                except (ValueError, IndexError):
                    return self.movimiento_aleatorio(tablero_actual)
            else:
                print(f"Error API: {response.status_code} - {response.text}")
                self.label_estado_ia.config(text="Error en API, usando movimiento aleatorio", fg='#E74C3C')
                return self.movimiento_aleatorio(tablero_actual)
                
        except Exception as e:
            print(f"Error consultando IA: {e}")
            self.label_estado_ia.config(text="Error de conexión, usando movimiento aleatorio", fg='#E74C3C')
            return self.movimiento_aleatorio(tablero_actual)
    
    def movimiento_aleatorio(self, tablero):
        """Movimiento aleatorio si la IA falla"""
        movimientos_disponibles = [i for i, celda in enumerate(tablero) if celda == ' ']
        if movimientos_disponibles:
            return random.choice(movimientos_disponibles)
        return 0
    
    def jugar(self, posicion):
        """Manejar la jugada del usuario"""
        print(f"Jugada en posición: {posicion}")
        
        # Verificar si la posición está vacía y no hay ganador
        if self.tablero[posicion] == ' ' and self.ganador is None and self.jugador_actual == 'X':
            # Realizar jugada del humano
            self.realizar_jugada(posicion, self.jugador_actual)
            
            # Verificar si el juego continúa y es turno de la IA
            if not self.ganador and self.jugadas < 9 and self.modo_ia:
                # Turno de la IA después de 1 segundo
                self.root.after(1000, self.turno_ia)
    
    def turno_ia(self):
        """Turno de la IA"""
        if self.ganador is None and self.jugadas < 9:
            self.label_estado_ia.config(text="🤖 IA pensando...", fg='#F39C12')
            self.root.update()
            
            # Consultar a la IA
            movimiento_ia = self.consultar_ia(self.tablero)
            
            # Verificar si el movimiento es válido
            if self.tablero[movimiento_ia] == ' ':
                self.realizar_jugada(movimiento_ia, self.ia_jugador)
                self.label_estado_ia.config(text="✅ IA ha jugado", fg='#27AE60')
            else:
                # Si la IA elige una posición ocupada, elegir aleatorio
                movimiento_ia = self.movimiento_aleatorio(self.tablero)
                self.realizar_jugada(movimiento_ia, self.ia_jugador)
                self.label_estado_ia.config(text="⚠️ IA usó movimiento aleatorio", fg='#E74C3C')
    
    def realizar_jugada(self, posicion, jugador):
        """Realizar una jugada en el tablero"""
        self.tablero[posicion] = jugador
        self.jugadas += 1
        
        # Actualizar botón
        color = '#E74C3C' if jugador == 'X' else '#3498DB'
        self.botones[posicion].config(
            text=jugador,
            fg=color,
            state='disabled',
            disabledforeground=color
        )
        
        # Verificar si hay ganador
        if self.verificar_ganador():
            self.mostrar_ganador()
        elif self.jugadas == 9:
            self.mostrar_empate()
        else:
            # Cambiar turno
            self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
            self.actualizar_interfaz()
    
    def verificar_ganador(self):
        """Verificar si hay un ganador"""
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combo in combinaciones:
            a, b, c = combo
            if self.tablero[a] != ' ' and self.tablero[a] == self.tablero[b] == self.tablero[c]:
                self.ganador = self.tablero[a]
                # Resaltar combinación ganadora
                for pos in combo:
                    self.botones[pos].config(bg='#27AE60')
                return True
        return False
    
    def mostrar_ganador(self):
        """Mostrar mensaje de ganador"""
        if self.ganador == 'X':
            ganador_texto = "Jugador (X)"
            self.puntuacion['Jugador (X)'] += 1
        else:
            ganador_texto = "IA (O)"
            self.puntuacion['IA (O)'] += 1
        
        mensaje = f"🎉 ¡{ganador_texto} ha ganado!\n\n¿Quieres jugar otra vez?"
        respuesta = messagebox.askyesno("¡Tenemos un ganador!", mensaje)
        
        self.actualizar_interfaz()
        
        if respuesta:
            self.reiniciar_juego()
    
    def mostrar_empate(self):
        """Mostrar mensaje de empate"""
        self.puntuacion['Empates'] += 1
        
        mensaje = "🤝 ¡El juego terminó en empate!\n\n¿Quieres jugar otra vez?"
        respuesta = messagebox.askyesno("Empate", mensaje)
        
        self.actualizar_interfaz()
        
        if respuesta:
            self.reiniciar_juego()
    
    def actualizar_interfaz(self):
        """Actualizar la información en pantalla"""
        if self.ganador:
            ganador_texto = "Jugador (X)" if self.ganador == 'X' else "IA (O)"
            estado = f"¡{ganador_texto} ganó!"
        elif self.jugadas == 9:
            estado = "¡Empate!"
        else:
            jugador_texto = "Jugador (X)" if self.jugador_actual == 'X' else "IA (O)"
            estado = f"Turno: {jugador_texto}"
        
        self.label_turno.config(text=estado)
        
        # Actualizar puntuación
        puntuacion_text = f"Puntuación: Jugador (X): {self.puntuacion['Jugador (X)']} - IA (O): {self.puntuacion['IA (O)']} - Empates: {self.puntuacion['Empates']}"
        self.label_puntuacion.config(text=puntuacion_text)
    
    def toggle_ia(self):
        """Activar/desactivar modo IA"""
        self.modo_ia = not self.modo_ia
        if self.modo_ia:
            self.btn_ia.config(text="🤖 IA: Activada", bg='#3498DB')
            self.label_estado_ia.config(text="✅ IA activada", fg='#27AE60')
        else:
            self.btn_ia.config(text="🤖 IA: Desactivada", bg='#95A5A6')
            self.label_estado_ia.config(text="⏸️ IA desactivada - Modo manual", fg='#BDC3C7')
    
    def reiniciar_juego(self):
        """Reiniciar el juego actual"""
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'  # Humano siempre empieza
        self.ganador = None
        self.jugadas = 0
        
        # Reiniciar botones
        for boton in self.botones:
            boton.config(
                text=' ',
                bg='#ECF0F1',
                state='normal'
            )
        
        self.actualizar_interfaz()
        self.label_estado_ia.config(text="✅ IA conectada y lista", fg='#27AE60')
    
    def nueva_partida(self):
        """Comenzar una nueva partida (resetear puntuación)"""
        self.puntuacion = {'Jugador (X)': 0, 'IA (O)': 0, 'Empates': 0}
        self.reiniciar_juego()
        messagebox.showinfo("Nueva Partida", "✨ ¡Nueva partida comenzada!")
    
    def salir(self):
        """Salir del juego"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir del juego?"):
            self.root.quit()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

# Función principal
def main():
    try:
        juego = TresEnRaya()
        juego.ejecutar()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()