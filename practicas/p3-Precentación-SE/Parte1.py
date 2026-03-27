def recomendar_bebida_convencional(hora_del_dia,preferencia_cafeina,le_gusta_dulce):
    """
    Recomineda una bebida basandose en la logica de negocio directamentes en el codigo
    """
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'si':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha"
            else:
                return "Te recomendamos un Americano"
        else: #No quiere cafeina por la mañana
            return "Te recomendamos un jugo de naranja"
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'si':
                return "Te recomendamos un Latte"
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Frappuccino sin cafe"
            else:
                return "Te recomendamos un té helado"
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'si':
            print("Advertencia: La cafeína por la noche puede afectar el sueño.")
            return "Te recomendamos un Espresso"
        else:
            return "Te recomendamos un Te de Manzanilla"
    else:
        return "No tenemos una recomendacion para ese momento del dia"

preferencia_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
} 

recomendacion = recomendar_bebida_convencional(
    preferencia_usuario["hora_del_dia"],
    preferencia_usuario["preferencia_cafeina"],
    preferencia_usuario["le_gusta_dulce"]
)

print(f"Enfoque Convencional: {recomendacion}")
