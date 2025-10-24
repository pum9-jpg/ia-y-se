# Reutilizamos la estructura de nuestro SistemaExperto de la Unidad 3
class SistemaExpertoDeductivo:
    """
    Un Sistema Experto Deductivo simple que aplica un conjunto de reglas 
    a hechos iniciales para deducir nuevos hechos.
    """
    def __init__(self, reglas):
        """
        Inicializa el sistema experto con un conjunto de reglas.
        :param reglas: Una lista de diccionarios, donde cada diccionario 
                       tiene la forma {"si": [condiciones], "entonces": conclusion}
        """
        self.reglas = reglas

    def razonar(self, hechos):
        """
        Realiza el razonamiento hacia adelante (forward chaining).
        Aplica repetidamente las reglas hasta que no se puedan deducir 
        más hechos nuevos.
        :param hechos: Un conjunto (set) de hechos iniciales.
        :return: Un conjunto (set) de todos los hechos deducidos.
        """
        # Inicializa los hechos deducidos con los hechos iniciales
        hechos_deducidos = set(hechos)
        # Bandera para controlar el bucle de razonamiento
        nuevos_hechos_encontrados = True

        while nuevos_hechos_encontrados:
            nuevos_hechos_encontrados = False
            
            # Itera sobre cada regla en la base de conocimiento
            for regla in self.reglas:
                # Las condiciones ("si") son las premisas
                condiciones = set(regla["si"])
                # La conclusión ("entonces") es el hecho a deducir
                conclusion = regla["entonces"]
                
                # Comprueba si TODAS las condiciones de la regla ya están
                # en los hechos deducidos (subset) Y si la conclusión 
                # aún no ha sido deducida.
                if condiciones.issubset(hechos_deducidos) and \
                   conclusion not in hechos_deducidos:
                    
                    # Si la regla se dispara, añade la conclusión a los hechos
                    hechos_deducidos.add(conclusion)
                    # Señala que se ha encontrado al menos un nuevo hecho
                    nuevos_hechos_encontrados = True
                    
        return hechos_deducidos

# ----------------------------------------------------------------------
# Base de Conocimiento (Reglas Generales)
# ----------------------------------------------------------------------
reglas_animales = [
    {"si": ["tiene_plumas"], "entonces": "es_ave"},
    {"si": ["es_ave", "canta"], "entonces": "es_canario"},
    {"si": ["pone_huevos", "vive_en_agua"], "entonces": "es_pez"}, # Regla con error de ejemplo
    {"si": ["es_ave", "vuela_bien"], "entonces": "es_pajaro"} # Nueva regla
]

# ----------------------------------------------------------------------
# Caso de Uso
# ----------------------------------------------------------------------
# Hechos Específicos de un animal misterioso
hechos_especificos = {"tiene_plumas", "canta"}

# Creamos el sistema y razonamos
sistema_deductivo = SistemaExpertoDeductivo(reglas_animales)
conclusion_final = sistema_deductivo.razonar(hechos_especificos)

# ----------------------------------------------------------------------
# Salida de Resultados
# ----------------------------------------------------------------------
print("-" * 30)
print("Sistema de Razonamiento Deductivo")
print("-" * 30)
print(f"Hechos iniciales: {hechos_especificos}")
print(f"Hechos Deducidos: {conclusion_final}")

# Formateo de la conclusión principal para la impresión final
animal_identificado = [c for c in conclusion_final if c.startswith('es_')]
if animal_identificado:
    print(f"Conclusión final: El animal es un '{animal_identificado[0]}'")
else:
    print("Conclusión final: No se pudo identificar el animal basándose en las reglas.")