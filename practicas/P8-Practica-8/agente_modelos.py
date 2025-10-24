# Paso 3: Implementar un Agente Basado en Modelos

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
        if estado == 'Sucia':
            return 'aspirar'
        elif self.modelo['A'] == 'Sucia':
            return 'ir_a_A'
        elif self.modelo['B'] == 'Sucia':
            return 'ir_a_B'
        # Si su modelo dice que todo está limpio, no hace nada (o podría apagarse).
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'no_hacer_nada'  # Acción para detenerse
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'