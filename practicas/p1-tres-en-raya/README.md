# tres_rayalimpio_sin_menu.py – explicación no repetitiva

## 1. Objetivo general  
Mini-juego “Tres en raya” que **arranca directamente en la partida**; cuando finaliza permite:  
- **ESPACIO** → reiniciar tablero  
- **ESC** → cerrar programa  

No hay menús ni estados intermedios; todo gira en torno a un único bucle `while True`.

---

## 2. Estructura de datos  
- `board[3][3]` → 0 vacía, 1 jugador O, 2 jugador X  
- `turn` → 1 (O) o 2 (X)  
- `winner` → 0 sin ganador, 1/2 ganador, 3 empate  
- `particles[]` → lista de diccionarios para el confeti  

---

## 3. Flujo de ejecución  
1. `reset()` limpia tablero y variables.  
2. Bucle principal:  
   - Gestiona eventos (ratón y teclado).  
   - Dibuja fondo + fichas.  
   - Comprueba victoria/empate → lanza confeti.  
   - Muestra texto de turno o resultado.  

---

## 4. Entrada de usuario  
- **Click izq**:  
  - Se traduce a celda `(c, r)`.  
  - Si está vacía y no hay ganador, se coloca ficha.  
  - Se alterna `turn = 3 - turn`.  
- **Teclas**:  
  - `ESPACIO` → llama a `reset()` (nueva partida inmediata).  
  - `ESC` → `pygame.quit(); sys.exit()`.

---

## 5. Reglas y comprobaciones  
`check_win(pl)` devuelve `True` si hay:  
- Tres iguales en fila, columna, diagonal principal o inversa.  
`full()` verifica que no queden 0 → empate.

---

## 6. Efectos visuales  
- **Confeti**: al finalizar se generan 80 círculos aleatorios; cada frame se actualiza su posición `y += vy` y se eliminan al salir de pantalla.  
- **Textos**: turno activo o resultado + instrucciones de reinicio/salida.

---

## 7. Dibujado por frame  
1. `draw_board()` → fondo oscuro + cuadrícula azul.  
2. `draw_figures()` → circulo rosa (O) o aspa cyan (X) según `board`.  
3. `update_confeti()` → partículas sobre el tablero.  
4. `draw_text()` → indicadores superiores/inferiores.

---

## 8. Reinicio limpio  
`reset()` crea **nuevo array** `[[0]*3 for _ in range(3)]` (evita copias por referencia), vacía `particles`, pone `turn = 1` y `winner = 0`.

---

## 9. Archivo final  
Un único archivo, sin dependencias externas, listo para ejecutar con `python tres_rayalimpio_sin_menu.py`.