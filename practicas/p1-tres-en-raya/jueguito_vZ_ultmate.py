import random

import tkinter as tk
from tkinter import messagebox
import random

class TresEnRayaGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tres en Raya")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#f0f0f0')
        
        # Variables del juego
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.game_over = False
        self.ganador = None
        
        # Crear interfaz
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.ventana, text="TRES EN RAYA", font=('Arial', 20, 'bold'), 
                         bg='#f0f0f0', fg='#333333')
        titulo.pack(pady=10)
        
        # Frame para el tablero
        frame_tablero = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_tablero.pack(pady=20)
        
        # Crear botones del tablero
        self.botones = []
        for i in range(3):
            fila_botones = []
            for j in range(3):
                boton = tk.Button(frame_tablero, text='', font=('Arial', 20, 'bold'),
                                 width=6, height=3, bg='#ffffff', fg='#333333',
                                 command=lambda fila=i, columna=j: self.hacer_movimiento(fila, columna))
                boton.grid(row=i, column=j, padx=2, pady=2)
                fila_botones.append(boton)
            self.botones.append(fila_botones)
        
        # Etiqueta de turno actual
        self.etiqueta_turno = tk.Label(self.ventana, text="Turno: Jugador 1 (X)", 
                                      font=('Arial', 14), bg='#f0f0f0', fg='#333333')
        self.etiqueta_turno.pack(pady=10)
        
        # Frame para botones de control
        frame_controles = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_controles.pack(pady=10)
        
        # Botón Reiniciar
        boton_reiniciar = tk.Button(frame_controles, text="Reiniciar Juego", 
                                   font=('Arial', 12), bg='#4CAF50', fg='white',
                                   command=self.reiniciar_juego)
        boton_reiniciar.grid(row=0, column=0, padx=10)
        
        # Botón Salir
        boton_salir = tk.Button(frame_controles, text="Salir", 
                               font=('Arial', 12), bg='#f44336', fg='white',
                               command=self.salir_juego)
        boton_salir.grid(row=0, column=1, padx=10)
        
        # Información de controles
        info = tk.Label(self.ventana, text="Haz clic en las casillas para jugar\nPresiona 'Z' para salir en cualquier momento", 
                       font=('Arial', 10), bg='#f0f0f0', fg='#666666')
        info.pack(pady=10)
        
        # Configurar tecla Z para salir
        self.ventana.bind('z', lambda event: self.salir_juego())
        self.ventana.bind('Z', lambda event: self.salir_juego())
        
    def hacer_movimiento(self, fila, columna):
        if self.game_over or self.tablero[fila][columna] != ' ':
            return
        
        # Realizar movimiento
        self.tablero[fila][columna] = self.jugador_actual
        self.botones[fila][columna].config(text=self.jugador_actual, 
                                          state='disabled',
                                          bg='#e0e0e0')
        
        # Verificar si hay ganador
        resultado = self.verificar_ganador()
        
        if resultado:
            self.game_over = True
            self.mostrar_resultado(resultado)
        else:
            # Cambiar turno
            self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
            self.actualizar_etiqueta_turno()
    
    def verificar_ganador(self):
        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                self.resaltar_ganador('fila', self.tablero.index(fila))
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                self.resaltar_ganador('columna', col)
                return self.tablero[0][col]
        
        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            self.resaltar_ganador('diagonal', 1)
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            self.resaltar_ganador('diagonal', 2)
            return self.tablero[0][2]
        
        # Verificar empate
        if all(self.tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Empate'
        
        return None
    
    def resaltar_ganador(self, tipo, indice):
        colores_ganador = ['#a5d6a7', '#81c784', '#4caf50']  # Verde en diferentes tonos
        
        if tipo == 'fila':
            for j in range(3):
                self.botones[indice][j].config(bg=colores_ganador[j])
        elif tipo == 'columna':
            for i in range(3):
                self.botones[i][indice].config(bg=colores_ganador[i])
        elif tipo == 'diagonal':
            if indice == 1:  # Diagonal principal
                for i in range(3):
                    self.botones[i][i].config(bg=colores_ganador[i])
            else:  # Diagonal secundaria
                for i in range(3):
                    self.botones[i][2-i].config(bg=colores_ganador[i])
    
    def mostrar_resultado(self, resultado):
        if resultado == 'X':
            mensaje = "¡Felicidades Jugador 1! ¡Has ganado!"
        elif resultado == 'O':
            mensaje = "¡Felicidades Jugador 2! ¡Has ganado!"
        else:
            mensaje = "¡Es un empate!"
        
        # Deshabilitar todos los botones
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(state='disabled')
        
        # Mostrar mensaje
        messagebox.showinfo("Fin del juego", mensaje)
        
        # Preguntar si quiere jugar de nuevo
        jugar_de_nuevo = messagebox.askyesno("Tres en Raya", "¿Quieres jugar de nuevo?")
        if jugar_de_nuevo:
            self.reiniciar_juego()
        else:
            self.ventana.quit()
    
    def actualizar_etiqueta_turno(self):
        jugador = "Jugador 1 (X)" if self.jugador_actual == 'X' else "Jugador 2 (O)"
        self.etiqueta_turno.config(text=f"Turno: {jugador}")
    
    def reiniciar_juego(self):
        # Reiniciar variables del juego
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.game_over = False
        self.ganador = None
        
        # Reiniciar botones
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text='', state='normal', bg='#ffffff')
        
        # Actualizar etiqueta de turno
        self.actualizar_etiqueta_turno()
    
    def salir_juego(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir del juego?"):
            self.ventana.quit()
    
    def iniciar(self):
        self.ventana.mainloop()

# Iniciar el juego
if __name__ == "__main__":
    juego = TresEnRayaGUI()
    juego.iniciar()