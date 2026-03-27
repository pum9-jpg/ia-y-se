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
    def obntener_percepcion(self):
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
        return all(status =='Limpia' for status in self.estado_habitaciones.values())
    def simular (self, agente, max_pasos=10):
        print(f"Estado Inicial: {self.estado_habitaciones}, Agente en: {self.ubicacion_agente}")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion_actual = self.obntener_percepcion()
            accion_elegida = agente.actuar(percepcion_actual)
            self.ejecutar_accion(accion_elegida)
            print(f"Paso {self.pasos + 1}: Percepción= {percepcion_actual}, Acción= {accion_elegida}")
            print(f"Simulación terminada en {self.pasos} pasos. Rendimiento final: {self.rendimiento}")
            print(f"Estado Final: {self.estado_habitaciones}\n")

class AgenteReactivoSimple:
    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'

class AgenteBasadoEnModelo:
    def __init__(self):
        self.modelo = {
            'A': 'Desconocido',
            'B': 'Desconocido'
        }

    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        self.modelo[ubicacion] = estado
        if estado == 'Sucia':
            return 'aspirar'
        elif self.modelo['A'] =='Sucia':
            return 'ir_a_A'
        elif self.modelo['B'] =='Sucia':
            return 'ir_a_B'
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'no_hacer_nada'
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'

print("-    Probando Agente Reactivo Simple    -")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

print("-    Probando Agente Basado en Modelo    -")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelo()
entorno2.simular(agente2)