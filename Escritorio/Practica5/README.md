# Sistema Experto de Diagnóstico de Autos (Encadenamiento Hacia Adelante) 🚗🧠

Este script de Python simula un **Sistema Experto** para diagnosticar por qué un coche no arranca. Lo especial de este sistema es que usa **Encadenamiento Hacia Adelante** (*Forward Chaining*): empieza con los síntomas que pones y usa reglas para generar hechos intermedios hasta llegar a un diagnóstico final.

## 💡 Conceptos Clave

1.  **BASE DE CONOCIMIENTO (`base_de_conocimiento_coche`)**: Es una lista de reglas. Cada regla tiene:
    * **`nombre`**: Una descripción legible.
    * **`si`**: Las condiciones (síntomas o hechos intermedios) que deben ser ciertas.
    * **`entonces`**: El nuevo hecho o diagnóstico que se concluye si se cumplen las condiciones.
2.  **HECHOS**: Los hechos iniciales (síntomas del usuario) y los hechos intermedios que se descubren durante el proceso.
3.  **Encadenamiento Hacia Adelante**: El motor de inferencia sigue aplicando reglas mientras pueda descubrir nuevos hechos, yendo de los **síntomas** a los **diagnósticos**.

---

## 🚀 ¿Cómo funciona el Motor de Inferencia (Implícito)?

Aunque no tienes la función del motor de inferencia aquí, la lógica que aplicaría sería:

1.  **Inicio**: Se tienen los **Hechos Iniciales** (los síntomas que tú reportas).
2.  **Iteración**: Se revisa la lista de reglas una y otra vez.
3.  **Activación**: Cada vez que se encuentra una regla cuyas condiciones (`"si"`) ya están en la lista de Hechos, se "dispara" la regla y su conclusión (`"entonces"`) se **añade** a la lista de Hechos.
4.  **Conclusión**: El proceso se repite hasta que no se puede añadir ningún nuevo hecho. El último hecho añadido es el **diagnóstico final**.

**Ejemplo de Cadena:**
`coche_no_gira_llave` **=> (Regla 1)** `problema_bateria_o_arranque`
Luego, con el nuevo hecho y el síntoma:
`problema_bateria_o_arranque` **+** `luces_debiles_o_muertas` **=> (Regla 3)** `diagnostico_bateria_descargada`

---

## ⚙️ Requisitos

Necesitas tener **Python** instalado en tu computadora (versión 3.x recomendada).

---

## 🏃‍♂️ Ejecución Rápida

Para probar este sistema, necesitarías implementar la función del motor de inferencia. A continuación, se muestra cómo se vería el código completo con un motor simple y cómo ejecutarlo.

### Ejecucion

Abre tu terminal, navega a la carpeta del archivo diagnostico_coche.py y ejecuta:
python diagnostico_coche.py

###  Código Completo

Copia la base de conocimiento y añade la siguiente función y el bloque de ejecución al final del archivo, llamándolo `diagnostico_coche.py`:

```python
def motor_de_inferencia_forward(hechos_iniciales, reglas):
    hechos = set(hechos_iniciales)
    hecho_nuevo_descubierto = True
    
    print(f"Hechos Iniciales: {hechos}")

    # Itera hasta que no se pueda deducir ningún hecho nuevo
    while hecho_nuevo_descubierto:
        hecho_nuevo_descubierto = False
        
        for regla in reglas:
            condiciones = set(regla["si"])
            
            # Comprueba si TODAS las condiciones SI de la regla ya están en los hechos
            if condiciones.issubset(hechos):
                conclusion = regla["entonces"]
                
                # Si la conclusión NO está ya en los hechos, la añadimos
                if conclusion not in hechos:
                    hechos.add(conclusion)
                    hecho_nuevo_descubierto = True
                    print(f"-> Regla '{regla['nombre']}' activada. Nuevo hecho: {conclusion}")
    
    # El diagnóstico final es el último hecho (o el más específico)
    diagnostico_final = [h for h in hechos if h.startswith("diagnostico_")]
    
    if diagnostico_final:
        return f"\nDiagnóstico Final: {diagnostico_final[0]}"
    else:
        return "\nNo se pudo llegar a un diagnóstico específico."

# --- EJEMPLO DE USO ---
sintomas_usuario = ["coche_no_gira_llave", "luces_debiles_o_muertas"]

resultado = motor_de_inferencia_forward(sintomas_usuario, base_de_conocimiento_coche)
print(resultado)
