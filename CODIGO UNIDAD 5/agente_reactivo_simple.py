# agente_reactivo_simple.py
import random

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
        elif accion == 'ir_a_B':
            if self.ubicacion_agente == 'A':
                self.ubicacion_agente = 'B'
                self.rendimiento -= 1
        elif accion == 'ir_a_A':
            if self.ubicacion_agente == 'B':
                self.ubicacion_agente = 'A'
                self.rendimiento -= 1

    def esta_limpio(self):
        return all(estado == 'Limpia' for estado in self.estado_habitaciones.values())


class AgenteReactivoSimple:
    def decidir_accion(self, percepcion):
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'


# Simulación
entorno = EntornoAspiradora()
agente = AgenteReactivoSimple()

print("=== Simulación del Agente Reactivo Simple ===")
for _ in range(10):
    percepcion = entorno.obtener_percepcion()
    accion = agente.decidir_accion(percepcion)
    entorno.ejecutar_accion(accion)
    print(f"Paso {_+1}: {percepcion} -> {accion} | Estado: {entorno.estado_habitaciones}")

print(f"Rendimiento final: {entorno.rendimiento}")
