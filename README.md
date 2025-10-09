📊 Análisis Morfológico en Español con spaCy y NLTK

Este proyecto muestra cómo realizar un análisis morfológico básico de textos en español utilizando las bibliotecas spaCy y NLTK dentro de Google Colab.

🧰 Tecnologías utilizadas

Python 3

spaCy

NLTK

Google Colab

📌 Objetivo

Tokenizar y analizar morfológicamente un texto en español.

Obtener etiquetas gramaticales (POS Tags).

Calcular métricas simples como:

Total de tokens

Total de tipos únicos

Ratio tipo-token (TTR)

📂 Estructura del proyecto
Analisis_Morfologico_SpaCy.ipynb  ← Notebook principal
README.md                          ← Este archivo

🚀 Cómo usarlo

Clona este repositorio:

git clone https://github.com/tu-usuario/tu-repo.git


Abre el archivo .ipynb en Google Colab.

Ejecuta las celdas en orden:

Instalar dependencias

Cargar modelo de spaCy

Analizar texto

Función general para análisis

Pruebas y resultados

🧪 Ejemplo de salida
{'total_tokens': 14,
 'total_tipos': 13,
 'ratio_tt': 0.929,
 'pos_tags': [
   ('El', 'DET'),
   ('gato', 'NOUN'),
   ('negro', 'ADJ'),
   ('salta', 'NOUN'),
   ('alto', 'ADJ'),
   ('y', 'CCONJ'),
   ('el', 'DET'),
   ('perro', 'PROPN'),
   ('corre', 'VERB'),
   ('rápido', 'ADV'),
   ('por', 'ADP'),
   ('el', 'DET'),
   ('parque', 'NOUN'),
   ('.', 'PUNCT')
 ]}

📝 Análisis breve

El análisis permite observar la estructura gramatical de un texto.
Por ejemplo, se puede identificar fácilmente sustantivos, verbos, adjetivos, etc.
Además, el ratio tipo-token da una idea de la riqueza léxica del texto.
