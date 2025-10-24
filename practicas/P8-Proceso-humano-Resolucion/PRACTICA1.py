import random

class EntornoAspiradora:
    """
    Representa el entorno del mundo de la aspiradora.
    """
    def __init__(self):
        # El estado de las habitaciones puede ser 'Limpia' o 'Sucia'.
        self.estado_habitaciones = {
            'A': random.choice(['Limpia', 'Sucia']),
            'B': random.choice(['Limpia', 'Sucia'])
        }
        # El agente comienza en una habitación al azar.
        self.ubicacion_agente = random.choice(['A', 'B'])
        self.pasos = 0
        self.rendimiento = 0

    def obtener_percepcion(self):
        """
        Retorna la percepción del agente: (ubicación, estado_de_la_ubicación).
        Estos son los datos de los "sensores".
        """
        return (self.ubicacion_agente, self.estado_habitaciones[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        """
        Ejecuta una acción del agente ("actuadores") y actualiza el
        entorno y el rendimiento.
        """
        self.pasos += 1
        if accion == 'aspirar':
            if self.estado_habitaciones[self.ubicacion_agente] == 'Sucia':
                self.estado_habitaciones[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10 # Gana puntos por limpiar
            else:
                self.rendimiento -= 1 # Pierde puntos por aspirar en
                                     # sitio limpio
        elif accion == 'ir_a_B':
            if self.ubicacion_agente == 'A':
                self.ubicacion_agente = 'B'
                self.rendimiento -= 1 # Pierde un punto por moverse
        elif accion == 'ir_a_A':
            if self.ubicacion_agente == 'B':
                self.ubicacion_agente = 'A'
                self.rendimiento -= 1 # Pierde un punto por moverse

    def esta_limpio(self):
        """Verifica si todo el entorno está limpio."""
        return all(status == 'Limpia' for status in self.estado_habitaciones.values())

    def simular(self, agente, max_pasos=10):
        """Ejecuta una simulación completa."""
        print(f"Estado Inicial: {self.estado_habitaciones}, Agente en: {self.ubicacion_agente}")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion_actual = self.obtener_percepcion()
            accion_elegida = agente.actuar(percepcion_actual)
            print(f"Paso {self.pasos+1}: Percepción={percepcion_actual}, Acción={accion_elegida}")
            self.ejecutar_accion(accion_elegida)
        print(f"Simulación terminada en {self.pasos} pasos.")
        print(f"Rendimiento final: {self.rendimiento}")
        print(f"Estado Final: {self.estado_habitaciones}\n")