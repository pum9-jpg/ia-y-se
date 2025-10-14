def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    """
    Recomienda una bebida basándose en la lógica de negocio
    directamente en el código.
    """
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'sí':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else: # No quiere cafeína por la mañana
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'sí':
            return "Te recomendamos un Latte."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Frappuccino sin café."
            else:
                return "Te recomendamos un Té Helado."
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'sí':
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

recomendacion = recomendar_bebida_convencional(preferencias_usuario["hora_del_dia"],
                                              preferencias_usuario["preferencia_cafeina"],
                                              preferencias_usuario["le_gusta_dulce"])

print(f"Enfoque Convencional: {recomendacion}")

# Parte 2: El Enfoque de IA (Basado en Reglas)

# 1. BASE DE CONOCIMIENTO (El "qué")
# Representamos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ('si') y una
# conclusión ('entonces').
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí",
               "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí",
               "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Americano."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Jugo de Naranja."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"},
        "entonces": "Te recomendamos un Latte."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no",
               "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Frappuccino sin café."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no",
               "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Té Helado."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té de Manzanilla."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "entonces": "Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."
    }
]

# 2. MOTOR DE INFERENCIA (El "cómo")
# Esta función no sabe nada sobre café, solo sabe cómo aplicar
# reglas.
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
                # esta regla no se aplica.
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

recomendacion_ia = motor_de_inferencia(hechos_usuario,
                                       base_de_conocimiento)
print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# Ventaja -
# Si queremos añadir una nueva bebida, solo modificamos la base de
# conocimiento.
# El motor de inferencia no cambia.
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí",
           "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})