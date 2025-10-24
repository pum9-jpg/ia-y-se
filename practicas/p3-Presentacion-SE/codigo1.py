def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    """
    Recomienda una bebida basándose en la lógica de negocio directamente en el código.
    """
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'si':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else:  # No quiere cafeína por la mañana
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'si':
            return "Te recomendamos un Latte."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Frappuccino sin café."
            else:
                return "Te recomendamos un Té Helado."
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'si':
            # Advertencia sobre cafeína por la noche
            print("Advertencia: La cafeína por la noche puede afectar el sueño.")
            return "Te recomendamos un Espresso."
        else:
            return "Te recomendamos un Té de Manzanilla."
    else:
        return "No tenemos una recomendación para ese momento del día."

# - Ejemplo de uso -
preferencias_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion = recomendar_bebida_convencional(
    preferencias_usuario["hora_del_dia"],
    preferencias_usuario["preferencia_cafeina"],
    preferencias_usuario["le_gusta_dulce"]
)

print(f"Enfoque Convencional: {recomendacion}")
