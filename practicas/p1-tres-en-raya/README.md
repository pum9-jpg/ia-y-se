# Descripcion

Método 1: Ejecución Directa
bash
# 1. Clonar o descargar el proyecto
git clone https://github.com/tu-usuario/tres-en-raya.git
cd tres-en-raya

# 2. Ejecutar el juego

# Navegar al directorio del proyecto
cd practicas/p1-tres-en-raya

# Verificar que Python esté instalado
python --version

# Ejecutar el juego
python tres_en_raya.py (verificar si estas en la carpeta p1-tres-en-raya)

# Método 2: desde el visual

# Simplemente abre el archivo y ejecuta:
python tres_en_raya.py

# O usa el botón de ejecución de tu IDE
Cómo Jugar
Reglas del Juego
Objetivo: Formar una línea de tres símbolos iguales (horizontal, vertical o diagonal)

Turnos: Los jugadores alternan turnos (X siempre comienza)

Movimiento: Cada jugador coloca su símbolo en una casilla vacía

Fin del juego: Cuando un jugador gana o todas las casillas están llenas (empate)

Instrucciones Paso a Paso
Iniciar el Juego:

Ejecuta el programa

La ventana del juego se abrirá automáticamente

Realizar Jugadas:

Haz clic en cualquier casilla vacía del tablero

El jugador X (❌) siempre comienza

Los turnos alternan automáticamente

Seguimiento del Juego:

Observa el panel superior para ver de quién es el turno

La puntuación se actualiza en tiempo real

Las casillas ganadoras se destacan en verde

# Controles Disponibles:

Reiniciar Juego: Reinicia el tablero manteniendo la puntuación

Nueva Partida: Resetea completamente la puntuación

Salir: Cierra la aplicación


# Clases Principales
TresEnRaya - Clase Principal
python
class TresEnRaya:
    def __init__(self):          # Inicialización del juego
    def crear_interfaz(self):    # Construcción de la UI
    def jugar(self, posicion):   # Lógica de jugadas
    def verificar_ganador(self): # Detección de victorias
    def reiniciar_juego(self):   # Reset del tablero
Flujo del Programa
Inicialización: Crear ventana y variables del juego

Interfaz: Construir elementos visuales

Game Loop: Esperar interacciones del usuario

Lógica: Procesar jugadas y verificar estado del juego

Actualización: Reflejar cambios en la interfaz

Capturas de Pantalla
Pantalla Principal
text
TRES EN RAYA


Turno del Jugador: X
Puntuación: X: 2 - O: 1 - Empates: 0

[❌] [⭕] [❌]
[⭕] [❌] [⭕]
[ ] [ ] [❌] 🏆

Reiniciar Juego   Nueva Partida   Salir
Mensajes del Juego
Victoria: "🎉 ¡Jugador X ha ganado! ¿Quieres jugar otra vez?"

Empate: "🤝 ¡El juego terminó en empate! ¿Quieres jugar otra vez?"

Confirmación: "¿Estás seguro de que quieres salir del juego?"

Tecnologías Utilizadas
Lenguajes y Frameworks
Python 3.10: Lenguaje de programación principal

Accessible: Interfaz intuitiva para todos los usuarios

