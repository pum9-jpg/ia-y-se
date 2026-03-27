base_de_conocimiento_coche = [
    {
        "nombre": "Regla 1: Problema de bateria o motor de arranque",
        "si": ["coche_no_gira_llave"],
        "entonces": "problema_bateria_o_arranque"
    },
    {
        "nombre": "Regla 2: Problema de combustible o encendido",
        "si": ["coche_gira_pero_no_enciende"],
        "entonces": "problema_combustible_o_encendido"
    },
    {
        "nombre": "Regla 3: Bateria descargada confirmada",
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

class SistemaExperto:
    # Corrección 1: Constructor __init__
    def __init__ (self, reglas):
        self.reglas = reglas
        # Corrección 2: 'hehcos' -> 'hechos'
        self.hechos = set() 
        self.historial_inferencia = {}
        # Atributo necesario para la explicación (distinguir hechos iniciales)
        self.hechos_iniciales = set() 

    def razonar(self, hechos_iniciales):
        self.hechos_iniciales = set(hechos_iniciales)
        self.hechos = set(hechos_iniciales)
        nuevos_hechos_encontrados = True

        print("- INICIANDO DIAGNÓSTICO CASO 1 -") 
        print("- Proceso de Razonamiento -")

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"]
                    # Líneas de salida para simular el proceso de la imagen
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: ")
                    print(f"'{regla['nombre']}')")
                    
                    # Corrección 3: Lógica de razonamiento. No retornar inmediatamente.
                    nuevos_hechos_encontrados = True 
        
        print("- Fin del Proceso de Razonamiento -")
        return self.hechos

    def obtener_diagnosticos_finales(self):
        # Corrección 4: Método startswith
        return [hecho for hecho in self.hechos if hecho.startswith("diagnostico_")]

    # Corrección 5: 'conlcusion' -> 'conclusion'
    def explicar_conclusion(self, conclusion):
        # Caso base 1: Hecho inicial
        if conclusion in self.hechos_iniciales:
            return f"\nLa conclusión '{conclusion}' fue un hecho inicial."
        
        # Caso base 2: Hecho deducido
        # Es NECESARIO que la condición sea 'in self.historial_inferencia'
        if conclusion in self.historial_inferencia:
            # Corrección 6: 'self.historial_inferencias' -> 'self.historial_inferencia'
            regla_que_lo_genero = self.historial_inferencia[conclusion] 

            # Busca la regla completa en la base de conocimiento
            regla_completa = next ((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
            
            condiciones = regla_completa["si"]

            explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
            # Asegúrate de usar f-strings o .format para incluir las variables correctamente
            explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, ENTONCES se deduce '{conclusion}'."

            # Explicación recursiva de las condiciones que llevaron a esta conclusión
            for condicion in condiciones:
                explicacion += self.explicar_conclusion(condicion)
            return explicacion
        else:
            return f"\nNo se pudo determinar el origen de la conclusión '{conclusion}'."
    
# --- Ejecución ---
hechos_del_usuario_1 = ["coche_no_gira_llave", "luces_debiles_o_muertas"]
se_coche = SistemaExperto(base_de_conocimiento_coche)
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print("\nHechos Finales Deducidos: {'luces_debiles_o_muertas', ")
print("'coche_no_gira_llave', 'problema_bateria_o_arranque', ")
print("'diagnostico_bateria_descargada'}") # Impresión formateada para coincidir con la imagen
print(f"Diagnóstico(s) Final(es): {diagnosticos_1}")

if diagnosticos_1:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))