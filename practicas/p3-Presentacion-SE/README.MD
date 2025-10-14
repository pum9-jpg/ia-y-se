# ☕ Sistema de Recomendación de Bebidas en Python

Este proyecto presenta dos enfoques para recomendar bebidas según las preferencias del usuario: uno basado en condicionales tradicionales y otro mediante un motor de inferencia con reglas. Ambos están escritos en Python y permiten personalizar la recomendación según la hora del día, la preferencia por cafeína y el gusto por lo dulce.

---

## 🧠 Enfoque 1: Lógica Convencional

* La función `recomendar_bebida_convencional` utiliza condicionales anidados para tomar decisiones directamente en el código.

### 📄 Código principal

```python
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    """
    Recomienda una bebida basándose en la lógica de negocio
    directamente en el código.
    """
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'sí':
            return "Te recomendamos un Café."
        else:
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'sí':
            return "Te recomendamos un Americano."
        else:
            return "Te recomendamos un Latte."
    elif hora_del_dia == 'noche':
        if le_gusta_dulce:
            return "Te recomendamos un Frappuccino sin café."
        else:
            return "Te recomendamos un Té Helado."
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'sí':
            print("Advertencia: La cafeína por la noche puede afectar el sueño.")
            return "Te recomendamos un Espresso."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Té de Manzanilla."
            else:
                return "No tenemos una recomendación para ese momento del día."
```

## 🧪 Ejemplo de uso

```python
preferencias_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion = recomendar_bebida_convencional(
    preferencias_usuario["hora_del_dia"],
    preferencias_usuario["preferencia_cafeina"],
    preferencias_usuario["le_gusta_dulce"]
)

print(f"Enfoque Convencional: {recomendacion}")


```

## 🧠 Enfoque 2: Motor de Inferencia Basado en Reglas
* Este enfoque separa el conocimiento (reglas) de la lógica (motor de inferencia), permitiendo modificar las recomendaciones sin alterar el código que las aplica.
base_de_conocimiento = [
```python    
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


todas_las_reglas = base_de_conocimiento + reglas_noche

```


## ⚙️ Motor de inferencia
```python
def motor_de_inferencia(reglas, hechos_del_usuario):
    for regla in reglas:
        condiciones = regla["si"]
        hechos_coinciden = True
        for condicion, valor in condiciones.items():
            if hechos_del_usuario.get(condicion) != valor:
                hechos_coinciden = False
                break
        if hechos_coinciden:
            return regla["entonces"]
    return "No se encontró una recomendación."
```

### 🧪 Ejemplo de uso

```python
hechos_del_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(todas_las_reglas, hechos_del_usuario)

print(f"Enfoque Basado en Reglas: {recomendacion_ia}")
```

### ➕ Añadir nuevas reglas
```python
base_de_conocimiento.append({
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "si", "le_gusta_leche": False},
    "entonces": "Te recomendamos un Café Cold Brew."
})

```

## Conclusión 
* El enfoque convencional va mas apegado para sistemas pequeños y rapidos, pero requiere una estructura clara en las reglas, mientras que el enfoque basado en reglas es ideal para sistemas un poco mas complejos que necesitan crecer o adaptarse sin tocar la logica.