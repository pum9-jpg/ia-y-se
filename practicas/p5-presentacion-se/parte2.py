class SistemaExperto:
    def __init__(self, reglas):
        self.reglas = reglas
        self.hechos = set()
        self.historial_inferencia = {}

    def razonar(self, hechos_iniciales):
        self.hechos = set(hechos_iniciales)
        print("Este es el MOTOR DE INFERENCIA. Utiliza un conjunto de conocimiento hacia adelante...\n")

        nuevos_hechos_encontrados = True
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    print("Regla encontrada:", regla["nombre"])
                    print("Condiciones:", condiciones)
                    print("Conclusión:", conclusion, "(Gracias a la regla:", regla["nombre"] + ")")
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla
                    nuevos_hechos_encontrados = True

            print("\n***** Fin del ciclo. Vamos a inferir solo los diagnósticos finales. *****\n")
            for hecho in self.hechos:
                if hecho.startswith("diagnostico_"):
                    print(self.explicar_conclusion(hecho))

    def obtener_diagnosticos_finales(self):
        return [hecho for hecho in self.hechos if hecho.startswith("diagnostico_")]

    def explicar_conclusion(self, conclusion):
        if conclusion in self.hechos and conclusion not in self.historial_inferencia:
            return f"La conclusión '{conclusion}' fue un hecho inicial.\n"

        if conclusion not in self.historial_inferencia:
            return f"No se pudo determinar cómo se llegó a la conclusión '{conclusion}'.\n"

        regla_que_lo_genero = self.historial_inferencia[conclusion]
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero["nombre"]), None)

        if not regla_completa:
            return f"No se encontró la regla completa para la conclusión '{conclusion}'.\n"

        condiciones = regla_completa["si"]

        explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la {regla_completa['nombre']}:\n"
        explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, "
        explicacion += f"ENTONCES se deduce '{conclusion}'.\n"

        for condicion in condiciones:
            explicacion += self.explicar_conclusion(condicion)

        return explicacion
