# Sistema de Diagnóstico de Bicicletas - Dos Enfoques de IA

## Descripción General

Este proyecto implementa un sistema de diagnóstico para problemas de bicicletas utilizando dos enfoques diferentes de representación del conocimiento en Inteligencia Artificial. Ambos sistemas toman síntomas reportados por el usuario y devuelven diagnósticos y soluciones para problemas comunes de bicicletas.

---

## Enfoque 1: Sistema Basado en Reglas de Producción

### ¿Qué hace este código?
Este sistema utiliza un enfoque de reglas "SI-ENTONCES" para el diagnóstico. Consta de dos bases de conocimiento separadas:

- **Base de reglas de diagnóstico**: Relaciona síntomas con problemas
- **Base de reglas de solución**: Relaciona diagnósticos con soluciones

### Flujo de ejecución:
1. **Recibe síntomas** del usuario (ej: `["chasquido_al_pedalear", "cadena_salta"]`)
2. **Busca en las reglas de diagnóstico** una que coincida con todos los síntomas
3. **Si encuentra diagnóstico**, busca en las reglas de solución la correspondiente
4. **Retorna ambos resultados**: diagnóstico y solución

### Ejemplo de funcionamiento:
```
Input: ["chasquido_al_pedalear", "cadena_salta"]
Output: 
Diagnóstico encontrado: diagnostico_cadena_desgastada
Solución encontrada: solucion_reemplazar_cadena
```

### Conclusión:
Este código implementa un **sistema experto clásico** donde el conocimiento está explícitamente separado en reglas. La función `diagnosticar_con_reglas` actúa como un motor de inferencia que aplica estas reglas en dos fases: primero diagnostica el problema, luego busca la solución correspondiente. Es un enfoque **modular** donde agregar nuevos problemas requiere añadir reglas tanto de diagnóstico como de solución.

---

## Enfoque 2: Sistema Basado en Marcos (Frames)

### ¿Qué hace este código?
Este sistema utiliza una representación orientada a objetos del conocimiento mediante "frames" (marcos). Cada problema se representa como un objeto completo con múltiples atributos:

- **Tipo de problema** (`es_un`)
- **Síntomas** que lo caracterizan
- **Solución** recomendada
- **Herramientas necesarias** para la reparación

### Flujo de ejecución:
1. **Recibe síntomas** del usuario
2. **Busca en todos los frames** aquel cuyo conjunto de síntomas coincida completamente
3. **Si encuentra coincidencia**, retorna el nombre del problema y todos sus detalles
4. **Presenta información completa** en un formato estructurado

### Ejemplo de funcionamiento:
```
Input: ["chasquido_al_pedalear", "cadena_salta"]
Output:
Problema identificado: cadena_desgastada
 -> Es un tipo de: problema_de_transmision
 -> La solución es: reemplazar_cadena
 -> Necesitarás: cortacadenas, cadena_nueva
```

### Conclusión:
Este código implementa un **sistema de conocimiento basado en objetos** donde cada problema es una entidad completa con múltiples atributos interrelacionados. La función `buscar_problema_por_sintoma` realiza una búsqueda exhaustiva comparando los síntomas del usuario con los de cada frame. La principal ventaja es que **toda la información relevante** sobre un problema está agrupada en una sola estructura, haciendo que el output sea más informativo y útil para el usuario final.

---

## Comparación de Flujos

### Sistema de Reglas:
```
Síntomas → Reglas Diagnóstico → Diagnóstico → Reglas Solución → Solución
```

### Sistema de Marcos:
```
Síntomas → Búsqueda en Frames → Problema + Todos sus Atributos
```

---

## Conclusión General

**El sistema de Reglas** funciona como un **proceso de dos pasos** donde el conocimiento está dividido y se aplica secuencialmente. Es como tener un manual de diagnóstico separado de un manual de reparación.

**El sistema de Marcos** funciona como una **base de datos de problemas** donde cada entrada contiene toda la información relevante. Es como tener fichas técnicas completas para cada problema.

Ambos sistemas logran el mismo objetivo (diagnosticar problemas de bicicletas) pero con filosofías diferentes: uno mediante aplicación secuencial de reglas y otro mediante búsqueda en estructuras de conocimiento completas.