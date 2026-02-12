# 💬 Tema: Tokenizacion

## 🌍 Introduccion
La tokenizacion es el proceso inicial dentro del analisis de lenguaje natural (PLN).  
Consiste en dividir un texto en unidades minimas llamadas **tokens**, que pueden ser palabras, signos o frases cortas.  
Es una fase esencial antes de realizar tareas como el analisis morfologico, el etiquetado o la clasificacion de texto.

---

## 1️⃣ Concepto de token

Un **token** es una unidad elemental de significado.  
Por ejemplo, en la frase:  
`El gato duerme mucho`  
Los tokens son: `["El", "gato", "duerme", "mucho"]`.

La identificacion correcta de tokens es clave para que los algoritmos entiendan la estructura del lenguaje.

---

## 2️⃣ Proceso de tokenizacion

El proceso de tokenizacion normalmente incluye los siguientes pasos:

1. **Limpieza del texto:** eliminar simbolos innecesarios, mayusculas, o puntuacion no relevante.  
2. **Division del texto:** separar las palabras mediante espacios o patrones regulares.  
3. **Normalizacion:** transformar las palabras en minusculas o en una forma uniforme.  
4. **Filtrado:** eliminar tokens vacios o irrelevantes como articulos o preposiciones, dependiendo de la tarea.

---

## 3️⃣ Tipos de tokenizacion

- **Tokenizacion por palabras:** la mas comun, divide segun los espacios.  
- **Tokenizacion por caracteres:** divide el texto en letras individuales, util para modelos de lenguaje o correccion ortografica.  
- **Tokenizacion por subpalabras:** usada en modelos modernos como BERT o GPT, donde las palabras se dividen en fragmentos que conservan sentido parcial.  
- **Tokenizacion por oraciones:** separa el texto segun signos de puntuacion mayores (., ?, !).

---

## 4️⃣ Ejemplo de tokenizacion en Python

```python
import nltk
from nltk.tokenize import word_tokenize

texto = "La inteligencia artificial estudia como las maquinas pueden aprender."
tokens = word_tokenize(texto, language='spanish')
print(tokens)
```
**Salida esperada:**  
`['La', 'inteligencia', 'artificial', 'estudia', 'como', 'las', 'maquinas', 'pueden', 'aprender', '.']`

Este ejemplo muestra como se puede aplicar tokenizacion con la biblioteca NLTK, una herramienta comun en procesamiento del lenguaje natural.

---

## 💡 Conclusion
La tokenizacion es la puerta de entrada al procesamiento de texto.  
Permite estructurar la informacion linguistica en unidades manejables que luego pueden ser analizadas por algoritmos de IA y PLN.
