# Descripcion tecnica



# 🧠 Tres en Raya con IA (Jugador vs Computadora)

El presente programa implementa el clásico juego de **Tres en Raya (Tic-Tac-Toe)** en **Python**, en una modalidad **Jugador vs IA**, donde la computadora toma decisiones mediante una **API de inteligencia artificial (LLM7 - GPT-4.1-nano)**.


## ⚙️ Descripción Técnica

El programa está desarrollado utilizando **Tkinter** para la interfaz gráfica y la librería **OpenAI** (con base_url de LLM7) para la inteligencia artificial del segundo jugador.

La estructura principal del programa está organizada dentro de una clase que encapsula toda la lógica del juego y la interfaz.

---

### 🧩 Clase Principal

```python
class TresEnRayaGUI:
    ...
```



### 🔢 Variables

```python
self.ventana          # Ventana principal de la interfaz Tkinter
self.tablero          # Matriz 3x3 que almacena el estado del juego
self.jugador_actual   # Indica de quién es el turno ('X' o 'O')
self.game_over        # Booleano que indica si la partida terminó
self.ganador          # Almacena qué símbolo ganó o si hubo empate
self.botones          # Matriz 3x3 de botones en el tablero gráfico
self.etiqueta_turno   # Etiqueta que muestra el turno actual
self.etiqueta_api     # NUEVO: Muestra el estado de la conexión con la API (OK, error, etc.)
```

---

### 🧱 Métodos

```python
__init__(self)               # Constructor, configura la ventana y variables iniciales
crear_interfaz(self)         # Crea los elementos gráficos (tablero, botones y etiquetas)
hacer_movimiento(self, fila, columna)  # Registra jugada del jugador humano
turno_ia(self)               # Llama a la API de IA para obtener el movimiento de la computadora
movimiento_ia(self, fila, columna)     # Ejecuta la jugada de la IA en el tablero
movimiento_aleatorio(self)   # Alternativa si la IA no responde o genera error
verificar_ganador(self)      # Evalúa si hay ganador, empate o si el juego continúa
mostrar_resultado(self, resultado)     # Muestra el resultado del juego
reiniciar_juego(self)        # Limpia el tablero y reinicia variables
salir_juego(self)            # Sale del programa con confirmación
iniciar(self)                # Inicia el bucle principal de Tkinter (mainloop)
```

---

### 🧩 Estilo de Programación

|    Tipo   |  Convención  |
| :-------: | :----------: |
| Variables | `snake_case` |
| Funciones | `snake_case` |
|   Clases  | `PascalCase` |

Esta convención permite mantener un **orden claro y escalable**, facilitando la futura implementación de extensiones.

---

## 🧠 Estado de la API

Debajo del indicador de turno, se añadió una etiqueta informativa que muestra el estado actual de la conexión con la IA.

| Estado              | Mensaje en pantalla                                       |
| :------------------ | :-------------------------------------------------------- |
| Esperando respuesta | `Estado API: Esperando respuesta...`                      |
| Respuesta exitosa   | `Estado API: Código 200 - OK`                             |
| Error o timeout     | `Error de API: <detalle>`                                 |
| Respuesta inválida  | `Estado API: Respuesta inválida, usando jugada aleatoria` |

Esto permite al usuario saber si la IA respondió correctamente o si el sistema utilizó un movimiento alternativo.

---

## 🐍 Instalación de Python

Para ejecutar correctamente el programa, es necesario tener **Python 3.10 o superior** instalado en tu sistema.
Existen tres métodos recomendados:

---

### **1️⃣ Instalación desde Microsoft Store (Windows)**

1. Abre la **Microsoft Store**.
2. Busca **“Python 3.13”** (o la versión más reciente).
3. Haz clic en **Obtener** e instálalo.
4. Una vez instalado, abre una terminal (CMD o PowerShell) y verifica con:

   ```bash
   python --version
   ```

   Debe mostrar algo como:

   ```
   Python 3.13.0
   ```

> 💡 Este método es el más sencillo y recomendado por los desarrolladores de Python.

---

### **2️⃣ Instalación desde Visual Studio Code**

1. Descarga e instala **Visual Studio Code**.
2. Ve al menú de **Extensiones** (icono de cuadrado con esquinas).
3. Busca `Python` y selecciona **Python Extension Pack**.
4. VSCode instalará automáticamente el intérprete de Python junto con herramientas de soporte (debugger, formateo, linters, etc.).
5. Puedes abrir el terminal interno de VSCode y verificar:

   ```bash
   python --version
   ```

---

### **3️⃣ Instalación manual desde línea de comandos**

#### En Windows:

```bash
winget install -e --id Python.Python.3.13
```

#### En Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### En macOS:

```bash
brew install python
```

Una vez instalado, verifica la instalación:

```bash
python3 --version
```

---

## 🔧 Instalación de la librería `openai`

Este proyecto utiliza la librería oficial `openai` (compatible con LLM7) para la comunicación con la IA.

1. Abre la terminal en la carpeta del proyecto.

2. Ejecuta:

   ```bash
   pip install --upgrade openai
   ```

3. Verifica que la instalación se haya completado correctamente:

   ```bash
   python -m pip show openai
   ```

   Debería mostrar algo similar a:

   ```
   Name: openai
   Version: 1.50.2
   Location: C:\Users\<usuario>\AppData\Local\Programs\Python\Python311\Lib\site-packages
   ```

4. Para probar la importación:

   ```python
   import openai
   print("✅ Librería OpenAI importada correctamente")
   ```

---

## 🚀 Ejecución del Programa

1. Guarda el archivo del juego, por ejemplo como:

   ```
   tres_en_raya_ia.py
   ```

2. Abre una terminal en la carpeta donde está el archivo.

3. Ejecuta el programa con:

   ```bash
   python tres_en_raya_ia.py
   ```
   *O con el nombre con el que tengas el archivo.*

4. ¡Juega contra la IA directamente desde la interfaz!

---

## 🤖 Funcionamiento de la IA

El jugador **humano (X)** juega primero.
Cada vez que realiza un movimiento, el programa:

1. **Envía el estado actual del tablero** a la API de LLM7.
2. **Solicita una jugada válida** (posición del 1 al 9).
3. **Ejecuta la jugada de la IA (O)** automáticamente en el tablero.

Si por alguna razón la API falla o devuelve una respuesta inválida, la IA hace una **jugada aleatoria** de respaldo para mantener la fluidez del juego.
*Es posible que la respuesta tarde en llegar unos segundos, esto depende del servicio de la API.*

---

