# ============================================
# SISTEMA EXPERTO BASADO EN REGLAS
# ============================================

# 1. BASE DE CONOCIMIENTO (KB)
# Representaremos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ("if") y una conclusión ("entonces").

base_de_conocimiento = [
    {
        "if": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "if": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Americano."
    },
    {
        "if": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Jugo de Naranja."
    },
    {
        "if": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Latte."
    },
    {
        "if": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Frappuccino sin café."
    },
    {
        "if": {"hora_del_dia": "tarde", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té Helado."
    },
    {
        "if": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té de Manzanilla."
    },
    {
        "if": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "entonces": "⚠️ Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso."
    }
]


# 2. MOTOR DE INFERENCIA (INFERENCE ENGINE)
# Esta función no sabe nada del dominio, sólo sabe cómo aplicar reglas.

def motor_de_inferencia(hechos, base_de_conocimiento):
    for regla in base_de_conocimiento:
        condiciones = regla["if"]
        cumple = True

        for condicion, valor in condiciones.items():
            if condicion not in hechos or hechos[condicion] != valor:
                cumple = False
                break

        if cumple:
            return regla["entonces"]

    return "No tenemos una recomendación para tus preferencias."


# 3. HECHOS DEL USUARIO (Datos de entrada)
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

# 4. EJECUCIÓN DEL MOTOR DE INFERENCIA
recomendacion_ia = motor_de_inferencia(hechos_usuario, base_de_conocimiento)

print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# ============================================
# Ventaja:
# Si queremos añadir una nueva bebida, sólo modificamos la base de conocimiento,
# el motor de inferencia no cambia.
# ============================================

base_de_conocimiento.append({
    "if": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})
