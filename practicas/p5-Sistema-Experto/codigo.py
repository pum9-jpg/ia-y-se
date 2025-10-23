reglas = [
    {"nombre": "Regla 1: Problema de batería o motor de arranque",
     "si": ["coche_no_gira_llave"],
     "entonces": "problema_bateria_o_arranque"},
    
    {"nombre": "Regla 2: Problema de combustible o encendido",
     "si": ["coche_gira_pero_no_enciende"],
     "entonces": "problema_combustible_o_encendido"},
    
    {"nombre": "Regla 3: Batería descargada confirmada",
     "si": ["problema_bateria_o_arranque", "luces_debiles_o_muertas"],
     "entonces": "diagnostico_bateria_descargada"},
    
    {"nombre": "Regla 4: Motor de arranque defectuoso",
     "si": ["problema_bateria_o_arranque", "luces_funcionan_bien"],
     "entonces": "diagnostico_motor_arranque_defectuoso"},
    
    {"nombre": "Regla 5: Problema de combustible",
     "si": ["problema_combustible_o_encendido", "huele_a_gasolina"],
     "entonces": "diagnostico_sistema_combustible"},
    
    {"nombre": "Regla 6: Problema de encendido",
     "si": ["problema_combustible_o_encendido", "no_huele_a_gasolina"],
     "entonces": "diagnostico_sistema_encendido"}
]

# Paso 2: Construir el Motor de Inferencia
class SistemaExperto:
    def __init__(self, reglas):
        self.reglas = reglas
        self.hechos = set()
        self.historial_inferencia = {}

    def razonar(self, hechos_iniciales):
        self.hechos = set(hechos_iniciales)
        nuevos = True
        while nuevos:
            nuevos = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: '{regla['nombre']}')")
                    nuevos = True
        return self.hechos

# Paso 3: Ejecutar el Sistema y Obtener un Diagnóstico
hechos_iniciales = {"coche_no_gira_llave", "luces_debiles_o_muertas"}
sistema = SistemaExperto(reglas)
print("\n- INICIANDO DIAGNÓSTICO CASO 1 -\n")
resultado = sistema.razonar(hechos_iniciales)
print("\nHechos Finales Deducidos:", resultado)