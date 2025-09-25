# Descripcion tecnica

El programa implemente el juego de Tres en Raya en python, en una modalidad jugador contra jugador.

Dividiendo la logica de la siguiente forma:

### Clase

```python
 class TresEnRayaGUI:
    ...
```
### Variables

```python
self.ventana          # Ventana principal de la interfaz Tkinter
self.tablero          # Matriz 3x3 que almacena el estado del juego
self.jugador_actual   # Indica de quién es el turno ('X' o 'O')
self.game_over        # Booleano que indica si la partida terminó
self.ganador          # Almacena qué símbolo ganó o si hubo empate
self.botones          # Matriz 3x3 de botones en el tablero gráfico
self.etiqueta_turno   # Etiqueta que muestra el turno actual

```
###  Métodos

```python
__init__(self)              # Constructor, configura la ventana y variables iniciales
crear_interfaz(self)        # Crea los elementos gráficos (tablero, botones y etiquetas)
hacer_movimiento(self, fila, columna) # Marca la jugada en el tablero y gestiona el turno
verificar_ganador(self)     # Evalúa si hay ganador, empate o si el juego continúa
resaltar_ganador(self, tipo, indice) # Resalta la línea ganadora en el tablero
mostrar_resultado(self, resultado)   # Muestra un mensaje con el resultado y pregunta si reiniciar
actualizar_etiqueta_turno(self)      # Cambia la etiqueta para mostrar el turno actual
reiniciar_juego(self)       # Reinicia variables y limpia el tablero para una nueva partida
salir_juego(self)           # Cierra la ventana tras confirmar con el usuario
iniciar(self)               # Inicia el bucle principal de Tkinter (mainloop)

```
Asi mismo, sigue el siguiente formato estilistico:

| Tipo | Convención |
|:---:|:---:|
|Variables| snake_case|
|Funciones| snake_case|
|Clases| PascalCase|

Con esto, se mantiene un mejor order para extensiones futuras, como ser la implementación de la libreria `random` para integrar un juego contra computadora automatico.


# Instalación de Python

Para la ejecucion correcta del programa, es necesario tener installado python, esto se puede hacer de las siguiente formas:

## 1. Microsoft Store (Windows)

En la Microsoft Store integrada en Windows, busca `Python 3.13`. Siendo esta la ultima version.
Esta es la forma mas facil y segura de instalación, siendo igualmente recomendada por los desarolladores.

## 2. Visual Studio Code

En las extensiones de `Visual Studio Code`, busca `Python` y selecciona `Python Extension Pack`.
Esto instalara no solo el python mismo, si no varias herramientas de soporte del mismo.