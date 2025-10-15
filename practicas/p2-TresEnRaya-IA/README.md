# 📄 Documentación del código: Tres en Raya (Flet - Python)

Este archivo explica la estructura y el funcionamiento del programa del
juego **Tres en Raya** desarrollado en Python usando la librería
**Flet** para la interfaz gráfica.

------------------------------------------------------------------------
## 🧪 Instalación paso a paso

### 1. Crear y activar un entorno virtual

En la terminal o consola:
-Crear el entorno virtual

```bash
virtualenv -p python3 env
```
-Activar el entorno virtual en Windows(cmd)
```bash
C:\....\env\Scripts\activate
#En caso de que no funcione solo ir hasta el \Scripts y ahi ejecutar
activate
```
Activar el entorno virtual con (bash)
```bash
#ir hasta 
/.../../env/Script
#una vez en ese directorio ejecutar
. activate
```
Verificar que estas dentro del entorno virtual
```bash
#al principio de toda la ruta debe mostrar
(env)
```
### Instalar las librerias
Primero instalaremos flet
estar en el directorio
```bash
practicas/p2-TresEnRaya-IA
```
ejecutar
```bash
pip install flet
```
Segundo instalar request
estar en el directorio
```bash
practicas/p1-tres-en-raya
```
ejecutar
```bash
pip install requests
```
### Ejecutar 
Ahora se debe ejecutar el siguiente comando para que funciones 
Estar en el directorio
```bash
/.../../practicas/p1-tres-en-raya
```
Ejecutar
```bash
python main.py
```
### Advertencia
En caso de que tarde en responder la ia haga click en limpiar y pruebe de nuevo
## 🔹 Configuración inicial

``` python
import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = "Tres en raya"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
```

-   Se importa **Flet** como `ft`.\
-   La función `main(page)` es el punto de entrada para la aplicación.\
-   Configura:
    -   Fondo (`bgcolor`) negro.\
    -   Título de la ventana.\
    -   Alineación vertical y horizontal centrada.

------------------------------------------------------------------------

## 🔹 Variables principales

``` python
jugador1 = "X"
celdas = []
```

-   `jugador1`: guarda de quién es el turno actual (inicia con **X**).\
-   `celdas`: lista que almacenará las casillas del tablero.

``` python
estado_juego_texto = ft.Text(
    "Turno del jugador X",
    color=ft.Colors.GREEN,
    size=20,
    font_family="Times New Roman"
)
```

-   Texto que muestra el estado del juego (turno, ganador o empate).

------------------------------------------------------------------------

## 🔹 Funciones

### 1. `verificar_ganador()`

``` python
def verificar_ganador():
    nonlocal jugador1
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combinacion in combinaciones_ganadoras:
        c1 = celdas[combinacion[0]].content.value
        c2 = celdas[combinacion[1]].content.value 
        c3 = celdas[combinacion[2]].content.value

        if c1 and c1 == c2 and c2 == c3:
            estado_juego_texto.value = f"¡Jugador {c1} es el ganador!"
            for celda in celdas:
                celda.on_click = None 
            return True
    return False
```

-   Define todas las combinaciones ganadoras posibles.\
-   Verifica si tres casillas contienen el mismo valor (**X** o **O**).\
-   Si hay ganador:
    -   Muestra el mensaje en `estado_juego_texto`.\
    -   Deshabilita los clicks en el tablero.

------------------------------------------------------------------------

### 2. `verificar_empate()`

``` python
def verificar_empate():
    for celda in celdas:
        if celda.content.value == "":
            return False
    estado_juego_texto.value = "¡Empate!"
    return True
```

-   Revisa si todas las casillas están llenas.\
-   Si no hay ganador y el tablero está completo → declara **empate**.

------------------------------------------------------------------------

### 3. `resetear_tablero(e)`

``` python
def resetear_tablero(e):
    nonlocal jugador1
    jugador1 = "X"
    for celda in celdas:
        celda.content.value = ""
        celda.on_click = jugar
    page.update()
```

-   Reinicia el juego.\
-   Limpia todas las casillas.\
-   Restaura el turno al jugador **X**.

------------------------------------------------------------------------

### 4. `jugar(e)`

``` python
def jugar(e):
    nonlocal jugador1
    clicked_text = e.control.content
    if clicked_text.value == "":
        clicked_text.value = jugador1
        clicked_text.color = ft.Colors.CYAN_ACCENT_700 if jugador1 == "X" else ft.Colors.RED_ACCENT_700

        e.control.on_click = None

        if not verificar_ganador():
            if not verificar_empate():
                jugador1 = "O" if jugador1 == "X" else "X"
                estado_juego_texto.value = f"Turno del jugador {jugador1}"
        page.update()
```

-   Marca la casilla seleccionada con el valor del jugador.\
-   Cambia el color según sea **X** o **O**.\
-   Desactiva el click de la casilla ya usada.\
-   Verifica si hay ganador o empate.\
-   Si no, cambia de turno.

------------------------------------------------------------------------

## 🔹 Interfaz gráfica

### Título

``` python
titulo = ft.Text("TRES EN RAYA", color=ft.Colors.GREEN, size=50, font_family="Times New Roman")
```

-   Texto principal del juego.

### Tablero

``` python
tablero = ft.GridView(
    max_extent=100,
    runs_count=3,
    spacing=10,
    run_spacing=10,
    width=320,
    height=320,
)
```

-   Usa `GridView` para organizar las 9 casillas.\
-   Cada casilla es un `Container` con un `Text` en su interior.

``` python
for _ in range(9):
    celda_texto = ft.Text(value="", size=50, weight="bold")
    celda = ft.Container(
        width=100,
        height=100,
        bgcolor=ft.Colors.GREEN_700,
        border_radius=ft.border_radius.all(10),
        alignment=ft.alignment.center,
        content=celda_texto,
        on_click=jugar
    )
    tablero.controls.append(celda)
    celdas.append(celda)
```

-   Genera las 9 celdas del tablero.\
-   Cada celda inicia vacía y espera un click para jugar.

### Botón de limpieza

``` python
clean_button = ft.ElevatedButton(
    text="Limpiar",
    bgcolor=ft.Colors.GREEN,
    color=ft.Colors.BLACK,
    on_click=resetear_tablero
)
```

-   Permite reiniciar el tablero cuando se desee.

------------------------------------------------------------------------

## 🔹 Estructura de la página

``` python
page.add(
    ft.Column(
        controls=[
            titulo,
            estado_juego_texto,
            ft.Container(
                content=tablero,
                padding=20,
                bgcolor=ft.Colors.BLACK,
                border_radius=ft.border_radius.all(15)
            ),
            clean_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30
    )
)
```

-   Organiza todos los elementos en una columna centrada.\
-   Incluye el título, estado del juego, tablero y botón.

------------------------------------------------------------------------

## 🔹 Ejecución del programa

``` python
ft.app(target=main)
```

-   Lanza la aplicación con la función principal `main`.
