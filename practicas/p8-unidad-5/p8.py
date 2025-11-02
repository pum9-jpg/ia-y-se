import random


# ----------------------------------------------------------
# 🌍 Clase del Entorno de la Aspiradora
# ----------------------------------------------------------
class EntornoAspiradora:
    def __init__(self):
        # Cada habitación inicia limpia o sucia al azar
        self.estado_habitaciones = {
            'A': random.choice(['Limpia', 'Sucia']),
            'B': random.choice(['Limpia', 'Sucia'])
        }
        # El agente empieza en A o B
        self.ubicacion_agente = random.choice(['A', 'B'])
        self.pasos = 0
        self.rendimiento = 0

    def obtener_percepcion(self):
        """
        Retorna una tupla con (ubicación actual, estado de la habitación).
        Esto simula los sensores del agente.
        """
        return (self.ubicacion_agente, self.estado_habitaciones[self.ubicacion_agente])

    def ejecutar_accion(self, accion):
        """
        Ejecuta la acción del agente y actualiza el entorno.
        También ajusta el rendimiento según las reglas.
        """
        self.pasos += 1

        if accion == 'aspirar':
            if self.estado_habitaciones[self.ubicacion_agente] == 'Sucia':
                self.estado_habitaciones[self.ubicacion_agente] = 'Limpia'
                self.rendimiento += 10  # Gana puntos por limpiar
                print(f"🧹 Habitación {self.ubicacion_agente} limpiada.")
            else:
                self.rendimiento -= 1  # Penalización por aspirar en limpio
                print(f"⚠️ Aspiró habitación limpia ({self.ubicacion_agente}).")

        elif accion == 'ir_a_B':
            if self.ubicacion_agente == 'A':
                self.ubicacion_agente = 'B'
                self.rendimiento -= 1
                print("➡️ El agente se mueve de A a B.")

        elif accion == 'ir_a_A':
            if self.ubicacion_agente == 'B':
                self.ubicacion_agente = 'A'
                self.rendimiento -= 1
                print("⬅️ El agente se mueve de B a A.")

    def esta_limpio(self):
        """Verifica si todas las habitaciones están limpias."""
        return all(estado == 'Limpia' for estado in self.estado_habitaciones.values())


# ----------------------------------------------------------
# 🤖 Agente Reactivo Simple
# ----------------------------------------------------------
class AgenteReactivoSimple:
    def __init__(self):
        pass

    def actuar(self, percepcion):
        """
        El agente actúa según la percepción actual sin memoria.
        """
        ubicacion, estado = percepcion

        if estado == 'Sucia':
            return 'aspirar'
        elif ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'


# ----------------------------------------------------------
# 🧠 Agente Basado en Modelos
# ----------------------------------------------------------
class AgenteBasadoEnModelos:
    def __init__(self):
        # El modelo interno guarda el estado conocido de cada habitación
        self.modelo = {'A': None, 'B': None}

    def actuar(self, percepcion):
        ubicacion, estado = percepcion
        self.modelo[ubicacion] = estado

        # Si la habitación actual está sucia, limpia
        if estado == 'Sucia':
            return 'aspirar'

        # Si ambas están limpias según el modelo, no hace nada
        if self.modelo['A'] == 'Limpia' and self.modelo['B'] == 'Limpia':
            return 'nada'

        # Si está en A, ve a B
        if ubicacion == 'A':
            return 'ir_a_B'
        else:
            return 'ir_a_A'


# ----------------------------------------------------------
# 🧪 Función para simular el comportamiento de un agente
# ----------------------------------------------------------
def simular(agente, entorno):
    print(f"\n===============================")
    print(f"Simulación con {agente.__class__.__name__}")
    print("===============================")
    print(f"Estado inicial: {entorno.estado_habitaciones}, agente en {entorno.ubicacion_agente}")
    print("-------------------------------")

    pasos_max = 10

    for _ in range(pasos_max):
        percepcion = entorno.obtener_percepcion()
        accion = agente.actuar(percepcion)
        print(f"👀 Percepción: {percepcion} → Acción: {accion}")

        if accion == 'nada':
            print("✅ Todo limpio. El agente se detiene.")
            break

        entorno.ejecutar_accion(accion)

        if entorno.esta_limpio():
            print("✨ Todas las habitaciones están limpias.")
            break

    print("-------------------------------")
    print(f"🏁 Estado final: {entorno.estado_habitaciones}")
    print(f"📊 Rendimiento total: {entorno.rendimiento}\n")


# ----------------------------------------------------------
# 🧩 Ejecución de la Simulación
# ----------------------------------------------------------
if __name__ == "__main__":
    # Simular agente reactivo
    entorno1 = EntornoAspiradora()
    agente1 = AgenteReactivoSimple()
    simular(agente1, entorno1)

    # Simular agente basado en modelos
    entorno2 = EntornoAspiradora()
    agente2 = AgenteBasadoEnModelos()
    simular(agente2, entorno2)
