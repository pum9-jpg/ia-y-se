class SistemaExperto:
    def __init__(self, reglas):
        # 1. Separación: El conocimiento se pasa al sistema, no está dentro de él.
        self.reglas = reglas
        self.hechos = set()
        # Para la explicación, guardamos qué regla generó cada hecho.
        self.historial_inferencia = {}
    
    def razonar(self, hechos_iniciales):
        """
        Este es el MOTOR DE INFERENCIA.
        Utiliza un algoritmo de encadenamiento hacia adelante.
        """
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True
        
        print("- Proceso de Razonamiento - ")
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                
                # Si las condiciones de la regla están en nuestros hechos y la conclusión no lo está.
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]  # Guardamos para la explicación
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: '{regla['nombre']}')")
                    nuevos_hechos_encontrados = True
        print("- Fin del Proceso de Razonamiento - ")
        return self.hechos
    
    def obtener_diagnosticos_finales(self):
        """Filtra los hechos para mostrar solo los diagnósticos finales."""
        return [hecho for hecho in self.hechos if hecho.startswith('diagnostico_')]
    
    def explicar_conclusion(self, conclusion):
        """
        2. Característica Distintiva: Capacidad de explicación.
        Muestra cómo se llegó a una conclusión específica.
        """
        if conclusion not in self.historial_inferencia:
            if conclusion in self.hechos:
                return f"La conclusión '{conclusion}' fue un hecho inicial."
            else:
                return f"No se pudo determinar cómo se llegó a la conclusión '{conclusion}'."
        
        regla_que_lo_genero = self.historial_inferencia[conclusion]
        
        # Busca la regla completa para mostrar sus condiciones
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
        condiciones = regla_completa["si"]
        
        explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
        explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, ENTONCES se deduce '{conclusion}'.\n"
        
        # Recursivamente, explica cómo se obtuvieron las condiciones
        for condicion in condiciones:
            explicacion += self.explicar_conclusion(condicion)
        
        return explicacion