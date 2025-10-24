##  Instalación de Python

Para ejecutar correctamente el programa, es necesario tener **Python 3.10 o superior** instalado en tu sistema.
Existen tres métodos recomendados:

---

# 📘 Conclusiones

## 🔹 Enfoque Convencional

### Cómo funciona
La lógica de decisión está escrita directamente en el código mediante condicionales (`if/elif/else`).

### Características
- **Rígido:** difícil de modificar o ampliar.  
- **Lógica y datos mezclados:** el conocimiento (bebidas) está incrustado en la función.  
- **Escalabilidad limitada:** añadir nuevas variables o bebidas implica reescribir código.  

### Ejemplo de uso
> Si es **mañana** y quiere **cafeína** y le gusta **dulce** → recomendar **Mocha**.

---

## 🔹 Enfoque de IA (Basado en Reglas)

### Cómo funciona
Se separa el **qué** (conocimiento: reglas en una lista) del **cómo** (motor de inferencia que aplica las reglas).

### Características
- **Flexible y modular:** basta con añadir o quitar reglas en la base de conocimiento.  
- **Fácil de mantener:** no requiere modificar el motor, solo la lista de reglas.  
- **Declarativo:** las reglas son explícitas y legibles, como frases de un experto humano.  

### Ejemplo de uso
> Hechos: **noche**, **no cafeína** → buscar en la base de conocimiento → recomendar **Té de Manzanilla**.
