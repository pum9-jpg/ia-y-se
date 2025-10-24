# Sistema de Diagnóstico - Enfoque Basado en Reglas de Producción

## Descripción
Este sistema utiliza un **enfoque basado en reglas de producción** para diagnosticar problemas mecánicos de una bicicleta.  
La base de conocimiento se divide en dos partes: reglas de **diagnóstico** y reglas de **solución**, que el motor de inferencia aplica para encontrar la causa y el tratamiento del problema.

## Código
```python
# Base de conocimiento: reglas de diagnóstico
base_conocimiento_reglas = {
    "regla_1": {
        "si": ["llanta_blanda"],
        "entonces": "diagnostico_ponchadura"
    },
    "regla_2": {
        "si": ["chasquido_al_pedalear", "cadena_salta"],
        "entonces": "diagnostico_cadena_desgastada"
    }
}

# Base de conocimiento: reglas de soluciones
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

# Hechos proporcionados por el usuario
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]

print("\n--- Usando Reglas de Producción ---\n")

def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
    diagnostico = None

    # Buscar un diagnóstico
    for nombre_regla, contenido in reglas_diagnostico.items():
        condiciones = contenido["si"]
        if all(condicion in hechos for condicion in condiciones):
            diagnostico = contenido["entonces"]
            print(f"Diagnóstico encontrado: {diagnostico}")
            break

    # Si se encontró un diagnóstico, buscar una solución
    if diagnostico:
        for nombre_regla, contenido in reglas_solucion.items():
            if contenido["si"][0] == diagnostico:
                solucion = contenido["entonces"]
                print(f"Solución encontrada: {solucion}")
                return
    else:
        print("No se pudo encontrar un diagnóstico con los síntomas proporcionados.")

# Ejecutar la función
diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)
```

## Ejemplo de uso
El usuario reporta los siguientes síntomas:  
- **chasquido al pedalear**  
- **cadena salta**  

**Resultado esperado:**  
> Diagnóstico encontrado: diagnóstico_cadena_desgastada  
> Solución encontrada: solución_reemplazar_cadena

## Observaciones
Este enfoque es similar a los sistemas expertos clásicos.  
La información está estructurada como **reglas de producción**, lo que permite automatizar decisiones mediante inferencia lógica.

## Conclusión
Es efectivo para **diagnósticos determinísticos** donde los síntomas tienen relaciones claras con las causas, sin embargo, su mantenimiento puede ser complejo si el número de reglas crece, ya que cada nueva situación requiere agregar o modificar reglas manualmente.
