import random

class EntornoAspiradora:
    def __init__(self):
        # Dos habitaciones: A y B, cada una puede estar limpia o sucia
        self.estado_habitaciones = {
            'A': random.choice(['Limpia', 'Sucia']),
            'B': random.choice(['Limpia', 'Sucia'])
        }
        # El agente comienza en una habitación al azar
        self.ubicacion_agente = random.choice(['A', 'B'])
        self.pasos = 0
        self.rendimiento = 0

    def obtener_percepcion(self):
        """
        Retorna la percepción del agente: (ubicación, estado_de_la_ubicación).
        Estos son los datos de los sensores.
        """
        return (self.ubicacion_agente, self.estado_habitaciones[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        """
        Ejecuta una acción del agente ("actuadores") y actualiza el entorno y el rendimiento.
        """
        self.pasos += 1
        if accion == 'aspirar':
            if self.estado_habitaciones[self.ubicacion_agente] == 'Sucia':
                self.estado_habitaciones[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10  # Gana puntos por limpiar
            else:
                self.rendimiento -= 1  # Pierde puntos por aspirar en limpio
        elif accion == 'ir_a_B':
            if self.ubicacion_agente == 'A':
                self.ubicacion_agente = 'B'
                self.rendimiento -= 1  # Pierde un punto por moverse
        elif accion == 'ir_a_A':
            if self.ubicacion_agente == 'B':
                self.ubicacion_agente = 'A'
                self.rendimiento -= 1  # Pierde un punto por moverse

    def esta_limpio(self):
        """Verifica si todo el entorno está limpio."""
        return all(estado == 'Limpia' for estado in self.estado_habitaciones.values())

class AgenteReactivoSimple:
    def __init__(self):
        pass

    def decidir(self, percepcion):
        """
        Toma una decisión basándose únicamente en la percepción actual.
        percepción = (ubicación, estado)
        """
        ubicacion, estado = percepcion
        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'

class AgenteBasadoEnModelos:
    def __init__(self):
        # Mantiene un modelo interno del entorno
        self.modelo = {'A': None, 'B': None}

    def decidir(self, percepcion):
        """
        Usa memoria interna para tomar decisiones más informadas.
        """
        ubicacion, estado = percepcion
        self.modelo[ubicacion] = estado

        if estado == 'Sucia':
            return 'aspirar'
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'nada'  # Todo limpio
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'

def simular(agente, entorno):
    print(f"Estado inicial: {entorno.estado_habitaciones}")
    while not entorno.esta_limpio() and entorno.pasos < 10:
        percepcion = entorno.obtener_percepcion()
        accion = agente.decidir(percepcion)
        entorno.ejecutar_accion(accion)
        print(f"Percepción: {percepcion} | Acción: {accion} | Estado: {entorno.estado_habitaciones}")
    print(f"Rendimiento final: {entorno.rendimiento}\n")

# Ejecutar simulaciones
print("Simulación con Agente Reactivo Simple:")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
simular(agente1, entorno1)

print("Simulación con Agente Basado en Modelos:")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
simular(agente2, entorno2)