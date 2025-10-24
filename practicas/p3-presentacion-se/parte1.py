# --- Código original 1 (mañana/tarde) ---
def recomendar_bebida_convencional_mananatarde(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'sí':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else:  # No quiere cafeína por la mañana
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'sí':
            if le_gusta_dulce:
                return "Te recomendamos un Latte."
            else:
                return "Te recomendamos un Espresso."


# --- Código original 2 (tarde/noche) ---
def recomendar_bebida_convencional_tardenoche(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    if hora_del_dia == 'tarde':
        if le_gusta_dulce:
            return "Te recomendamos un Frappuccino sin café."
        else:
            return "Te recomendamos un Té Helado."
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'sí':
            print("Advertencia: la cafeína por la noche puede afectar el sueño.")
            return "Te recomendamos un Espresso."
        else:
            return "Te recomendamos un Té de Manzanilla."
    else:
        return "No tenemos una recomendación para ese momento del día."


# --- Función unificada (sin alterar los códigos originales) ---
def recomendar_bebida(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    if hora_del_dia in ['mañana', 'tarde']:
        return recomendar_bebida_convencional_mananatarde(hora_del_dia, preferencia_cafeina, le_gusta_dulce)
    elif hora_del_dia in ['tarde', 'noche']:
        return recomendar_bebida_convencional_tardenoche(hora_del_dia, preferencia_cafeina, le_gusta_dulce)
    else:
        return "No tenemos una recomendación para ese momento del día."


# --- Ejemplo de uso ---
preferencias_usuario = {
    "hora_del_dia": "noche",
    "preferencia_cafeina": "sí",
    "le_gusta_dulce": False
}

print("Recomendación final:", recomendar_bebida(
    preferencias_usuario["hora_del_dia"],
    preferencias_usuario["preferencia_cafeina"],
    preferencias_usuario["le_gusta_dulce"]
))
