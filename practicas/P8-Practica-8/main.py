# Paso 4: Ejecutar y Comparar las Simulaciones

from entorno_aspiradora import EntornoAspiradora
from agente_reactivo import AgenteReactivoSimple
from agente_modelos import AgenteBasadoEnModelos

# - Simulación 1: Agente Reactivo Simple -
print("=" * 50)
print("- Probando Agente Reactivo Simple -")
print("=" * 50)
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

# - Simulación 2: Agente Basado en Modelos -
print("=" * 50)
print("- Probando Agente Basado en Modelos -")
print("=" * 50)
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)

# - Comparación de Resultados -
print("=" * 50)
print("- RESUMEN COMPARATIVO -")
print("=" * 50)
print("Agente Reactivo Simple:")
print(f"  - Pasos: {entorno1.pasos}")
print(f"  - Rendimiento: {entorno1.rendimiento}")

print("\nAgente Basado en Modelos:")
print(f"  - Pasos: {entorno2.pasos}")
print(f"  - Rendimiento: {entorno2.rendimiento}")