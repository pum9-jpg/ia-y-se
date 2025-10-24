# 1. BASE DE CONOCIMIENTO (El "qué")
# Representamos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ("si") y una conclusión ("entonces").
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"},
        "le_gusta_dulce": True,
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"},
        "le_gusta_dulce": False,
        "entonces": "Te recomendamos un Café Negro."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "le_gusta_dulce": True,
        "entonces": "Te recomendamos un Jugo de Naranja."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "le_gusta_dulce": False,
        "entonces": "Te recomendamos un Latte."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"},
        "le_gusta_dulce": True,
        "entonces": "Te recomendamos un Frappuccino con caramelo."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"},
        "le_gusta_dulce": False,
        "entonces": "Te recomendamos un Espresso."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no"},
        "le_gusta_dulce": True,
        "entonces": "Te recomendamos un Té Helado."
    }
]

# También se añaden reglas para la noche
reglas = [
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un té de Manzanilla."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "entonces": "Advertencia: La cafeína no te permitirá dormir. Se te recomienda un Espresso."
    }
]

# 2. MOTOR DE INFERENCIA (El "cómo")
# Esta función no sabe nada sobre café, solo sabe cómo aplicar reglas.
def motor_de_inferencia(hechos, reglas):
    """
    Busca en la base de conocimiento una regla que coincida con los hechos del usuario.
    """
    for regla in reglas:
        condiciones = regla["si"]
        coincide = True
        for condición, valor in condiciones.items():
            if hechos.get(condición) != valor:
                coincide = False
                break
        if coincide:
            return regla["entonces"]
    return "No tenemos una recomendación para tus preferencias."

# 3. EJEMPLO DE USO
hechos_usuario = {
    "hora_del_dia": "noche",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(hechos_usuario, base_de_conocimiento + reglas)
print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# - Ventaja -
# Si queremos añadir una nueva bebida, solo modificamos la base de conocimiento.
# El motor de inferencia no cambia.
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si", "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})