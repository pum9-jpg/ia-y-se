# 🧠 Unidad: Enfoques para Recomendar Bebidas en Python  
**Comparación entre Enfoque Convencional y Enfoque Basado en Reglas (IA)**  

---

## 📘 Descripción
Este proyecto demuestra dos formas de implementar la lógica de decisión en Python para recomendar bebidas según las preferencias del usuario:

1. **Enfoque Convencional:**  
   La lógica está escrita directamente en el código mediante estructuras condicionales (`if`, `elif`, `else`).

2. **Enfoque Basado en Reglas (IA):**  
   Se separa el *qué* (conocimiento) del *cómo* (razonamiento).  
   Las reglas se almacenan en una *base de conocimiento* y un *motor de inferencia* las evalúa.

---

## 📂 Archivos del Proyecto
- `convencional.py` → Implementación del enfoque convencional.  
- `basado_reglas.py` → Implementación del enfoque basado en reglas.  
- `README.md` → Este archivo.  
- *(opcional)* `comparativo.py` → Ejecuta ambos enfoques y muestra resultados.

---

## ⚙️ Requisitos
- **Python 3.8 o superior.**
- No requiere librerías externas.

---

## 🖥️ Instalación (opcional)
Puedes crear un entorno virtual para mantener tu entorno limpio:

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows.
```
# CONCLUCIONES
El enfoque convencional es simple y adecuado para pocos casos.
Sin embargo, cuando la lógica de decisión crece, el enfoque basado en reglas es más escalable y flexible, ya que separa la lógica del conocimiento, permitiendo modificar las recomendaciones sin tocar el código principal.
