# Juego de 3 en Raya 

Este documento describe un juego simple de 3 en raya implementado en Python utilizando la biblioteca Pygame. El juego permite a dos jugadores alternarse para colocar "X" y "O" en un tablero 3x3, detectando victorias, empates implícitos (reinicio al final) y manejando clics del mouse para las jugadas.

El código está escrito en **Python 3** y requiere la biblioteca gráfica **Pygame** para renderizar la interfaz.

## Requisitos para Ejecutar el Código

Para correr este código en la terminal (o línea de comandos), necesitas lo siguiente:

### 1. **Python Instalado**
   - Asegúrate de tener **Python 3.6 o superior** instalado en tu sistema.
     - En Windows: Descárgalo desde [python.org](https://www.python.org/downloads/) e instala marcando "Add Python to PATH".
     - En macOS: Usa Homebrew (`brew install python`) o descarga desde python.org.
     - En Linux (Ubuntu/Debian): `sudo apt update && sudo apt install python3 python3-pip`.
   - Verifica la instalación abriendo la terminal y ejecutando:
     ```
     python --version
     ```
     o
     ```
     python3 --version
     ```
     Debería mostrar algo como "Python 3.x.x".

### 2. **Instalar Pygame**
   - Pygame es una biblioteca para crear juegos y aplicaciones multimedia en Python. No viene preinstalada, así que instálala usando **pip** (el gestor de paquetes de Python).
   - En la terminal, ejecuta:
     ```
     pip install pygame
     ```
     o, si usas Python 3 específicamente:
     ```
     pip3 install pygame
     ```
   - Si tienes problemas (por ejemplo, en Windows o con permisos), prueba:
     - `python -m pip install pygame`
     - O en Linux/macOS: `sudo pip3 install pygame`.
   - Verifica la instalación ejecutando en Python (abre el intérprete con `python` o `python3`):
     ```python
     import pygame
     print(pygame.__version__)
     ```
     Debería imprimir la versión sin errores.

### 3. **Entorno de Ejecución**
   - **Sistema Operativo**: Compatible con Windows, macOS y Linux.
   - **Dependencias Adicionales**: Ninguna más allá de Python y Pygame. El código usa módulos estándar como `sys`.
   - **Hardware**: Una pantalla gráfica (no funciona en entornos sin GUI, como servidores remotos sin X11 forwarding).

## Instrucciones para Correr el Código



1. **Abre la Terminal**:
   - En Windows: Presiona `Win + R`, escribe `cmd` y presiona Enter.
   - En macOS: Presiona `Cmd + Espacio`, busca "Terminal".
   - En Linux: Busca "Terminal" en el menú.

2. **Navega al Directorio del Archivo**:
   - Usa el comando `cd` para ir a la carpeta donde guardaste el archivo. Por ejemplo:
     ```
     cd C:\Users\TuUsuario\Documentos\Juegos
     ```
     o
     ```
     cd ~/Documentos/Juegos
     ```

3. **Ejecuta el Código**:
   - En la terminal, escribe:
     ```
     python.py
     ```
     o, si usas Python 3:
     ```
     python3.py
     ```
   - Se abrirá una ventana de 600x600 píxeles con el tablero. Haz clic en las casillas para jugar como "X" (primero) y "O" (segundo).
   - El juego detecta ganadores y reinicia automáticamente al final de cada ronda.
   - Para salir, cierra la ventana o presiona el botón de cerrar (o usa `Ctrl + C` en la terminal si es necesario).

