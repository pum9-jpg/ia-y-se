# Descripción técnica

El programa implementa el juego de **Tres en Raya** en Python, en una modalidad **jugador contra jugador** en consola.  
La lógica se divide en funciones que gestionan el tablero.

## Para poder jugar, ejecuta el codigo ingresando el siguiente comando en la consola

```bash
python juego.py

---

### Variables principales

```python
tablero          # Matriz 3x3 que almacena el estado del juego
jugador_actual   # Indica de quién es el turno ('X' o 'O')
fila, col        # Coordenadas ingresadas por el jugador para realizar su movimiento

imprimir_tablero(tablero)        # Muestra el tablero en consola con el estado actual
hay_ganador(tablero, jugador)    # Evalúa si el jugador actual ha ganado (filas, columnas o diagonales)
tablero_lleno(tablero)           # Verifica si todas las casillas están ocupadas (empate)
jugar()                          # Controla el flujo principal del juego, alternando turnos y validando jugadas



```
Asi mismo, sigue el siguiente formato estilistico:

| Tipo      | Convención  | En el codigo                         |
|:---------:|:-----------:|---------------------------------------|
| Variables | snake_case  | `tablero`, `jugador_actual`, `fila`, `col` |
| Funciones | snake_case  | `imprimir_tablero`, `hay_ganador`, `tablero_lleno`, `jugar` |



