
# Sistema de Recomendación de Bebidas

Este proyecto contiene dos implementaciones de un sistema de recomendación de bebidas basado en preferencias del usuario.

## 📁 Implementaciones

### 1. Enfoque Convencional (`recomendar_bebida_convencional`)
- Lógica de negocio embebida en el código
- Estructura condicional if-elif-else
- Más simple pero menos mantenible

### 2. Enfoque Basado en Reglas (`motor_de_inferencia`)
- Separación entre conocimiento y razonamiento
- Base de conocimiento modificable
- Motor de inferencia reutilizable
- Más mantenible y escalable

---

## 🎯 Descripción del Sistema

El sistema recomienda bebidas según tres criterios:
- **Hora del día** (mañana, tarde o noche)
- **Preferencia por cafeína** (sí o no)
- **Gusto por bebidas dulces** (True o False)

---

## 🚀 Uso

### Enfoque Convencional
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
```

### Enfoque Basado en Reglas
```python
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no", 
    "le_gusta_dulce": True
}

recomendacion = motor_de_inferencia(hechos_usuario, base_de_conocimiento)
```

---

## ✨ Comparación de Enfoques

| Aspecto | Enfoque Convencional | Enfoque Basado en Reglas |
|---------|---------------------|-------------------------|
| Mantenibilidad | Baja | Alta |
| Flexibilidad | Baja | Alta |
| Separación de concerns | No | Sí |
| Reutilización | Limitada | Alta |
| Complejidad | Simple | Moderada |

---

## 🛠️ Requisitos

- Python 3.x
- No se requieren dependencias externas
