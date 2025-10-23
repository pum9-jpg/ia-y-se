Agentes Inteligentes - Mundo de la Aspiradora
🎯 Objetivo
Simular dos tipos de agentes inteligentes que resuelven el problema clásico de limpiar dos habitaciones.

🤖 Agentes Implementados
1. Agente Reactivo Simple
Sin memoria: Solo reacciona a lo que ve en el momento

Reglas básicas:

Si está sucio → aspirar

Si está en A → ir a B

Si está en B → ir a A

2. Agente Basado en Modelos
Con memoria: Mantiene un modelo interno del mundo

Ventajas:

Recuerda el estado de ambas habitaciones

Evita movimientos innecesarios

Se detiene cuando todo está limpio

🚀 Cómo Ejecutar
bash
python practica8.py
📊 Resultados Típicos
Agente Reactivo:

Más movimientos innecesarios

Puede entrar en bucles infinitos

Rendimiento más bajo

Agente con Modelo:

Menos movimientos

Decisiones más inteligentes

Rendimiento más alto

✅ Conclusión
El agente reactivo simple actúa según lo que percibe en el instante si ve suciedad aspira si no, se mueve. Esto llega a provoca movimientos innecesarios y puede entrar en bucles porque no recuerda lo que ya hizo.
El agente basado en modelo mantiene una memoria del estado de ambas habitaciones. Gracias a esa información evita acciones redundantes, decide cuándo realmente debe moverse o detenerse y termina antes.
En resumen: recordar y modelar el entorno reduce pasos innecesarios y mejora la eficiencia, por eso el agente con modelo funciona mejor que el reactivo simple.

