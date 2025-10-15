# 1. BASE DE CONOCIMIENTO (El "qué")
# Representamos el conocimiento como una lista de reglas.
# Cada regla es un diccionario con condiciones ("si") y una conclusión ("entonces").
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"},
        "entonces": "Te recomendamos un Mocha."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": False},
        "entonces": "Te recomendamos un Café Negro."
    },
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Jugo de naranja."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"},
        "entonces": "Te recomendamos un Cappuccino."
    },
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Té Helado."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"},
        "entonces": "Te recomendamos un Té de Manzanilla."
    },
    {
        "si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"},
        "entonces": "Advertencia: La cafeína en la noche puede afectar el sueño. Te recomendamos un Espresso."
    }
]

# 2. MOTOR DE INFERENCIA (El "cómo")
# Esta función no sabe nada sobre café, sólo sabe cómo aplicar reglas.
def motor_de_inferencia(hechos, reglas):
    """
    Busca en la base de conocimiento una regla que coincida con los hechos del usuario.
    """
    for regla in reglas:
        condiciones = regla["si"]
        coincide = True
        for condicion, valor in condiciones.items():
            # Si el hecho del usuario no coincide con la condición de la regla
            if hechos.get(condicion) != valor:
                coincide = False
                break
        if coincide:
            # Regresa la recomendación
            return regla["entonces"]
    return "No se encontró una recomendación."

# 3. EJEMPLO DE USO
hechos_usuario = {
    "hora_del_dia": "noche",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# 4. VENTAJA: Añadir nuevas reglas sin tocar el motor
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí", "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})
