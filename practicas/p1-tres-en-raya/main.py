import flet as ft
import requests

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

    def bloquear_ganador(tablero):
    # Combinaciones ganadoras posibles
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
    
        for combinacion in combinaciones_ganadoras:
            c1, c2, c3 = combinacion
            if tablero[c1] == 'X' and tablero[c2] == 'X' and tablero[c3] == '_':
                return c3
            if tablero[c1] == 'X' and tablero[c3] == 'X' and tablero[c2] == '_':
                return c2
            if tablero[c2] == 'X' and tablero[c3] == 'X' and tablero[c1] == '_':
                return c1
        return -1    

    def obtener_movimiento_llm7(tablero, jugador_ia="O"):
        url = "https://api.llm7.io/v1/chat/completions"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer unused"
        }

        casilla_a_bloquear = bloquear_ganador(tablero)
        if casilla_a_bloquear != -1:
            return casilla_a_bloquear
        # Representar el tablero en formato 3x3 legible
        tablero_visual = (
            f"{tablero[0]} | {tablero[1]} | {tablero[2]}\n"
            f"{tablero[3]} | {tablero[4]} | {tablero[5]}\n"
            f"{tablero[6]} | {tablero[7]} | {tablero[8]}"
        )

        prompt_sistema = (
            "Eres una IA experta en el juego de tres en raya. "
            "Tu única tarea es analizar el tablero y devolver el índice (de 0 a 8) "
            "donde debe jugar el jugador 'O'. "
            "Si el jugador 'X' está a punto de ganar, es decir, si tiene dos 'X' en una línea y la tercera casilla está vacía, "
            "debes bloquear esa jugada colocando un 'O' en la casilla vacía. "
            "Nunca debes dejar que el jugador 'X' gane en su próximo turno. "
            "Si no hay una amenaza de victoria de 'X', puedes jugar en cualquier casilla vacía, pero siempre con el objetivo de bloquear cualquier jugada futura. "
            "Los índices se distribuyen así:\n"
            "0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n"
            "Devuelve solo el número (0 a 8) y nada más."
        )

        prompt_usuario = (
            f"Este es el tablero actual:\n{tablero_visual}\n"
            f"¿Dónde debe jugar el jugador '{jugador_ia}'? Solo responde con el número (0 a 8)."
        )

        data = {
            "model": "mistral-small-3.1-24b-instruct-2503",
            "messages": [
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": prompt_usuario}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            respuesta_ia = response.json()
            texto = respuesta_ia["choices"][0]["message"]["content"].strip()
            movimiento = int("".join(filter(str.isdigit, texto)))

            if 0 <= movimiento <= 8 and tablero[movimiento] == "_":
                return movimiento
            else:
                print("Índice inválido, usando primer espacio disponible.")
        except Exception as e:
            print(f"Error al llamar a LLM7.io: {e}")

    # Fallback
        for i, valor in enumerate(tablero):
            if valor == "_":
                return i
        return 0


    def jugar_ia():
        nonlocal jugador1

        # 🧠 1. Obtenemos el estado del tablero como lista de 9 strings
        tablero = [celda.content.value if celda.content.value != "" else "_" for celda in celdas]

        # 🧠 2. Llamamos a la IA
        indice_ia = obtener_movimiento_llm7(tablero, jugador_ia="O")

        # ✅ 3. Ejecutamos la jugada
        celda = celdas[indice_ia]
        celda.content.value = "O"
        celda.content.color = ft.Colors.RED_ACCENT_700
        celda.on_click = None

        # 🔁 4. Verificamos estado del juego
        if not verificar_ganador():
            if not verificar_empate():
                jugador1 = "X"
                estado_juego_texto.value = "Turno del jugador X"

        page.update()


    def jugar(e):
        nonlocal jugador1

        # 🚫 Ignorar clics si es el turno de la IA
        if jugador1 != "X":
            return

        clicked_text = e.control.content
        if clicked_text.value == "":
            clicked_text.value = jugador1
            clicked_text.color = ft.Colors.CYAN_ACCENT_700

            e.control.on_click = None

            if not verificar_ganador():
                if not verificar_empate():
                    jugador1 = "O"
                    estado_juego_texto.value = "Turno del jugador O"
                    page.update()
                    jugar_ia()  # llama directamente a la IA

        page.update()
        """nonlocal jugador1
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
                    if jugador1 == "O":
                        jugar_ia()
            page.update()"""
    

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