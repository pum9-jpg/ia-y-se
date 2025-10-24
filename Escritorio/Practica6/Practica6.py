import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# =========================================================
# I. SISTEMA DE RAZONAMIENTO INDUCTIVO (ÁRBOL DE DECISIÓN)
# =========================================================

# - Datos (Observaciones Específicas) -
# En lugar de reglas, tenemos una lista de ejemplos.
datos_animales = [
    {'nombre': 'paloma', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 1, 'clase': 'pajaro'},
    {'nombre': 'canario', 'tiene_plumas': 1, 'canta': 1, 'vuela_bien': 1, 'clase': 'canario'},
    {'nombre': 'gallina', 'tiene_plumas': 1, 'canta': 0, 'vuela_bien': 0, 'clase': 'ave_no_voladora'},
    {'nombre': 'pez_dorado', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'},
    {'nombre': 'salmon', 'tiene_plumas': 0, 'canta': 0, 'vuela_bien': 0, 'clase': 'pez'}
]

# Convertimos los datos a un formato que scikit-learn entiende
df = pd.DataFrame(datos_animales)
features = ["tiene_plumas", "canta", "vuela_bien"]
X = df[features]  # Las características (los "hechos")
y = df['clase']    # La etiqueta que queremos predecir (la "conclusión")

# - Proceso de Inducción (Aprendizaje) -
modelo_inductivo = DecisionTreeClassifier()
modelo_inductivo.fit(X, y) # El modelo aprende las reglas de los datos.

# - Resultados: Las Reglas "Aprendidas" -
reglas_aprendidas = export_text(modelo_inductivo, feature_names=features)

print("="*60)
print("SISTEMA 1: RAZONAMIENTO INDUCTIVO (ÁRBOL DE DECISIÓN)")
print("Reglas que el sistema INDUJO a partir de los ejemplos:")
print(reglas_aprendidas)

# - Caso de Uso -
animal_nuevo = pd.DataFrame([[1, 1, 1]], columns=features) # tiene_plumas=1, canta=1, vuela_bien=1
prediccion = modelo_inductivo.predict(animal_nuevo)

print(f"\nClasificando un animal nuevo con características [Plumas=Sí, Canta=Sí, Vuela=Sí]. ")
print(f"Conclusión probable: El animal es un '{prediccion[0]}'")

# =========================================================
# II. SISTEMA DE RAZONAMIENTO DEDUCTIVO SIMPLE
# =========================================================

# Reutilizamos la estructura de nuestro SistemaExperto de la Unidad 3
class SistemaExpertoDeductivo:
    def __init__(self, reglas):
        self.reglas = reglas

    def razonar(self, hechos):
        hechos_deducidos = set(hechos)
        nuevos_hechos_encontrados = True

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]
                
                if condiciones.issubset(hechos_deducidos) and \
                   conclusion not in hechos_deducidos:
                    hechos_deducidos.add(conclusion)
                    nuevos_hechos_encontrados = True
        return hechos_deducidos

# - Base de Conocimiento (Reglas Generales) -
reglas_animales = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"},
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"} # Nueva regla
]

# - Caso de Uso -
hechos_especificos = {"tiene_plumas", "canta"}

# Creamos el sistema y razonamos
sistema_deductivo = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema_deductivo.razonar(hechos_especificos)

print("\n" + "="*60)
print("SISTEMA 2: RAZONAMIENTO DEDUCTIVO SIMPLE")
print(f"Hechos iniciales: {hechos_especificos}")
print(f"Hechos deducidos: {conclusion_final}")
print(f"Conclusión final: El animal es un '{next(c for c in conclusion_final if c.startswith('es_'))}'")


# =========================================================
# III. SISTEMA EXPERTO CON CAPACIDAD DE EXPLICACIÓN (COCHE)
# =========================================================

# BASE DE CONOCIMIENTO (Reglas de un mecánico experto)
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
    def __init__(self, reglas):
        # 1. Separación: El conocimiento se pasa al sistema, no está
        # dentro de él.
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

        print("\n- Proceso de Razonamiento -")
        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            for regla in self.reglas:
                condiciones = set(regla["si"])
                conclusion = regla["entonces"]

                # Si las condiciones de la regla están en nuestros
                # hechos y la conclusión no lo está.
                if condiciones.issubset(self.hechos) and conclusion not in self.hechos:
                    self.hechos.add(conclusion)
                    self.historial_inferencia[conclusion] = regla["nombre"] # Guardamos para la explicación
                    print(f"Hecho añadido: '{conclusion}' (Gracias a la regla: '{regla['nombre']}')")
                    nuevos_hechos_encontrados = True
        print("- Fin del Proceso de Razonamiento -")
        return self.hechos

    def obtener_diagnosticos_finales(self):
        """Filtra los hechos para mostrar solo los diagnósticos."""
        return [hecho for hecho in self.hechos if hecho.startswith('diagnostico_')]

    def explicar_conclusion(self, conclusion):
        """
        2. Característica Distintiva: Capacidad de explicación.
        Muestra cómo se llegó a una conclusión específica.
        """
        if conclusion not in self.historial_inferencia:
            if conclusion in self.hechos:
                return f"\nLa conclusión '{conclusion}' fue un hecho inicial."
            else:
                return f"\nNo se pudo determinar cómo se llegó a la conclusión '{conclusion}'."

        regla_que_lo_genero = self.historial_inferencia[conclusion]

        # Busca la regla completa para mostrar sus condiciones
        regla_completa = next((r for r in self.reglas if r["nombre"] == regla_que_lo_genero), None)
        condiciones = regla_completa["si"]

        explicacion = f"\nSe llegó a la conclusión '{conclusion}' por la '{regla_que_lo_genero}'.\n"
        explicacion += f"Esta regla establece que SI se cumplen las siguientes condiciones: {condiciones}, ENTONCES se deduce '{conclusion}'.\n"

        # Recursivamente, explica cómo se obtuvieron las condiciones
        for condicion in condiciones:
            explicacion += self.explicar_conclusion(condicion)

        return explicacion

# - Caso de Uso 1 -
print("\n" + "="*60)
print("SISTEMA 3: DEDUCTIVO CON EXPLICACIÓN (DIAGNÓSTICO COCHE)")
print("- INICIANDO DIAGNÓSTICO CASO 1 -")
# Hechos iniciales: El coche no gira la llave y las luces están muertas.
hechos_del_usuario_1 = {"coche_no_gira_llave", "luces_debiles_o_muertas"}

# Creamos una instancia de nuestro sistema experto con el conocimiento del mecánico
se_coche = SistemaExperto(base_de_conocimiento_coche)
# El motor de inferencia procesa los hechos
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_1}")
print(f"Diagnóstico(s) Final(es): {diagnosticos_1}")

# Pedimos una explicación para el diagnóstico final
if diagnosticos_1:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO -")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))