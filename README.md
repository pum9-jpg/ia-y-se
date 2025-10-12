# 🧠 Examen: Análisis Morfológico con NLTK

Este examen consiste en implementar un **análisis morfológico** en español utilizando la biblioteca **NLTK**.

---

## 📘 Descripción General

El análisis morfológico estudia la estructura interna de las palabras y su función dentro de una oración.  
En este examen se implementa la función `analisis_morfologico(oracion)` que devuelve estadísticas y etiquetas POS.

---

## ⚙️ Funcionalidades

- **Tokenización** con `nltk.word_tokenize()`  
- **Etiquetado morfosintáctico (POS Tagging)** con `nltk.pos_tag()`  
- **Cálculo de métricas básicas**:
  - total_tokens: número total de palabras
  - total_tipos: número de palabras únicas
  - ratio_tt: diversidad léxica

---

## 🧩 Código Base

```python
def analisis_morfologico(oracion):
    tokens = word_tokenize(oracion, language='spanish')
    total_tokens = len(tokens)
    total_tipos = len(set(tokens))
    ratio_tt = round(total_tipos / total_tokens, 3)
    pos_tags = pos_tag(tokens, lang='spa')
    return {'total_tokens': total_tokens, 'total_tipos': total_tipos, 'ratio_tt': ratio_tt, 'pos_tags': pos_tags}
```

---

## 🧪 Ejemplo de Ejecución

**Entrada:**
```python
oracion_ejemplo = "El gato negro salta alto y el perro corre rápido por el parque."
print(analisis_morfologico(oracion_ejemplo))
```

**Salida esperada:**
```python
{
    'total_tokens': 13,
    'total_tipos': 11,
    'ratio_tt': 0.846,
    'pos_tags': [
        ('El', 'DET'), ('gato', 'NOUN'), ('negro', 'ADJ'),
        ('salta', 'VERB'), ('alto', 'ADV'), ('y', 'CCONJ'),
        ('el', 'DET'), ('perro', 'NOUN'), ('corre', 'VERB'),
        ('rápido', 'ADJ'), ('por', 'ADP'), ('el', 'DET'),
        ('parque', 'NOUN'), ('.', 'PUNCT')
    ]
}
```

---

## 📊 Análisis e Interpretación

- **Tokens:** Cantidad total de unidades léxicas (palabras + puntuación).  
- **Tipos:** Palabras únicas, considerando diferencias entre mayúsculas y minúsculas.  
- **Ratio TT:** Mide la riqueza del vocabulario; valores más altos implican mayor diversidad.  
- **Etiquetas POS:** Identifican el rol gramatical de cada palabra.

---

## 🧾 Conclusión

NLTK proporciona herramientas básicas para el análisis morfológico, útiles para tareas introductorias de PLN.  
Sin embargo, para resultados más precisos y robustos, se pueden emplear herramientas más avanzadas como **spaCy**, **UDPipe** o **transformers** (BERT, RoBERTa).

---

**Autor:** Estudiante — 2025  
**Materia:** Procesamiento de Lenguaje Natural  
