##  Instalación de Python

Para ejecutar correctamente el programa, es necesario tener **Python 3.10 o superior** instalado en tu sistema.
Existen tres métodos recomendados:

---

# 📘 Conclusiones


## Enfoque con Reglas de Producción

## Cómo funciona
 Usa reglas del tipo SI (condiciones) → ENTONCES (conclusión). El motor de inferencia compara los síntomas del usuario con las reglas y devuelve un diagnóstico y solución.

### Características:

- Potente para razonamiento diagnóstico.

- Ideal para capturar relaciones de causa–efecto.

- Menos flexible: añadir nuevas reglas requiere modificar la base de reglas con cuidado.

### Ejemplo de uso
 > Si el usuario reporta “chasquido al pedalear” y “cadena salta” → Diagnóstico: cadena desgastada → Solución: reemplazar cadena.
---

## Enfoque con Marcos (Frames)

### Cómo funciona
 Representa el conocimiento como objetos estructurados (frames). Cada frame describe un problema con sus atributos: síntomas, solución y herramientas necesarias.

### Características:

- Excelente para organizar conocimiento descriptivo.

- Muy flexible: se pueden añadir nuevos atributos o frames sin afectar a los demás.

- Ideal para consultas rápidas y estructuradas.

### Ejemplo de uso
 > Problema de transmisión → Síntomas: cadena salta → Solución: reemplazar cadena → Herramientas: desarmador, cadena nueva.
 ---