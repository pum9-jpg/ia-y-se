import random

class EntornoAspiradora:
    """
    Representa el entorno del mundo de la aspiradora.
    """
    def __init__(self):
        self.estado_habitaciones = {
            'A': random.choice(['Limpia', 'Sucia']),
            'B': random.choice(['Limpia', 'Sucia'])
        }
        self.ubicacion_agente = random.choice(['A', 'B'])
        self.pasos = 0
        self.rendimiento = 0

    def obtener_percepcion(self):
        return (self.ubicacion_agente, self.estado_habitaciones[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        self.pasos += 1
        if accion == 'aspirar':
            if self.estado_habitaciones[self.ubicacion_agente] == 'Sucia':
                self.estado_habitaciones[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10
            else:
                self.rendimiento -= 1
        elif accion == 'ir_a_B':
            if self.ubicacion_agente == 'A':
                self.ubicacion_agente = 'B'
                self.rendimiento -= 1
        elif accion == 'ir_a_A':
            if self.ubicacion_agente == 'B':
                self.ubicacion_agente = 'A'
                self.rendimiento -= 1

    def esta_limpio(self):
        return all(status == 'Limpia' for status in self.estado_habitaciones.values())

    def simular(self, agente, max_pasos=20):
        print(f"\n--- Simulación: {agente.__class__.__name__} ---")
        print(f"Estado Inicial: {self.estado_habitaciones}, Agente en: {self.ubicacion_agente}")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion_actual = self.obtener_percepcion()
            accion_elegida = agente.actuar(percepcion_actual)
            print(f"Paso {self.pasos+1}: Percepción={percepcion_actual}, Acción={accion_elegida}")
            self.ejecutar_accion(accion_elegida)
        print(f"Simulación terminada en {self.pasos} pasos. Rendimiento final: {self.rendimiento}")
        print(f"Estado Final: {self.estado_habitaciones}")

class AgenteReactivoSimple:
    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        # si está limpio, moverse a la otra habitación
        return 'ir_a_B' if ubicacion == 'A' else 'ir_a_A'

class AgenteBasadoEnModelo:
    def __init__(self):
        # modelo de creencias sobre el estado de A y B
        self.modelo = {'A': None, 'B': None}

    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        # actualizar modelo
        self.modelo[ubicacion] = estado

        # si la posición actual está sucia, aspirar
        if estado == 'Sucia':
            return 'aspirar'

        # si conoce alguna habitación sucia, ir a ella
        for sala, val in self.modelo.items():
            if val == 'Sucia' and sala != ubicacion:
                return 'ir_a_B' if sala == 'B' else 'ir_a_A'

        # en duda, moverse para explorar
        return 'ir_a_B' if ubicacion == 'A' else 'ir_a_A'

if __name__ == "__main__":
    # Ejecutar dos simulaciones independientes
    env1 = EntornoAspiradora()
    agente1 = AgenteReactivoSimple()
    env1.simular(agente1)

    env2 = EntornoAspiradora()
    agente2 = AgenteBasadoEnModelo()
    env2.simular(agente2)
