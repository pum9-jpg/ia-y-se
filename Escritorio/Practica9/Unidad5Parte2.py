class AgenteReactivoSimple:
    """
    Un agente cuya acción solo depende de la percepción actual.
    """
    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'