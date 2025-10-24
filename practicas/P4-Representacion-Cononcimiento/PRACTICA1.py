# image_34d41a.png
# La base de conocimiento se estructura como una lista de reglas de
# diagnóstico.
# Cada regla asocia un conjunto de síntomas con un problema.
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
    # Se podrían añadir más reglas para otros problemas (frenos,
    # cambios, etc.)
}

# También podemos tener reglas para las soluciones
base_conocimiento_soluciones = {
    "regla_3": {
        "si": ["diagnostico_ponchadura"],
        "entonces": "solucion_parchar_o_cambiar_tubo"
    },
    "regla_4": {
        "si": ["diagnostico_cadena_desgastada"],
        "entonces": "solucion_reemplazar_cadena"
    }
}

# Ejemplo de uso
# Supongamos que un usuario nos da sus sintomas (hechos)
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

print("- Usando Reglas de Producción -")

def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
    # Inicializa la variable de diagnóstico
    diagnostico = None
    
    # 1. Buscar un diagnóstico (Usa las reglas de diagnóstico)
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        
        # Evalúa si TODAS las condiciones (síntomas) de la regla están en los hechos_usuario
        if all(condicion in hechos for condicion in condiciones):
            # image_34d439.png (Continuación)
            diagnostico = contenido["entonces"]
            print(f"Diagnóstico encontrado: {diagnostico}")
            break # Detiene la búsqueda de diagnóstico una vez que se encuentra uno

    # 2. Si se encontró un diagnóstico, buscar una solución (Usa las reglas de solución)
    if diagnostico:
        for nombre_regla, contenido in reglas_solucion.items():
            # Evalúa si la condición de la regla de solución (el diagnóstico)
            # es el diagnóstico encontrado.
            # Nota: Asume que las reglas de solución solo tienen una condición en la lista "si"
            if contenido["si"][0] == diagnostico:
                solucion = contenido["entonces"]
                print(f"Solución encontrada: {solucion}")
                return # Termina la función después de encontrar la solución
    
    # 3. Si no se encontró un diagnóstico o una solución (esto último no es posible
    #    con la estructura actual si el diagnóstico se encuentra), imprime el mensaje.
    if not diagnostico:
        print("No se pudo encontrar un diagnóstico con los sintomas proporcionados.")

# Llamada a la función
diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)

# --------------------------------------------------
## Explicación de las adiciones

La parte clave faltante en el bucle de diagnóstico era la lógica de la condición `if` en la línea 40 (`image_34d41a.png`), la cual debe verificar que **todos** los síntomas requeridos por la regla estén presentes en los hechos del usuario.

Se completó con:

1.  **Línea 40 (nueva):**
    ```python
    if all(condicion in hechos for condicion in condiciones):
    ```
    Esto utiliza el generador de expresiones y la función **`all()`** de Python. `all()` devuelve `True` si todos los elementos del iterable (en este caso, una serie de valores booleanos de la forma `condicion in hechos`) son `True`. Esto asegura que todos los síntomas de la regla de diagnóstico se cumplan con los `hechos_usuario`.

2.  **Continuación del Bucle de Diagnóstico (Líneas 41-43 en `image_34d439.png`):**
    Esta parte se ejecuta solo si la condición `if all(...)` es verdadera, lo que significa que se ha encontrado un diagnóstico coincidente.
    ```python
    diagnostico = contenido["entonces"]
    print(f"Diagnóstico encontrado: {diagnostico}")
    break # Sale del bucle for al encontrar el primer diagnóstico
    ```

3.  **Bucle de Solución (Líneas 47-51 en `image_34d439.png`):**
    La condición para buscar la solución también se completó para verificar si la condición de la regla de solución coincide con el diagnóstico encontrado.
    ```python
    if contenido["si"][0] == diagnostico:
    ```
    Se usa `contenido["si"][0]` asumiendo que las reglas de solución siempre tendrán solo un elemento en su lista "si" (que es el diagnóstico).

Con estas adiciones, el código funciona como un motor de inferencia simple de **encadenamiento hacia adelante** (partiendo de los hechos/síntomas para llegar a una conclusión/diagnóstico).