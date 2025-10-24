# Recomendador de Bebidas - Enfoque Basado en Reglas

## Descripción
Este enfoque separa la **lógica (motor de inferencia)** del **conocimiento (reglas)**.  
De esta forma, las reglas pueden modificarse o ampliarse sin alterar la programación base.  
El sistema utiliza una base de conocimiento y un motor de inferencia para generar recomendaciones.

## Código
```python
# 1. Base de conocimiento
base_de_conocimiento = [
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"}, "le_gusta_dulce": True, "entonces": "Te recomendamos un Mocha."},
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"}, "le_gusta_dulce": False, "entonces": "Te recomendamos un Café Negro."},
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"}, "le_gusta_dulce": True, "entonces": "Te recomendamos un Jugo de Naranja."},
    {"si": {"hora_del_dia": "mañana", "preferencia_cafeina": "no"}, "le_gusta_dulce": False, "entonces": "Te recomendamos un Latte."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"}, "le_gusta_dulce": True, "entonces": "Te recomendamos un Frappuccino con caramelo."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "sí"}, "le_gusta_dulce": False, "entonces": "Te recomendamos un Espresso."},
    {"si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no"}, "le_gusta_dulce": True, "entonces": "Te recomendamos un Té Helado."}
]

# Reglas adicionales para la noche
reglas = [
    {"si": {"hora_del_dia": "noche", "preferencia_cafeina": "no"}, "entonces": "Te recomendamos un té de Manzanilla."},
    {"si": {"hora_del_dia": "noche", "preferencia_cafeina": "sí"}, "entonces": "Advertencia: La cafeína no te permitirá dormir. Se te recomienda un Espresso."}
]

# 2. Motor de inferencia
def motor_de_inferencia(hechos, reglas):
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

# 3. Ejemplo de uso
hechos_usuario = {
    "hora_del_dia": "noche",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(hechos_usuario, base_de_conocimiento + reglas)
print(f"Enfoque Basado en Reglas: {recomendacion_ia}")

# Ventaja: agregar nuevas bebidas sin modificar el motor
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si", "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})
```

## Ejemplo de uso
El usuario ingresa sus preferencias:
- **Hora del día:** noche  
- **Desea cafeína:** no  
- **Le gusta lo dulce:** sí  

**Resultado:**  
> Enfoque Basado en Reglas: Te recomendamos un té de Manzanilla.

## Ventajas
- Separación entre logica e informacion. 

- Facil de ampliar sin tocar el codigo.
  
- Ideal para sistemas expertos o de IA simbolica.

## Conclucion Personal
Que representa una evolución hacia un sistema más modular, adaptable y escalable, al separar la lógica del conocimiento, permite añadir o ajustar reglas sin alterar el código principal, donde el conocimiento se expande con facilidad y el mantenimiento resulta más eficiente.
