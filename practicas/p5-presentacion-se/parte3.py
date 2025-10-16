from parte2 import SistemaExperto

print("- INICIANDO DIAGNÓSTICO CASO 1 -")

# Hechos iniciales: El coche no gira la llave y las luces están muertas.
hechos_del_usuario_1 = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

# Ejemplo de base de conocimiento del mecánico
base_de_conocimiento_coche = [
    {"nombre": "regla_1", "si": ["coche_no_gira_llave", "luces_debiles_o_muertas"], "entonces": "bateria_descargada"},
    {"nombre": "regla_2", "si": ["bateria_descargada"], "entonces": "diagnostico_bateria"},
]

# Creamos una instancia del sistema experto con el conocimiento del mecánico
se_coche = SistemaExperto(base_de_conocimiento_coche)

# El motor de inferencia procesa los hechos
se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {se_coche.hechos}")
print(f"Diagnóstico(s) Final(es): {diagnosticos_1}")

# Pedimos una explicación para el diagnóstico final
if diagnosticos_1:
    print("\n---- EXPLICACIÓN DEL DIAGNÓSTICO ----")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))
else:
    print("\nNo se encontró ningún diagnóstico final.")