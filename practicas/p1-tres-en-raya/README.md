# Descripcion tecnica

El programa implemente el juego de Tres en Raya en python, en una modalidad jugador contra jugador.

Dividiendo la logica de la siguiente forma:

### Clase

```python
 class TresEnRaya:
    ...
```
### Variables

```python
self.tablero #Matriz 3x3 que almacena el juego
self.jugador_actual #Indica de quien es el turno
self.game_over #bool que indica si la partida terminó
self.ganador #Almacena que simbolo ganó o empate
```
###  Métodos

```python
__init__(self) #Constructor, inicia la clase
imprimir_tablero(self) #Imprime el formato de tablero
movimiento_valido(self, fila, columna) #Valida las pocisiones
verificar_ganardor(self) #Evalua el tablero
movimientos_disponibles(self) #Devuelve las pocisiones vacias
jugar(self) #Gestiona el bucle de juego
```
Asi mismo, sigue el siguiente formato estilistico:

| Tipo | Convención |
|:---:|:---:|
|Variables| snake_case|
|Funciones| snake_case|
|Clases| PascalCase|

Con esto, se mantiene un mejor order para extensiones futuras, como ser la implementación de la libreria ```random``` para integrar un juego contra computadora automatico.


