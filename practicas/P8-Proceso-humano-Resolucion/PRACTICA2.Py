import random
# (Asumimos que la clase EntornoAspiradora está definida aquí o importada)

# =======================================================================
# Definición del Agente Reactivo Simple
# =======================================================================

class AgenteReactivoSimple:
    """
    Un agente cuya acción solo depende de la percepción actual.
    """
    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        
        # 1. Si está Sucio, aspira.
        if estado == 'Sucia':
            return 'aspirar'
        
        # 2. Si está Limpio, se mueve al otro lado.
        elif ubicacion == 'A':
            return 'ir_a_B'
        
        elif ubicacion == 'B':
            return 'ir_a_A'
            
# =======================================================================
# Definición del Agente Basado en Modelos
# =======================================================================

class AgenteBasadoEnModelos:
    """
    Un agente que mantiene un estado interno (modelo) del mundo.
    """
    def __init__(self):
        # El modelo interno del agente. Inicialmente no sabe nada.
        self.modelo = {'A': 'Desconocido', 'B': 'Desconocido'}

    def actuar(self, percepcion):
        ubicacion, estado = percepcion

        # 1. Actualiza su modelo interno con la nueva percepción.
        self.modelo[ubicacion] = estado

        # 2. Toma una decisión basada en su modelo actualizado.
        
        # A. Si la ubicación actual está sucia, aspira (Alta Prioridad).
        if estado == 'Sucia':
            return 'aspirar'
            
        # B. Si el modelo indica que la otra habitación está sucia, se dirige a ella.
        elif self.modelo['A'] == 'Sucia' and ubicacion == 'B':
            return 'ir_a_A'
            
        elif self.modelo['B'] == 'Sucia' and ubicacion == 'A':
            return 'ir_a_B'
            
        # C. Si su modelo dice que todo está limpio, no hace nada (o podría apagarse).
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'no_hacer_nada' # Acción para detenerse
            
        # D. Si no hay suciedad conocida pero aún no ha visitado (o por defecto), se mueve.
        elif ubicacion == 'A':
            return 'ir_a_B'
            
        elif ubicacion == 'B':
            return 'ir_a_A'


# =======================================================================
# Código de Simulación
# =======================================================================

# - Simulación 1: Agente Reactivo Simple -
print("- Probando Agente Reactivo Simple -")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

# - Simulación 2: Agente Basado en Modelos -
print("- Probando Agente Basado en Modelos -")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)