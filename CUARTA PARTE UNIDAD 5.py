import random

# =========================================================
# Clase del entorno de la aspiradora
# =========================================================
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
        elif accion == 'no_hacer_nada':
            self.rendimiento += 0

    def esta_limpio(self):
        return all(estado == 'Limpia' for estado in self.estado_habitaciones.values())

    def simular(self, agente, max_pasos=10):
        print(f"\n--- Simulación: {agente.__class__.__name__} ---")
        print(f"Estado inicial: {self.estado_habitaciones}, agente en {self.ubicacion_agente}\n")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion = self.obtener_percepcion()
            accion = agente.actuar(percepcion)
            print(f"Paso {self.pasos+1}: Percepción={percepcion} → Acción={accion}")
            self.ejecutar_accion(accion)
        print(f"\nSimulación terminada en {self.pasos} pasos.")
        print(f"Estado final: {self.estado_habitaciones}")
        print(f"Rendimiento final: {self.rendimiento}\n")


# =========================================================
# Agente Reactivo Simple
# =========================================================
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


# =========================================================
# Agente Basado en Modelos
# =========================================================
class AgenteBasadoEnModelos:
    """
    Un agente que mantiene un estado interno (modelo) del mundo.
    """
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


# =========================================================
# Paso 4: Ejecutar y comparar simulaciones
# =========================================================
if __name__ == "__main__":
    # Simulación 1: Agente Reactivo Simple
    print("\n--- Probando Agente Reactivo Simple ---")
    entorno1 = EntornoAspiradora()
    agente1 = AgenteReactivoSimple()
    entorno1.simular(agente1)

    # Simulación 2: Agente Basado en Modelos
    print("\n--- Probando Agente Basado en Modelos ---")
    entorno2 = EntornoAspiradora()
    agente2 = AgenteBasadoEnModelos()
    entorno2.simular(agente2)
