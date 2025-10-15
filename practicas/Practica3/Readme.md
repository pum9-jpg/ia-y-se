#  Comparación de Enfoques: Recomendador de Bebidas en Python

## Objetivo

Demostrar dos enfoques de programación para resolver el mismo problema: recomendar una bebida en una cafetería según las preferencias del usuario. Se comparan:

- **Enfoque Convencional**: lógica embebida directamente en el código.
- **Enfoque Basado en Reglas**: lógica separada del conocimiento, usando estructuras de datos.

---

## Enfoque Convencional

### Descripción

La lógica de decisión está codificada directamente en la función. Si cambian las reglas, se debe modificar el código fuente.

## Cómo Ejecutar el Programa

Asegúrate de tener Python instalado en tu sistema.

Abre una terminal o consola y navega hasta el directorio donde guardaste el archivo.

Ejecuta el script con el siguiente comando:

### bash
---- python practica_3.py
### Código


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
    
## Conclusiones
- El enfoque convencional es útil para sistemas simples, pero se vuelve rígido y difícil de mantener cuando se requiere flexibilidad o expansión.
- El enfoque basado en reglas permite separar la lógica de decisión del conocimiento, lo que facilita el mantenimiento, la escalabilidad y la adaptación a nuevos escenarios.
- Este tipo de estructura es ideal para sistemas expertos, asistentes inteligentes y aplicaciones educativas donde el conocimiento puede cambiar con frecuencia.
- Elegir el enfoque adecuado depende del contexto, pero para sistemas dinámicos y evolutivos, el enfoque basado en reglas ofrece claras ventajas