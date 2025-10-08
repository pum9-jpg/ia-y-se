# Algoritmo de Planificación Round Robin
def round_robin(procesos, quantum):
    tiempo = 0
    cola = procesos.copy()
    tiempos_espera = {p[0]: 0 for p in procesos}
    tiempos_retorno = {}

    while cola:
        proceso = cola.pop(0)
        nombre, rafaga = proceso

        if rafaga > quantum:
            print(f"{nombre} ejecuta {quantum} unidades de tiempo")
            tiempo += quantum
            cola.append((nombre, rafaga - quantum))
            # Actualizar espera de los demás
            for p in cola:
                if p[0] != nombre:
                    tiempos_espera[p[0]] += quantum
        else:
            print(f"{nombre} ejecuta {rafaga} unidades de tiempo y termina")
            tiempo += rafaga
            tiempos_retorno[nombre] = tiempo
            # Actualizar espera de los demás
            for p in cola:
                tiempos_espera[p[0]] += rafaga

    print("\n Resultados:")
    for nombre in tiempos_retorno:
        print(f"Proceso {nombre}: Retorno = {tiempos_retorno[nombre]}, Espera = {tiempos_espera[nombre]}")

# Lista de procesos: (Nombre, Tiempo de ráfaga)
procesos = [("P1", 10), ("P2", 5), ("P3", 8)]
quantum = 3

round_robin(procesos, quantum)
