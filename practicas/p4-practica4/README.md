README - Sistema Experto para Diagnóstico de Problemas en Bicicletas
📋 Descripción del Proyecto
Este proyecto implementa un sistema experto para diagnosticar problemas comunes en bicicletas utilizando dos enfoques diferentes de representación del conocimiento: Reglas de Producción y Marcos (Frames).

🎯 Objetivo
Demostrar cómo el conocimiento de un experto en reparación de bicicletas puede ser formalizado en formatos que una computadora pueda procesar, aplicando los conceptos de la Ingeniería del Conocimiento.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.x

Enfoques de Representación:

Reglas de Producción (IF-THEN)

Marcos (Frames) - Representación orientada a objetos

📁 Estructura del Código
Parte 1: Representación mediante Reglas de Producción
python
# Base de conocimiento para diagnóstico
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
}

# Base de conocimiento para soluciones
base_conocimiento_soluciones = {
    "regla_3": {
        "si": ["diagnostico_ponchadura"],
        "entonces": "solucion_parchar_o_cambiar_tubo"
    },
    "regla_4": {
        "si": ["diagnostico_cadena_desgastada"],
        "entonces": "solucion_reemplazar_cadena"
    }
}
Parte 2: Representación mediante Marcos (Frames)
python
base_conocimiento_frames = {
    "ponchadura": {
        "es_un": "problema_de_llanta",
        "sintomas": ["llanta_blanda"],
        "solucion": "parchar_o_cambiar_tubo",
        "herramientas_necesarias": ["bomba_de_aire", "parches", "pegamento"]
    },
    "cadena_desgastada": {
        "es_un": "problema_de_transmision",
        "sintomas": ["chasquido_al_pedalear", "cadena_salta"],
        "solucion": "reemplazar_cadena",
        "herramientas_necesarias": ["cortacadenas", "cadena_nueva"]
    }
}
🚀 Cómo Ejecutar el Proyecto
Prerrequisitos
Python 3.x instalado

No se requieren librerías externas

Pasos para ejecutar:
Clonar o descargar el código

bash
git clone <url-del-repositorio>
cd sistema-experto-bicicletas
Ejecutar el script

bash
python sistema_experto_bicicletas.py
Salida esperada

text
- Usando Reglas de Producción - 
Diagnóstico encontrado: diagnostico_cadena_desgastada
Solución encontrada: solucion_reemplazar_cadena

- Usando Marcos (Frames) - 
Problema identificado: cadena_desgastada
 Es un tipo de: problema_de_transmision
 La solución es: reemplazar_cadena
 Necesitarás: cortacadenas, cadena_nueva
📊 Conocimiento del Experto Representado
El sistema captura el siguiente conocimiento del experto:

Problemas Diagnosticados:
Ponchadura

Síntoma: Llanta blanda

Solución: Parchar o cambiar el tubo

Herramientas: Bomba de aire, parches, pegamento

Categoría: Problema de llanta

Cadena Desgastada

Síntomas: Chasquido al pedalear, cadena salta

Solución: Reemplazar la cadena

Herramientas: Cortacadenas, cadena nueva

Categoría: Problema de transmisión

🔍 Funcionalidades Principales
1. Sistema de Reglas de Producción
Diagnóstico basado en síntomas: Aplica reglas IF-THEN para inferir problemas

Modularidad: Cada regla es independiente y fácil de modificar

Encadenamiento hacia adelante: De síntomas a diagnóstico y solución

2. Sistema de Marcos (Frames)
Representación estructurada: Organiza el conocimiento en objetos con atributos

Consultas descriptivas: Proporciona información completa sobre cada problema

Jerarquías: Soporta relaciones "es_un" para categorización

📈 Análisis de los Enfoques
✅ Ventajas de las Reglas de Producción
Intuitivas: Se asemejan al razonamiento humano

Modulares: Fácil agregar nuevas reglas sin afectar las existentes

Ideales para diagnóstico: Excelentes para lógica condicional

✅ Ventajas de los Marcos (Frames)
Estructurados: Agrupan toda la información relacionada

Flexibles: Fácil agregar nuevos atributos

Jerárquicos: Soportan herencia y categorización

🎓 Conceptos de Ingeniería del Conocimiento Aplicados
Adquisición del Conocimiento: Extracción del conocimiento del experto

Representación del Conocimiento: Formalización en estructuras computables

Sistemas Expertos: Aplicación práctica del conocimiento para resolver problemas

Razonamiento Automatizado: Inferencia de conclusiones basadas en evidencia

🔮 Posibles Extensiones
Ampliar la base de conocimiento con más problemas:

Problemas de frenos

Problemas de cambios

Problemas de dirección

Interfaz de usuario:

Aplicación web o móvil

Formulario interactivo de síntomas

Características avanzadas:

Sistema de aprendizaje automático

Base de datos de soluciones

Sistema de recomendaciones de repuestos

👥 Contribuciones
Las contribuciones son bienvenidas. Algunas áreas de mejora:

Agregar más reglas y frames para otros problemas comunes

Mejorar la interfaz de usuario

Implementar un motor de inferencia más sofisticado

📝 Licencia
Este proyecto es con fines educativos como parte del estudio de Sistemas Expertos e Ingeniería del Conocimiento.


