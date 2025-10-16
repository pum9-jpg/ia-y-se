# Paso 1: Definir la Base de Conocimiento
# Contiene el conocimiento de un mecánico experto.
# Cada regla tiene condiciones, una conclusión y un nombre para identificarla.

base_de_conocimiento_coche = [
    {
        "nombre": "Regla 1: Problema de batería o motor de arranque",
        "si": ["coche_no_gira_llave"],
        "entonces": "problema_bateria_o_arranque"
    },
    {
        "nombre": "Regla 2: Problema de combustible o encendido",
        "si": ["coche_gira_pero_no_enciende"],
        "entonces": "problema_combustible_o_encendido"
    },
    {
        "nombre": "Regla 3: Batería descargada confirmada",
        "si": ["problema_bateria_o_arranque", "luces_debiles_o_muertas"],
        "entonces": "diagnostico_bateria_descargada"
    },
    {
        "nombre": "Regla 4: Posible problema del motor de arranque",
        "si": ["problema_bateria_o_arranque", "luces_funcionan_bien"],
        "entonces": "diagnostico_motor_arranque_defectuoso"
    },
    {
        "nombre": "Regla 5: Posible problema de combustible",
        "si": ["problema_combustible_o_encendido", "huele_a_gasolina"],
        "entonces": "diagnostico_sistema_combustible"
    },
    {
        "nombre": "Regla 6: Posible problema de encendido",
        "si": ["problema_combustible_o_encendido", "no_huele_a_gasolina"],
        "entonces": "diagnostico_sistema_encendido"
    }
]

# Paso 2: Construir el Motor de Inferencia y la Estructura del Sistema
class SistemaExperto:
    def __init__(self, reglas):
        # 1. Separación: El conocimiento se pasa al sistema, no está dentro de él.
        self.reglas = reglas
        self.hechos = set()
        # Para la explicación, guardamos qué regla generó cada hecho.
        self.historial_inferencia = {}
    
    def razonar(self, hechos_iniciales):
        """
        Este es el MOTOR DE INFERENCIA.
        Utiliza un algoritmo de encadenamiento hacia adelante.
        """
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True
        print("- Proceso de Razonamiento -")
        
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                
                # Si las condiciones de la regla están en nuestros hechos y la conclusión no lo está.
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]  # Guardamos para la explicación
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: '{regla['nombre']}')")
                    nuevos_hechos_encontrados = True
        
        print("- Fin del Proceso de Razonamiento -")
        return self.hechos
    
    def obtener_diagnosticos_finales(self):
        """Filtra los hechos para mostrar solo los diagnósticos finales."""
        return [hecho for hecho in self.hechos if hecho.startswith('diagnostico_')]
    
    def explicar_conclusion(self, conclusion):
        """
        2. Característica Distintiva: Capacidad de explicación.
        Muestra cómo se llegó a una conclusión específica.
        """
        if conclusion not in self.historial_inferencia:
            if conclusion in self.hechos:
                return f"La conclusión '{conclusion}' fue un hecho inicial."
            else:
                return f"No se pudo determinar cómo se llegó a la conclusión '{conclusion}'."
        
        regla_que_lo_genero = self.historial_inferencia[conclusion]
        
        # Busca la regla completa para mostrar sus condiciones
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
        condiciones = regla_completa["si"]
        
        explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
        explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, ENTONCES se deduce '{conclusion}'.\n\n"
        explicacion += "Trazabilidad completa:\n"
        
        # Reconstruye toda la cadena de razonamiento
        for condicion in condiciones:
            if condicion in self.historial_inferencia:
                explicacion += f"- {condicion}: obtenido por {self.historial_inferencia[condicion]}\n"
            else:
                explicacion += f"- {condicion}: hecho inicial proporcionado por el usuario\n"
        
        return explicacion

# Paso 3: Ejecutar el Sistema y Obtener un Diagnóstico
# - Caso de Uso 1 -
print("- INICIANDO DIAGNÓSTICO CASO 1 -")
# Hechos iniciales: El coche no gira la llave y las luces están muertas.
hechos_del_usuario_1 = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

# Creamos una instancia de nuestro sistema experto con el conocimiento del mecánico
se_coche = SistemaExperto(base_de_conocimiento_coche)

# El motor de inferencia procesa los hechos
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_1}")
print(f"\nDiagnóstico(s) Final(es): {diagnosticos_1}")

# Pedimos una explicación para el diagnóstico final
if diagnosticos_1:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))

# - Caso de Uso 2 (opcional) -
print("\n" + "="*50)
print("- INICIANDO DIAGNÓSTICO CASO 2 -")
hechos_del_usuario_2 = ["coche_gira_pero_no_enciende", "no_huele_a_gasolina"]
hechos_finales_2 = se_coche.razonar(hechos_del_usuario_2)
diagnosticos_2 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_2}")
print(f"\nDiagnóstico(s) Final(es): {diagnosticos_2}")

if diagnosticos_2:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(se_coche.explicar_conclusion(diagnosticos_2[0]))