# ---------------------------------------------
# PARTE 1: Enfoque Convencional
# ---------------------------------------------

def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    if hora_del_dia == "mañana":
        if preferencia_cafeina == "si":
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else:
            return "Te recomendamos un Jugo de Naranja."

    elif hora_del_dia == "tarde":
        if preferencia_cafeina == "si":
            return "Te recomendamos un Latte."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Frappuccino sin café."
            else:
                return "Te recomendamos un Té Helado."

    elif hora_del_dia == "noche":
        if preferencia_cafeina == "si":
            return "Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."
        else:
            return "Te recomendamos un Té de Manzanilla."

    return "No tenemos una recomendación para ese momento del día."


# Ejemplo de uso:
if __name__ == "__main__":
    hora = input("¿Qué momento del día es (mañana/tarde/noche)? ").lower()
    cafeina = input("¿Querés cafeína (si/no)? ").lower()
    dulce = input("¿Te gustan las bebidas dulces (si/no)? ").lower() == "si"

    recomendacion = recomendar_bebida_convencional(hora, cafeina, dulce)
    print("\n" + recomendacion)
