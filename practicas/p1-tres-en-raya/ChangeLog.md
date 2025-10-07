# Cambios del programa

---
## V2 (25/09/2025)

* **- Se eliminó la interfaz de lineas de comando.**

* **+ Se añadió una interfaz visual en ventana para el juego,** remplazando la interfaz previa.

    * Se modificó la logica para adaptarse a los botones de la nueva interfaz.

* **+ Se añadió la opción de salir del juego durante partida**, interrumpiendo la misma al presionar la tecla "Z".

---
## V3 (07/10/2025)

* **+ Se añadió un modo Jugador vs IA**, integrando una **API de inteligencia artificial (LLM7 - GPT-4.1-nano)** para que el segundo jugador sea controlado por la máquina.

    * **La IA analiza el tablero actual** y selecciona automáticamente una posición óptima (1–9) para colocar su ficha **"O"**.  
    * En caso de error o respuesta inválida de la IA, el juego **realiza un movimiento aleatorio de respaldo** para mantener la fluidez de la partida.

* **+ Se añadió soporte multihilo (threading)** para realizar las solicitudes a la API sin congelar la interfaz de Tkinter.

* **+ Se actualizó la interfaz visual**:
    * Se cambió el título a **"Tres en Raya (Jugador vs IA)"**.
    * Se agregaron colores diferenciados para los movimientos de la IA (azul claro) y del jugador (gris claro).
    * Se ajustó el mensaje de turno para indicar claramente cuándo juega la IA.

* **~ Se reorganizó la lógica interna**:
    * Separación de las funciones `turno_ia()`, `movimiento_ia()` y `movimiento_aleatorio()` para mayor claridad.
    * Mejora en la verificación de ganador y gestión de turnos.

* **+ Se añadió un bloque de verificación e instalación de la librería `openai`**, con instrucciones detalladas para su configuración y compatibilidad con la API LLM7.

* **+ Se añadió un indicador de estado de la API debajo del turno actual.**
    * Muestra mensajes como: "Esperando respuesta", "Código 200 - OK" o "Error de conexión".

* **- Se removió la dependencia del segundo jugador humano.**  
  Ahora el modo predeterminado es **Jugador (X) vs IA (O)**.
---