# 🧠 Recomendador de Bebidas

Este proyecto presenta dos enfoques para recomendar bebidas según las preferencias del usuario: uno basado en lógica convencional codificada directamente y otro basado en una base de conocimiento con motor de inferencia.

---


## 📌 Codigo1: El Enfoque Convencional

Este enfoque utiliza condicionales `if` para tomar decisiones directamente en el código.

### 🔧 Función principal

```python
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
    # Lógica de negocio embebida
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
## codigo 2: El Enfoque de IA (Basado en Reglas)
* Este enfoque separa el conocimiento (reglas) de la lógica (motor de inferencia), facilitando la escalabilidad y mantenimiento.
## 📚 Base de Conocimiento
```python
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí"},
        "le_gusta_dulce": True,
        "entonces": "Te recomendamos un Mocha."
    },
    ...
]
```
## ⚙️ Motor de Inferencia
```python
def motor_de_inferencia(hechos, reglas):
    for regla in reglas:
        condiciones = regla["si"]
        coincide = all(hechos.get(k) == v for k, v in condiciones.items())
        if coincide:
            return regla["entonces"]
    return "No tenemos una recomendación para tus preferencias."
```
## 🧪 Ejemplo de uso
```python
hechos_usuario = {
    "hora_del_dia": "noche",
    "preferencia_cafeina": "no",
    "le_gusta_dulce": True
}

recomendacion_ia = motor_de_inferencia(hechos_usuario, base_de_conocimiento + reglas)
print(f"Enfoque Basado en Reglas: {recomendacion_ia}")
```
## Conclusiones
* En conclusion el codigo que llegaria a ser El Enfoque Convencional llegaria a estar basado mas para casos simples, lo que dificulta su mantenimiento y expansión. Cada cambio requiere modificar el código, aumentando el riesgo de errores y limitando la flexibilidad del sistema.

* El codigo que llegaria a ser  de El Enfoque de IA (Basado en Reglas) seria un enfoque basado en reglas que separa el conocimiento de la lógica, lo que lo hace más flexible y fácil de mantener ya que las reglas son claras, editables y permiten actualizar el sistema sin tocar el código del motor.