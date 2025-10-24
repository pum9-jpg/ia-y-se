import random

# =====================================================
# Clase del entorno
# =====================================================
class EntornoAspiradora:
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
        elif accion == 'ir_a_B' and self.ubicacion_agente == 'A':
            self.ubicacion_agente = 'B'
            self.rendimiento -= 1
        elif accion == 'ir_a_A' and self.ubicacion_agente == 'B':
            self.ubicacion_agente = 'A'
            self.rendimiento -= 1

    def esta_limpio(self):
        return all(estado == 'Limpia' for estado in self.estado_habitaciones.values())

    def simular(self, agente, max_pasos=10):
        print(f"\nEstado inicial: {self.estado_habitaciones}, agente en {self.ubicacion_agente}\n")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion = self.obtener_percepcion()
            accion = agente.actuar(percepcion)
            print(f"Paso {self.pasos+1}: Percepción={percepcion} → Acción={accion}")
            self.ejecutar_accion(accion)
        print(f"\nSimulación terminada en {self.pasos} pasos.")
        print(f"Estado final: {self.estado_habitaciones}")
        print(f"Rendimiento final: {self.rendimiento}\n")


# =====================================================
# Clase del Agente Reactivo Simple
# =====================================================
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


# =====================================================
# Ejecución de la simulación
# =====================================================
if __name__ == "__main__":
    entorno = EntornoAspiradora()
    agente = AgenteReactivoSimple()
    entorno.simular(agente)
