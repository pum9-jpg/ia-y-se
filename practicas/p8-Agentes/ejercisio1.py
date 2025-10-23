import random

# Estado inicial del entorno
ambiente = ["sucio", "limpio"]
posicion = random.choice(["A", "B"])
estado = {"A": random.choice(ambiente), "B": random.choice(ambiente)}

def agente_reactivo(posicion, estado):
    print(f"El agente está en la posición {posicion} y el estado es {estado[posicion]}")
    if estado[posicion] == "sucio":
        print("Acción: limpiar")
        estado[posicion] = "limpio"
    else:
        nueva_posicion = "B" if posicion == "A" else "A"
        print(f"Acción: moverse a {nueva_posicion}")
        posicion = nueva_posicion
    return posicion, estado

# Bucle de simulación
for _ in range(4):
    posicion, estado = agente_reactivo(posicion, estado)
    print("Estado actual:", estado, "\n")