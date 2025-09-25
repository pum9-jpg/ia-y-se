import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title(" Tres en Raya ")
        self.root.geometry("500x600")
        self.root.configure(bg='#2C3E50')
        self.root.resizable(False, False)
        
        # Variables del juego - INICIALIZAR CORRECTAMENTE
        self.tablero = [' ' for _ in range(9)]  # 9 espacios vacíos
        self.jugador_actual = 'X'  # X siempre empieza
        self.ganador = None  # No hay ganador al inicio
        self.jugadas = 0  # Contador de jugadas
        self.puntuacion = {'X': 0, 'O': 0, 'Empates': 0}
        
        # Crear interfaz
        self.crear_interfaz()
        self.actualizar_interfaz()  # Actualizar estado inicial
        
    def crear_interfaz(self):
        """Crear todos los elementos de la interfaz"""
        
        # Título principal
        titulo_frame = tk.Frame(self.root, bg='#2C3E50')
        titulo_frame.pack(pady=10)
        
        tk.Label(
            titulo_frame,
            text="🎮 TRES EN RAYA",
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
            text="Puntuación: X: 0 - O: 0 - Empates: 0",
            font=('Arial', 10),
            fg='#BDC3C7',
            bg='#34495E'
        )
        self.label_puntuacion.pack(pady=5)
        
        # Tablero de juego
        tablero_frame = tk.Frame(self.root, bg='#2C3E50')
        tablero_frame.pack(pady=20)
        
        # Crear botones del tablero - CORREGIDO
        self.botones = []
        for i in range(3):
            for j in range(3):
                posicion = i * 3 + j  # Calcular posición correcta
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
                    command=lambda pos=posicion: self.jugar(pos)  # CORREGIDO
                )
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.botones.append(btn)  # Lista simple, no matriz
        
        # Controles
        controles_frame = tk.Frame(self.root, bg='#2C3E50')
        controles_frame.pack(pady=15)
        
        # Botón Reiniciar Juego - CORREGIDO
        btn_reiniciar = tk.Button(
            controles_frame,
            text="🔄 Reiniciar Juego",
            font=('Arial', 10, 'bold'),
            bg='#E74C3C',
            fg='white',
            command=self.reiniciar_juego,  # CORREGIDO
            width=15,
            height=1
        )
        btn_reiniciar.pack(side='left', padx=5)
        
        # Botón Nueva Partida - CORREGIDO
        btn_nueva = tk.Button(
            controles_frame,
            text="✨ Nueva Partida",
            font=('Arial', 10, 'bold'),
            bg='#27AE60',
            fg='white',
            command=self.nueva_partida,  # CORREGIDO
            width=15,
            height=1
        )
        btn_nueva.pack(side='left', padx=5)
        
        # Botón Salir - CORREGIDO
        btn_salir = tk.Button(
            controles_frame,
            text="❌ Salir",
            font=('Arial', 10, 'bold'),
            bg='#95A5A6',
            fg='white',
            command=self.salir,  # CORREGIDO
            width=15,
            height=1
        )
        btn_salir.pack(side='left', padx=5)
        
        # Instrucciones
        instrucciones_frame = tk.Frame(self.root, bg='#34495E', relief='ridge', bd=1)
        instrucciones_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(
            instrucciones_frame,
            text="💡 Instrucciones: Haz clic en cualquier casilla para colocar tu ficha (X).\nGana el jugador que forme una línea de tres símbolos iguales.",
            font=('Arial', 9),
            fg='#BDC3C7',
            bg='#34495E',
            justify='center'
        ).pack(pady=8)
    
    def jugar(self, posicion):
        """Manejar la jugada del usuario - CORREGIDO"""
        print(f"Jugada en posición: {posicion}")  # Debug
        
        # Verificar si la posición está vacía y no hay ganador
        if self.tablero[posicion] == ' ' and self.ganador is None:
            # Realizar jugada
            self.tablero[posicion] = self.jugador_actual
            self.jugadas += 1
            
            # Actualizar botón
            color = '#E74C3C' if self.jugador_actual == 'X' else '#3498DB'
            self.botones[posicion].config(
                text=self.jugador_actual,
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
        """Verificar si hay un ganador - CORREGIDO"""
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
                    self.botones[pos].config(bg='#27AE60')  # Verde
                return True
        return False
    
    def mostrar_ganador(self):
        """Mostrar mensaje de ganador - CORREGIDO"""
        self.puntuacion[self.ganador] += 1
        
        mensaje = f"🎉 ¡Jugador {self.ganador} ha ganado!\n\n¿Quieres jugar otra vez?"
        respuesta = messagebox.askyesno("¡Tenemos un ganador!", mensaje)
        
        self.actualizar_interfaz()
        
        if respuesta:
            self.reiniciar_juego()
    
    def mostrar_empate(self):
        """Mostrar mensaje de empate - CORREGIDO"""
        self.puntuacion['Empates'] += 1
        
        mensaje = "🤝 ¡El juego terminó en empate!\n\n¿Quieres jugar otra vez?"
        respuesta = messagebox.askyesno("Empate", mensaje)
        
        self.actualizar_interfaz()
        
        if respuesta:
            self.reiniciar_juego()
    
    def actualizar_interfaz(self):
        """Actualizar la información en pantalla - CORREGIDO"""
        if self.ganador:
            estado = f"¡Jugador {self.ganador} ganó!"
        elif self.jugadas == 9:
            estado = "¡Empate!"
        else:
            estado = f"Turno del Jugador: {self.jugador_actual}"
        
        self.label_turno.config(text=estado)
        
        # Actualizar puntuación
        puntuacion_text = f"Puntuación: X: {self.puntuacion['X']} - O: {self.puntuacion['O']} - Empates: {self.puntuacion['Empates']}"
        self.label_puntuacion.config(text=puntuacion_text)
    
    def reiniciar_juego(self):
        """Reiniciar el juego actual - CORREGIDO"""
        self.tablero = [' ' for _ in range(9)]
        self.jugador_actual = 'X'
        self.ganador = None
        self.jugadas = 0
        
        # Reiniciar botones
        for i, boton in enumerate(self.botones):
            boton.config(
                text=' ',
                bg='#ECF0F1',
                state='normal'
            )
        
        self.actualizar_interfaz()
        print("Juego reiniciado")  # Debug
    
    def nueva_partida(self):
        """Comenzar una nueva partida (resetear puntuación) - CORREGIDO"""
        self.puntuacion = {'X': 0, 'O': 0, 'Empates': 0}
        self.reiniciar_juego()
        messagebox.showinfo("Nueva Partida", "✨ ¡Nueva partida comenzada!")
        print("Nueva partida")  # Debug
    
    def salir(self):
        """Salir del juego - CORREGIDO"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir del juego?"):
            self.root.quit()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

# Función principal CORREGIDA
def main():
    try:
        juego = TresEnRaya()
        juego.ejecutar()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()