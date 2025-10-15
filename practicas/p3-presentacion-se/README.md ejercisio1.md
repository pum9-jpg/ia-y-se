# Recomendador de Bebidas - Enfoque Convencional

## Descripción
Este enfoque implementa la lógica de recomendación directamente en el código.  
Dependiendo de la hora del día, la preferencia por cafeína y el gusto por lo dulce,  
el sistema sugiere una bebida específica según una estructura condicional.

## Código
```python
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    """
    Recomienda una bebida basándose en la lógica de negocio directamente en el código.
    """
    if hora_del_dia == 'mañana':
        if preferencia_cafeina == 'si':
            if le_gusta_dulce:
                return "Te recomendamos un Mocha."
            else:
                return "Te recomendamos un Americano."
        else:
            return "Te recomendamos un Jugo de Naranja."
    elif hora_del_dia == 'tarde':
        if preferencia_cafeina == 'si':
            return "Te recomendamos un Latte."
        else:
            if le_gusta_dulce:
                return "Te recomendamos un Frappuccino sin café."
            else:
                return "Te recomendamos un Té Helado."
    elif hora_del_dia == 'noche':
        if preferencia_cafeina == 'si':
            print("Advertencia: La cafeína por la noche puede afectar el sueño.")
            return "Te recomendamos un Espresso."
        else:
            return "Te recomendamos un Té de Manzanilla."
    else:
        return "No tenemos una recomendación para ese momento del día."

# Ejemplo de uso
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

## Ejemplo de uso
El usuario ingresa sus preferencias:
- **Hora del día:** tarde  
- **Desea cafeína:** no  
- **Le gusta lo dulce:** sí  

**Resultado:**  
> Enfoque Convencional: Te recomendamos un Frappuccino sin café.

## Observaciones
Este método es funcional pero poco flexible.  
Si se desea agregar nuevas condiciones o bebidas, se debe modificar directamente el código.

## Conclucion Personal
Es sencillo y directo, ideal para sistemas pequeños o con reglas fijas, sin embargo, su principal limitación es la falta de flexibilidad: cada nueva condición o cambio en la lógica requiere modificar el código fuente haciendolo menos escalable y más propenso a errores a medida que el sistema crece.
