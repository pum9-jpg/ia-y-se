# 📌 Examen Parcial - Análisis Morfológico con NLTK

## 🎯 Objetivo
Implementar una función en Python llamada `analisis_morfologico(oracion)` que procese una oración en español y retorne un análisis morfológico básico.

---

## 🧠 ¿Qué realiza el programa?

Dada una oración en español, la función devuelve:

| Clave          | Descripción |
|----------------|------------|
| `total_tokens` | Número total de tokens generados (palabras + signos) |
| `total_tipos`  | Cantidad de palabras únicas (vocabulario) |
| `ratio_tt`     | Relación tipos/tokens (diversidad léxica), redondeada a 3 decimales |
| `pos_tags`     | Lista de tuplas con la forma `(palabra, etiqueta_POS)` |

---

## 📦 Dependencias requeridas

Este programa utiliza la librería **NLTK** (Natural Language Toolkit).  
En caso de ejecutarlo en **Google Colab**, asegúrate de haber instalado y descargado los recursos necesarios:

```bash
!pip install -U nltk
```

Luego, en Python:

```python
import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('universal_tagset')
```

---

## 🧩 Descripción del funcionamiento

### 1. **Tokenización**
Se utiliza `nltk.word_tokenize` para dividir la oración en palabras y signos de puntuación.  
El tokenizador está configurado para trabajar con español (`language='spanish'`).

### 2. **Etiquetado morfológico (rule-based)**
Se aplica un conjunto manual de reglas para asignar etiquetas POS simplificadas.  
Ejemplos de reglas:
- `el`, `la`, `los` → `DET` (determinante)
- `y`, `pero` → `CCONJ` (conjunción)
- `de`, `por`, `en` → `ADP` (adposición/preposición)
- Palabras que terminan en `-mente` → `ADV` (adverbio)
- Lista manual de verbos comunes → `VERB`
- Signos como `, . ! ?` → `PUNCT`
- Todo lo demás → `NOUN`

> ⚠ **Nota importante:** Este analizador es **básico y académico**. No reemplaza un etiquetador profesional entrenado como *spaCy*.

---

## 📊 Cálculo estadístico

- Los **tokens totales** incluyen cada aparición.
- Los **tipos únicos** eliminan repeticiones.
- El **ratio tipos/tokens (TTR)** permite estimar la diversidad léxica:

\[
	ext{TTR} = rac{	ext{tipos únicos}}{	ext{tokens totales}}
\]

Ejemplo: Si hay 12 tokens y 8 son únicos → `TTR = 0.666`

---

## ▶️ Ejemplo de uso

```python
oracion_ejemplo = "El gato negro salta alto y el perro corre rápido por el parque."
resultado = analisis_morfologico(oracion_ejemplo)
print(resultado)
```

**Salida esperada (estructura):**

```python
{
  'total_tokens': ...,
  'total_tipos': ...,
  'ratio_tt': ...,
  'pos_tags': [
      ('El', 'DET'),
      ('gato', 'NOUN'),
      ('negro', 'ADJ'),
      ...
  ]
}
```

---

## 🚀 Posibles mejoras futuras

- Integrar lematización (forma base de palabras).
- Sustituir reglas manuales por un modelo entrenado en español (**spaCy**, **Stanza**, etc.)
- Exportar resultados en tabla o CSV.
- Visualizar los tokens y etiquetas en una tabla bonita (pandas + display en Colab).

---

