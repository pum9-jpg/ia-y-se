# 1. BASE DE CONOCIMIENTO (El "qué")
# Representamos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ('si') y una
# conclusión ('entonces').
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "si", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "si", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Americano."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Jugo de Naranja."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si"},
        "entonces": "Te recomendamos un Latte."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Frappuccino sin café."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Té Helado."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té de Manzanilla."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "si"},
        "entonces": "Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."
    }
]

# 2. MOTOR DE INFERENCIA (El "cómo")
# Esta función no sabe nada sobre café, solo sabe cómo aplicar reglas.
def motor_de_inferencia(hechos, reglas):
    """
    Busca en la base de conocimiento una regla que coincida con los
    hechos del usuario.
    """

    for regla in reglas:
        condiciones = regla["si"]
        coincide = True
        for condicion, valor in condiciones.items():
            # Si un hecho del usuario no coincide con la condición de
            # la regla,
            if hechos.get(condicion) != valor:
                coincide = False
                break
        
        # Si todas las condiciones coincidieron, hemos encontrado una
        # recomendación.
        if coincide:
            return regla["entonces"]
            
    return "No tenemos una recomendación para tus preferencias."

# - Ejemplo de uso -
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

# La llamada a la función para obtener la recomendación estaría aquí, por ejemplo:
# recomendacion = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
# print(f"Enfoque SE: {recomendacion}")