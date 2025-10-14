Ejemplo de salida:
text
Enfoque Convencional: Te recomendamos un Frappuccino sin café.
Enfoque Basado en Reglas: Te recomendamos un Frappuccino sin café.
Explicación detallada del código:
Parte 1: Enfoque Convencional
python
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce):
Esta función toma 3 parámetros y usa condiciones anidadas (if-elif-else) para decidir qué bebida recomendar.

Ejemplo con nuestros datos:

hora_del_dia = "tarde"

preferencia_cafeina = "no"

le_gusta_dulce = True

Recorre este camino:

¿Es mañana? ❌ No

¿Es tarde? ✅ Sí

¿Quiere cafeína? ❌ No

¿Le gusta dulce? ✅ Sí

Resultado: "Te recomendamos un Frappuccino sin café."

Parte 2: Enfoque de IA (Basado en Reglas)
Base de Conocimiento:
python
base_de_conocimiento = [
    {
        "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
        "entonces": "Te recomendamos un Frappuccino sin café."
    },
    # ... más reglas
]
Es una lista de reglas tipo "SI estas condiciones SE CUMPLEN, ENTONCES recomienda esto".

Motor de Inferencia:
python
def motor_de_inferencia(hechos, reglas):
Esta función busca patrones - compara los hechos del usuario con cada regla hasta encontrar una que coincida completamente.

Con nuestros datos:

python
hechos_usuario = {
    "hora_del_dia": "tarde",
    "preferencia_cafeina": "no", 
    "le_gusta_dulce": True
}
El motor:

Toma la primera regla → No coincide

Toma la segunda regla → No coincide

...

Llega a la regla 5: ✅ ¡Coincide perfectamente!

Devuelve: "Te recomendamos un Frappuccino sin café."

¿Por qué ambos enfoques dan el mismo resultado?
Porque ambos implementan la misma lógica de negocio, pero de forma diferente:

Convencional: Lógica hardcodeada en if/else

IA basada en reglas: Lógica separada en datos (base de conocimiento) + motor genérico

Ventaja del enfoque IA:
Si quiero agregar una nueva bebida, solo añado una regla a la base de conocimiento:

python
base_de_conocimiento.append({
    "si": {"hora_del_dia": "mañana", "preferencia_cafeina": "sí", "es_fin_de_semana": True},
    "entonces": "Te recomendamos un Cappuccino especial de fin de semana."
})
¡El motor de inferencia NO necesita cambios! Mientras que en el enfoque convencional tendría que modificar la función.

¿Te queda claro cómo funciona cada parte?

puedes darme un readme en formato markdown
Sistema de Recomendación de Bebidas
📋 Descripción
Este proyecto implementa un sistema de recomendación de bebidas usando dos enfoques diferentes:

Enfoque Convencional: Lógica programada directamente con estructuras condicionales

Enfoque de IA Basado en Reglas: Sistema inteligente que separa el conocimiento del razonamiento

🎯 Objetivos
Demostrar la diferencia entre programación convencional y sistemas basados en reglas

Mostrar cómo los sistemas de IA separan el conocimiento del motor de inferencia

Proporcionar un ejemplo práctico de sistema experto simple

🏗️ Arquitectura del Sistema
Enfoque Convencional
text
Entrada → Función con if/else → Recomendación
Enfoque Basado en Reglas
text
Entrada → Motor de Inferencia → Base de Conocimiento → Recomendación
📁 Estructura del Código
1. Función Convencional (recomendar_bebida_convencional)
python
def recomendar_bebida_convencional(hora_del_dia, preferencia_cafeina, le_gusta_dulce)
Lógica hardcodeada en estructuras if/elif/else

Fácil de entender pero difícil de mantener y extender

Cambios requieren modificar el código directamente

2. Sistema Basado en Reglas
Base de Conocimiento
python
base_de_conocimiento = [
    {
        "si": {"condiciones"},
        "entonces": "recomendación"
    }
]
Conocimiento declarativo: Representa el "QUÉ" sabemos

Fácil de modificar: Añadir nuevas reglas sin cambiar la lógica

Ejemplo de regla:

python
{
    "si": {"hora_del_dia": "tarde", "preferencia_cafeina": "no", "le_gusta_dulce": True},
    "entonces": "Te recomendamos un Frappuccino sin café."
}
Motor de Inferencia
python
def motor_de_inferencia(hechos, reglas)
Lógica genérica: No sabe nada sobre bebidas

Busca patrones: Compara hechos con condiciones de las reglas

Separación de concerns: Conocimiento y razonamiento separados

🚀 Cómo Usar
Ejecución Básica
bash
python practica3.py
Personalizar Recomendaciones
Modifica el diccionario de preferencias:

python
hechos_usuario = {
    "hora_del_dia": "mañana",  # Opciones: 'mañana', 'tarde', 'noche'
    "preferencia_cafeina": "sí",  # Opciones: 'sí', 'no'
    "le_gusta_dulce": True  # Opciones: True, False
}
📊 Reglas de Recomendación
Hora	Cafeína	Dulce	Recomendación
Mañana	Sí	Sí	Mocha
Mañana	Sí	No	Americano
Mañana	No	-	Jugo de Naranja
Tarde	Sí	-	Latte
Tarde	No	Sí	Frappuccino sin café
Tarde	No	No	Té Helado
Noche	Sí	-	Espresso (con advertencia)
Noche	No	-	Té de Manzanilla
🔧 Extender el Sistema
Añadir Nueva Regla
python
base_de_conocimiento.append({
    "si": {
        "hora_del_dia": "tarde",
        "preferencia_cafeina": "sí", 
        "le_gusta_leche": False
    },
    "entonces": "Te recomendamos un Café Cold Brew."
})
Añadir Nuevo Atributo
Actualizar la base de conocimiento con nuevas condiciones

El motor de inferencia funciona automáticamente

💡 Conceptos de IA Aplicados
Sistema Basado en Reglas
Base de Conocimiento: Hechos y reglas del dominio

Motor de Inferencia: Algoritmo de pattern matching

Separación: Conocimiento declarativo vs. razonamiento procedural

Ventajas del Enfoque IA
✅ Mantenible: Cambios solo en la base de conocimiento

✅ Extensible: Nuevas reglas sin modificar el motor

✅ Explicable: Fácil entender por qué se tomó una decisión

✅ Modular: Motor reusable para otros dominios

🧪 Ejemplos de Salida
Ejemplo 1: Tarde sin cafeína
text
Enfoque Convencional: Te recomendamos un Frappuccino sin café.
Enfoque Basado en Reglas: Te recomendamos un Frappuccino sin café.
Ejemplo 2: Noche con cafeína
text
Advertencia: La cafeína por la noche puede afectar el sueño.
Enfoque Convencional: Te recomendamos un Espresso.
Enfoque Basado en Reglas: Advertencia: La cafeína por la noche puede afectar el sueño. Te recomendamos un Espresso.
🛠️ Requisitos
Python 3.6+

No se requieren librerías externas

📝 Notas de Implementación
El sistema es determinístico: mismas entradas → misma salida

Manejo de casos borde: Regla por defecto cuando no hay coincidencias

Advertencias: El sistema alerta sobre cafeína en la noche

🎓 Aprendizajes Clave
Separación de concerns mejora la mantenibilidad

Sistemas basados en reglas son explicables y modificables

Pattern matching es fundamental en IA simbólica

Conocimiento declarativo permite actualizaciones sin reprogramar

🔮 Posibles Mejoras
Interfaz gráfica de usuario

Base de conocimiento en archivo externo (JSON)

Sistema de aprendizaje de preferencias

Integración con API de clima

Historial de recomendaciones

