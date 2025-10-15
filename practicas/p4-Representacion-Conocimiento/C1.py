# Código Python Basado en Reglas

# 1. BASE DE CONOCIMIENTO (o "reglas")
# Se representa el conocimiento como una lista de reglas.
# Cada regla tiene condiciones ("si") y un resultado ("entonces").

base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
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
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "advertencia": "Advertencia: La cafeína por la noche puede afectar el sueño.",
        "entonces": "Te recomendamos un Espresso."
    }
]

# 2. MOTOR DE INFERENCIA (la lógica)
# Esta función analiza los hechos y determina qué regla aplicar.

def motor_de_inferencia(hechos_usuario, reglas):
    """
    Busca en la base de conocimiento una regla que coincida con los hechos del usuario.
    """
    for regla in reglas:
        condiciones = regla["si"]
        cumple = True
        for condicion, valor in condiciones.items():
            if condicion not in hechos_usuario or hechos_usuario[condicion] != valor:
                cumple = False
                break
        if cumple:
            if "advertencia" in regla:
                print(regla["advertencia"])
            return regla["entonces"]
    return "No tenemos una recomendación para tus preferencias."


# Ejemplo de uso
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
print(f"Recomendación Basada en Reglas: {recomendacion}")

# Verificación adicional
hechos_usuario = {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"}
print(f"Nueva recomendación: {motor_de_inferencia(hechos_usuario, base_de_conocimiento)}")
