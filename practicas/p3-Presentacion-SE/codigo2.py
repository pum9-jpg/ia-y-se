# 1. BASE DE CONOCIMIENTO (El "qué")
# Representamos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ('si') y una conclusión ('entonces').
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Café Negro."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Jugo de Naranja."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Latte Vainilla."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Frappuccino sin café."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Té Helado."
    }
]

# Reglas adicionales para la noche
reglas_noche = [
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té de Manzanilla."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "entonces": "Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."
    }
]

# Combinamos todas las reglas en una sola lista
todas_las_reglas = base_de_conocimiento + reglas_noche

# 2. MOTOR DE INFERENCIA (El "cómo")
# Esta función no sabe nada sobre café, sólo sabe cómo aplicar reglas.
def motor_de_inferencia(reglas, hechos_del_usuario):
    """
    Busca en la base de conocimiento una regla que coincida con los hechos del usuario.
    """
    for regla in reglas:
        condiciones = regla["si"]
        hechos_coinciden = True
        for condicion, valor in condiciones.items():
            if hechos_del_usuario.get(condicion) != valor:
                hechos_coinciden = False
                break
        # Si todas las condiciones coinciden (hechos coinciden con la regla),
        # esta regla es la que aplica.
        if hechos_coinciden:
            return regla["entonces"]
    return "No se encontró una recomendación."

# 3. Ejemplo de uso
hechos_del_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(todas_las_reglas, hechos_del_usuario)

print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# - Ventaja -
# Si queremos añadir una nueva bebida, solo modificamos la base de conocimiento.
# El motor de inferencia no cambia.
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si", "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})
             