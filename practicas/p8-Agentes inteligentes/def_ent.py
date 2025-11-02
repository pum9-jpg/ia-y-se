import random

class EntornoAspiradora:
    def __init__(self):
        self.habitaciones = {
            "A": random.choice(["Limpio", "Sucio"]),
            "B": random.choice(["Limpio", "Sucio"]),
        }
        self.ubicacion_agente = random.choice(["A", "B"])
        self.pasos = 0

    def obtener_percepcion(self):
        estado = self.habitaciones[self.ubicacion_agente]
        return (self.ubicacion_agente, estado)

    def ejecutar_accion(self, accion):
        if accion == "Limpiar":
            self.habitaciones[self.ubicacion_agente] = "Limpio"
        elif accion == "Izquierda":
            self.ubicacion_agente = "A"
        elif accion == "Derecha":
            self.ubicacion_agente = "B"
        self.pasos += 1

    def esta_limpio(self):
        return all(e == "Limpio" for e in self.habitaciones.values())

