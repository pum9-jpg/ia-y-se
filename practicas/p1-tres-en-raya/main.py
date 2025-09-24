import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.title = "Tres en raya"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    jugador1 = "X"
    celdas = []

    estado_juego_texto = ft.Text(
        "Turno del jugador X",
        color=ft.Colors.GREEN,
        size=20,
        font_family="Times New Roman"
    )

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
    
    def verificar_empate():
        for celda in celdas:
            if celda.content.value == "":
                return False
        estado_juego_texto.value = "¡Empate!"
        return True

    def resetear_tablero(e):
        nonlocal jugador1
        jugador1 = "X"
        for celda in celdas:
            celda.content.value = ""
            celda.on_click = jugar
        page.update()


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

    titulo = ft.Text("TRES EN RAYA", color=ft.Colors.GREEN, size=50, font_family="Times New Roman")

    tablero = ft.GridView(
        max_extent=100,  
        runs_count=3,    
        spacing=10,      
        run_spacing=10,  
        width=320,      
        height=320,
        )

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

    clean_button = ft.ElevatedButton(
        text="Limpiar",
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.BLACK,
        on_click=resetear_tablero
    )

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

ft.app(target=main)