from base_conocimiento import base_de_conocimiento_coche
from sistema_experto import SistemaExperto

# - Caso de Uso 1 -
print("- INICIANDO DIAGNÓSTICO CASO 1 - ")
# Hechos iniciales: El coche no gira la llave y las luces están muertas.
hechos_del_usuario_1 = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

# Creamos una instancia de nuestro sistema experto con el conocimiento del mecánico
se_coche = SistemaExperto(base_de_conocimiento_coche)

# El motor de inferencia procesa los hechos
hechos_finales_1 = se_coche.razonar(hechos_del_usuario_1)
diagnosticos_1 = se_coche.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_1}")
print(f"Diagnóstico(s) Final(es): {diagnosticos_1}")

# Pedimos una explicación para el diagnóstico final
if diagnosticos_1:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO - ")
    print(se_coche.explicar_conclusion(diagnosticos_1[0]))

# - Caso de Uso 2 (opcional) -
print("\n" + "="*50)
print("- INICIANDO DIAGNÓSTICO CASO 2 - ")
hechos_del_usuario_2 = ["coche_gira_pero_no_enciende", "huele_a_gasolina"]
se_coche_2 = SistemaExperto(base_de_conocimiento_coche)
hechos_finales_2 = se_coche_2.razonar(hechos_del_usuario_2)
diagnosticos_2 = se_coche_2.obtener_diagnosticos_finales()

print(f"\nHechos Finales Deducidos: {hechos_finales_2}")
print(f"Diagnóstico(s) Final(es): {diagnosticos_2}")

if diagnosticos_2:
    print("\n- EXPLICACIÓN DEL DIAGNÓSTICO - ")
    print(se_coche_2.explicar_conclusion(diagnosticos_2[0]))