# 3 en Raya - Juego de 2 Jugadores

## Descripción

Este proyecto es una implementación simple de un juego de **3 en Raya** (Tic-Tac-Toe) para dos jugadores, desarrollado en Python utilizando la biblioteca gráfica **Tkinter**. El juego se ejecuta en una interfaz gráfica de 3x3 casillas, donde los jugadores alternan turnos colocando "X" o "O". El objetivo es alinear tres símbolos en una fila, columna o diagonal. Si el tablero se llena sin ganador, se declara empate. Al finalizar una partida, el juego se reinicia automáticamente.

El código es autónomo, fácil de entender y ejecutar, ideal para principiantes en programación gráfica con Python.

# 3 en Raya - Juego de 2 Jugadores

## Descripción

Este proyecto es una implementación simple de un juego de **3 en Raya** (Tic-Tac-Toe) para dos jugadores, desarrollado en Python utilizando la biblioteca gráfica **Tkinter**. El juego se ejecuta en una interfaz gráfica de 3x3 casillas, donde los jugadores alternan turnos colocando "X" o "O". El objetivo es alinear tres símbolos en una fila, columna o diagonal. Si el tablero se llena sin ganador, se declara empate. Al finalizar una partida, el juego se reinicia automáticamente.

El código es autónomo, fácil de entender y ejecutar, ideal para principiantes en programación gráfica con Python.

## Variables Principales
Estas son las variables de instancia (atributos de la clase) que almacenan el estado del juego. Se inicializan en el constructor (`__init__`).

### `self.root`
- **Tipo**: Objeto `tk.Tk` (ventana principal de Tkinter).
- **Propósito**: Referencia a la ventana raíz de la aplicación. Se usa para crear y posicionar widgets (como botones) dentro de la interfaz gráfica.

- **Inicialización**: Se pasa como parámetro al constructor desde el punto de entrada (`root = tk.Tk()`).
- **Uso**: En `crear_interfaz()`, se usa como padre para los botones (`tk.Button(self.root, ...)`).

- **Ejemplo de Acceso**:
  ```python
  self.root.title("3 en Raya - 2 Jugadores")  # Configura el título de la ventana
### `self.turno`
- **Tipo**: String ("X" o "O").
- **Propósito**:  Indica qué jugador tiene el turno actual. "X" siempre inicia el juego.
- **Inicialización**: Se establece en "X" en el constructor.
- **Uso**: Se actualiza en presionar() después de cada movimiento válido. Se usa para colocar el símbolo en el botón y verificar ganadores.
- **Ejemplo de Acceso**:
  ```python
  self.turno = "O" if self.turno == "X" else "X"  # Alterna entre X y O
### `self.botones`
- **Tipo**: Lista de listas (matriz 3x3) de objetos tk.Button.
- **Propósito**:  Representa el tablero del juego. Cada elemento es un botón que puede contener texto ("X", "O" o vacío "").
- **Inicialización**: Se crea como [[None for _ in range(3)] for _ in range(3)] en el constructor, y se llena en crear_interfaz().
- **Uso**: Accedida por coordenadas (fila, col) para leer/escribir el estado de las casillas. Es central para verificaciones de ganador y empate.
- **Ejemplo de Acceso**:
  ```python
  self.botones[fila][col] = boton # Asigna un botón a la posición
  boton["text"] = self.turno # Coloca el símbolo en el botón
## Funciones principales
Estas son los métodos de la clase TresEnRaya. Cada uno incluye una explicación, parámetros, lógica clave y el código completo para referencia.
### `verificar_ganador(self)` 
- **Proposito**: Chequea alineaciones en filas, columnas y diagonales.
- **Uso**: Llamado post movimiento, retorna `true` si hay ganador
### `empate(self)` 
- **Proposito**: Verifica si el tablero esta lleno. 
- **Uso**: Llamado post movimiento, si no hay ganador, returna `true` para empate
 
### Características
- Detección automática de ganador (filas, columnas y diagonales).
- Verificación de empate.
- Turnos alternados: "X" inicia.
- Mensajes de alerta para resultados del juego.

## Requisitos

- **Python 3.x** (Tkinter viene incluido por defecto en la mayoría de las instalaciones de Python).
- No se requieren bibliotecas externas adicionales.

Si Tkinter no está disponible (por ejemplo, en algunas distribuciones de Linux), instálalo con:

```bash
sudo apt-get install python3-tk  # Para Ubuntu/Debian
