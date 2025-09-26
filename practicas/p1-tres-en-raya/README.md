README.md
markdown
# 🎯 Juego de Tres en Raya (Tic-Tac-Toe)

Un juego clásico de Tres en Raya implementado en Python con interfaz de consola.

## 📋 Requisitos Previos

### Python 3.12+
Este programa requiere Python 3.12 o superior.

#### Verificar instalación de Python:
```bash
python --version
# o
python3 --version
Instalación de Python:
Descargar desde python.org

IMPORTANTE: Marcar la opción "Add Python to PATH" durante la instalación

Verificar la instalación:

bash
python --version

Guía de Instalación y Configuración de Git
📁 Creación de la Estructura de Carpetas
1. Navegar al directorio principal
bash
cd /e/licenciatura Magaly/Inteligencia Artificial

2. Verificar la ubicación actual
bash
pwd
Debería mostrar: /e/licenciatura Magaly/Inteligencia Artificial

🔧 Configuración de Git
3. Verificar la configuración actual de Git
bash
git config --list

4. Configurar tu usuario y correo electrónico (si no está configurado)
bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu.correo@dominio.com"

5. Verificar que la configuración se aplicó correctamente
bash
git config user.name
git config user.email

📥 Clonar el Repositorio
6. Clonar el repositorio usando HTTPS
bash
git clone https://github.com/pum9-jpg/ia-y-se.git ia-y-se

7. Verificar que la clonación fue exitosa
bash
ls -la ia-y-se/

8. Navegar al directorio del repositorio clonado
bash
cd ia-y-se

9. Verificar el estado del repositorio
bash
git status
Debería mostrar: On branch master y working tree clean

🌿 Crear una Nueva Rama
10. Crear y cambiar a una nueva rama
bash
git checkout -b practica-1
11. Verificar que estás en la nueva rama
bash
git branch
Deberías ver un asterisco (*) junto a practica-1

12. Ver el estado final
bash
git status
Debería mostrar: On branch practica-1

✅ Verificación Final
13. Verificar toda la configuración
bash
# Verificar usuario
git config user.name

# Verificar email
git config user.email

# Verificar rama actual
git branch

# Verificar conexión con el repositorio remoto
git remote -v
14. Estructura final de carpetas
bash
pwd
Debería mostrar: /e/licenciatura Magaly/Inteligencia Artificial/ia-y-se

bash
ls -la
Deberías ver: .git/, documentacion/, practicas/

#Ingresa al programa utilizando en la terminal
code .

# comando de ejecucion del juego en la terminal
python practica1.py

2. Ejecutar el juego
bash
python Practica1.py
🎮 Cómo Jugar
El juego comienza con el jugador X

En cada turno, se muestra el tablero actual

Ingresa las coordenadas:

Fila: 0, 1, o 2

Columna: 0, 1, o 2

Para salir del juego, presiona 'Z' cuando te pida la fila

Ejemplo de movimiento:
text
Fila: 1
Columna: 1
📁 Estructura del Código
Clase Principal: PracticaV1
Atributos:
tablero: Matriz 3x3 que representa el juego

jugador_actual: 'X' o 'O'

ganador: Almacena al jugador ganador

Métodos Principales:
Método	Descripción
imprimir_tablero()	Muestra el estado actual del tablero
movimiento_valido(fila, columna)	Verifica si un movimiento es válido
hacer_movimiento(fila, columna)	Ejecuta un movimiento en el tablero
verificar_ganador()	Comprueba condiciones de victoria
tablero_lleno()	Verifica si hay empate
jugar()	Bucle principal del juego
Flujo del Programa
python
# Inicialización
juego = PracticaV1()

# Bucle principal
while not hay_ganador and not empate:
    mostrar_tablero()
    pedir_movimiento()
    verificar_estado_juego()
    cambiar_turno()
🏗️ Características del Código
✅ Manejo de Errores
Validación de entradas numéricas

Verificación de movimientos válidos

Prevención de sobrescritura de casillas

✅ Interfaz de Usuario
Tablero visual en consola

Mensajes informativos claros

Opción de salida con 'Z'

✅ Lógica del Juego
Detección de victoria en filas, columnas y diagonales

Detección de empates

Alternancia automática de turnos

🐛 Solución de Problemas
Error: NameError: name 'TresEnRaya' is not defined
Solución: Asegurarse de que la instancia use el nombre correcto de la clase:

python
juego = PracticaV1()  # ✅ Correcto
# juego = TresEnRaya()  # ❌ Incorrecto
Error: Python no reconocido
Solución: Verificar que Python esté en el PATH o reinstalar marcando la opción correspondiente.

👥 Autores
Kevin Ramos

Magaly Escalera

📝 Notas
Proyecto desarrollado como práctica de programación en Python

Código estructurado y comentado para fácil comprensión

Compatible con Windows, Linux y macOS

¡Diviértete jugando! 🎉

text

## 📂 Para crear el archivo:

### Opción 1: Usar VS Code
```bash
code README.md
Pega el contenido y guarda (Ctrl + S)