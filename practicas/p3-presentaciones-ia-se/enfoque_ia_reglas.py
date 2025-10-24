# ---------------------------------------------
# PARTE 2: Enfoque de IA (Basado en Reglas)
# ---------------------------------------------

# Base de conocimiento (qué)
base_de_conocimiento = [
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "si", "le_gusta_dulce": True},
     "entonces": "Te recomendamos un Mocha."},
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "si", "le_gusta_dulce": False},
     "entonces": "Te recomendamos un Americano."},
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
     "entonces": "Te recomendamos un Jugo de Naranja."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si"},
     "entonces": "Te recomendamos un Latte."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
     "entonces": "Te recomendamos un Frappuccino sin café."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": False},
     "entonces": "Te recomendamos un Té Helado."},
    {"si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
     "entonces": "Te recomendamos un Té de Manzanilla."},
    {"si": {"hora_del_dia": "noche", "preferencia_cafeina": "si"},
     "entonces": "Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."}
]

# Motor de inferencia (cómo)
def motor_de_inferencia(hechos, reglas):
    """
    Busca en la base de conocimiento una regla que coincida con los hechos del usuario.
    """
    for regla in reglas:
        condiciones = regla["si"]
        coincide = True
        for condicion, valor in condiciones.items():
            if hechos.get(condicion) != valor:
                coincide = False
                break
        if coincide:
            return regla["entonces"]
    return "No tenemos una recomendación para tus preferencias."


# Ejemplo de uso:
if __name__ == "__main__":
    hora = input("¿Qué momento del día es (mañana/tarde/noche)? ").lower()
    cafeina = input("¿Querés cafeína (si/no)? ").lower()
    dulce = input("¿Te gustan las bebidas dulces (si/no)? ").lower() == "si"

    hechos_usuario = {
        "hora_del_dia": hora,
        "preferencia_cafeina": cafeina,
        "le_gusta_dulce": dulce
    }

    recomendacion = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
    print("\n" + recomendacion)
