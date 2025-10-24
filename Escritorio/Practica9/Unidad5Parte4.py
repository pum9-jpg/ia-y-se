# - Simulación 1: Agente Reactivo Simple -
print("-    Probando Agente Reactivo Simple -")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

# - Simulación 2: Agente Basado en Modelos -
print("-    Probando Agente Basado en Modelos -")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)