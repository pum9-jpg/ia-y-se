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
        return all(status == 'Limpia' for status in self.estado_habitaciones.values())
    
    def simular(self, agente, max_pasos=10):
        """Ejecuta una simulación completa."""
        print(f"Estado Inicial: {self.estado_habitaciones}, Agente en: {self.ubicacion_agente}")
        while not self.esta_limpio() and self.pasos < max_pasos:
            percepcion_actual = self.obtener_percepcion()
            accion_elegida = agente.actuar(percepcion_actual)
            print(f"Paso {self.pasos+1}: Percepción={percepcion_actual}, Acción={accion_elegida}")
            self.ejecutar_accion(accion_elegida)
        print(f"Simulación terminada en {self.pasos} pasos. Rendimiento final: {self.rendimiento}")
        print(f"Estado Final: {self.estado_habitaciones} \n")

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

class AgenteBasadoEnModelos:
    """
    Un agente que mantiene un estado interno (modelo) del mundo.
    """
    
    def __init__(self):
        # El modelo interno del agente. Inicialmente no sabe nada.
        self.modelo = {'A': 'Desconocido', 'B': 'Desconocido'}
    
    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        
        # 1. Actualiza su modelo interno con la nueva percepción.
        self.modelo[ubicacion] = estado
        
        # 2. Toma una decisión basada en su modelo actualizado.
        if estado == 'Sucia':
            return 'aspirar'
        elif self.modelo['A'] == 'Sucia':
            return 'ir_a_A'
        elif self.modelo['B'] == 'Sucia':
            return 'ir_a_B'
        # Si su modelo dice que todo está limpio, no hace nada (o podría apagarse).
        elif self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'no_hacer_nada'  # Acción para detenerse
        elif ubicacion == 'A':
            return 'ir_a_B'
        elif ubicacion == 'B':
            return 'ir_a_A'
            
# - Simulación 1: Agente Reactivo Simple -
print("- Probando Agente Reactivo Simple -")
entorno1 = EntornoAspiradora()
agente1 = AgenteReactivoSimple()
entorno1.simular(agente1)

# - Simulación 2: Agente Basado en Modelos -
print("- Probando Agente Basado en Modelos -")
entorno2 = EntornoAspiradora()
agente2 = AgenteBasadoEnModelos()
entorno2.simular(agente2)