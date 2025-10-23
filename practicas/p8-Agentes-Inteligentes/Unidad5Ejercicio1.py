import random

class EntornoAspiradora:
    """Representa el entorno del mundo de la aspiradora."""

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
        """Retorna la percepción del agente: (ubicación, estado_de_la_ubicación)."""
        return (self.ubicacion_agente, self.estado_habitaciones[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        """Ejecuta una acción del agente y actualiza el entorno y el rendimiento."""
        self.pasos += 1

        if accion == 'aspirar':
            if self.estado_habitaciones[self.ubicacion_agente] == 'Sucia':
                self.estado_habitaciones[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10
            else:
                self.rendimiento -= 1

        elif accion == 'ir_a_B' and self.ubicacion_agente == 'A':
            self.ubicacion_agente = 'B'
            self.rendimiento -= 1

        elif accion == 'ir_a_A' and self.ubicacion_agente == 'B':
            self.ubicacion_agente = 'A'
            self.rendimiento -= 1

        elif accion == 'no_hacer_nada':
            self.rendimiento += 0  # sin cambio

    def esta_limpio(self):
        """Verifica si todo el entorno está limpio."""
        return all(status == 'Limpia' for status in self.estado_habitaciones.values())

    def simular(self, agente, max_pasos=10):
        """Ejecuta una simulación completa."""
        print(f"Estado Inicial: {self.estado_habitaciones}, Agente en: {self.ubicacion_agente}\n")

        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion_actual = self.obtener_percepcion()
            accion_elegida = agente.actuar(percepcion_actual)
            print(f"Paso {self.pasos+1}: Percepción: {percepcion_actual}, Acción: {accion_elegida}")
            self.ejecutar_accion(accion_elegida)

        print(f"\nSimulación terminada en {self.pasos} pasos.")
        print(f"Rendimiento Final: {self.rendimiento}")
        print(f"Estado Final: {self.estado_habitaciones}\n")


class AgenteReactivoSimple:
    """Un agente cuya acción solo depende de la percepción actual."""

    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'


class AgenteBasadoEnModelos:
    """Un agente que mantiene un estado interno (modelo) del mundo."""

    def __init__(self):
        self.modelo = {'A': 'Desconocido', 'B': 'Desconocido'}

    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        self.modelo[ubicacion] = estado

        if estado == 'Sucia':
            return 'aspirar'
        elif self.modelo['A'] == 'Sucia':
            return 'ir_a_A'
        elif self.modelo['B'] == 'Sucia':
            return 'ir_a_B'
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'no_hacer_nada'
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'


# ==========================
#  EJECUCIÓN DE SIMULACIONES
# ==========================

print("\n--- Probando Agente Reactivo Simple ---")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

print("\n--- Probando Agente Basado en Modelos ---")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)
