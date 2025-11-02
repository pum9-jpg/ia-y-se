from def_ent import EntornoAspiradora  # <-- IMPORTA EL ENTORNO

class AgenteReactivoSimple:
    """Un agente cuyas acciones solo dependen de la percepción actual."""

    def seleccionar_accion(self, percepcion):
        ubicacion, estado = percepcion
        if estado == "Sucio":
            return "Limpiar"
        elif ubicacion == "A":
            return "Derecha"
        elif ubicacion == "B":
            return "Izquierda"

if __name__ == "__main__":
    print("\n--- Probando Agente Reactivo Simple ---")
    entorno1 = EntornoAspiradora()
    agente1 = AgenteReactivoSimple()

    while not entorno1.esta_limpio() and entorno1.pasos < 10:
        percepcion = entorno1.obtener_percepcion()
        accion = agente1.seleccionar_accion(percepcion)
        entorno1.ejecutar_accion(accion)
        print(f"Percepción: {percepcion}, Acción: {accion}")

    print(f"Estado final: {entorno1.habitaciones}, Pasos: {entorno1.pasos}")
