from def_ent import EntornoAspiradora  # <-- IMPORTA EL ENTORNO

class AgenteBasadoEnModelos:
    """Mantiene un modelo interno del entorno (estado de A y B)."""

    def __init__(self):
        self.modelo = {"A": "Desconocido", "B": "Desconocido"}

    def seleccionar_accion(self, percepcion):
        ubicacion, estado = percepcion
        self.modelo[ubicacion] = estado

        if estado == "Sucio":
            return "Limpiar"
        elif ubicacion == "A":
            return "Derecha" if self.modelo["B"] != "Limpio" else "No hacer nada"
        elif ubicacion == "B":
            return "Izquierda" if self.modelo["A"] != "Limpio" else "No hacer nada"

if __name__ == "__main__":
    print("\n--- Probando Agente Basado en Modelos ---")
    entorno2 = EntornoAspiradora()
    agente2 = AgenteBasadoEnModelos()

    while not entorno2.esta_limpio() and entorno2.pasos < 10:
        percepcion = entorno2.obtener_percepcion()
        accion = agente2.seleccionar_accion(percepcion)
        entorno2.ejecutar_accion(accion)
        print(f"Percepción: {percepcion}, Acción: {accion}")

    print(f"Estado final: {entorno2.habitaciones}, Pasos: {entorno2.pasos}")
