# --- Enfoque Convencional ---
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    
    # --- Recomienda una bebida basándose en la lógica de negocio directamente en el código. ---
    
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'sí':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else:
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'sí':
            return "Te recomendamos un Latte."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Té Chai."
            else:
                return "Te recomendamos un Té Verde."

# --- Enfoque Basado en Reglas ---
reglas_bebidas = [
    {"condiciones": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": True}, "bebida": "Mocha"},
    {"condiciones": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "le_gusta_dulce": False}, "bebida": "Americano"},
    {"condiciones": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"}, "bebida": "Jugo de Naranja"},
    {"condiciones": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"}, "bebida": "Latte"},
    {"condiciones": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True}, "bebida": "Té Chai"},
    {"condiciones": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": False}, "bebida": "Té Verde"},
]

def recomendar_bebida_por_reglas(preferencias):
    for regla in reglas_bebidas:
        condiciones = regla["condiciones"]
        if all(preferencias.get(k) == v for k, v in condiciones.items()):
            return f"Te recomendamos un {regla['bebida']}."
    return "No se encontró una bebida adecuada para tus preferencias."

# --- Ejemplo de uso ---
preferencias_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

# Resultados
recomendacion_convencional = recomendar_bebida_convencional(
    preferencias_usuario["hora_del_dia"],
    preferencias_usuario["preferencia_cafeina"],
    preferencias_usuario["le_gusta_dulce"]
)

recomendacion_reglas = recomendar_bebida_por_reglas(preferencias_usuario)

print(f"Enfoque Convencional: {recomendacion_convencional}")
print(f"Enfoque Basado en Reglas: {recomendacion_reglas}")