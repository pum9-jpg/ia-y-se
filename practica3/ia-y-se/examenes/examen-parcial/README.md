# Examen: Análisis Morfológico con NLTK

## Información del Examen
**Materia:** Procesamiento de Lenguaje Natural  
**Herramientas:** Python, NLTK, Google Colab  
**Duración estimada:** 45 minutos  
**Dificultad:** Intermedia

## Instrucciones tecnicas
1. Crear una rama 
```
git checkout -b QuelaliGaston/ExamenParcial
```
2. Subir el cuaderno (archivo) con el nombre `ExamenParcial.ipynb` dentro de la carpeta `examen-parcial` en tu rama.

## Instrucciones Generales
1. Implemente la función solicitada en Google Colab
2. Use únicamente las bibliotecas especificadas
3. Comente su código adecuadamente
4. Pruebe con los casos de prueba proporcionados
5. Prepare un breve análisis de los resultados

## Ejercicio practico: Análisis Morfológico

### Enunciado Completo
Implemente una función `analisis_morfologico(oracion)` que reciba una cadena de texto en español y retorne un diccionario con la siguiente información:

- **total_tokens**: número total de tokens en la oración
- **total_tipos**: número de tipos únicos (vocabulario)
- **ratio_tt**: ratio tipo-token (tipos/tokens) redondeado a 3 decimales
- **pos_tags**: lista de tuplas (palabra, etiqueta_POS) para cada token

### Ejemplo de Entrada y Salida

#### Entrada:
```python
oracion_ejemplo = "El gato negro salta alto y el perro corre rápido por el parque."
```

#### Salida esperada:
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

1. Preparacion de entorno
```
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_esp')
```
2. Funciones a utilizar:
- `nltk.word_tokenize()` para tokenización en español
- `nltk.pos_tag()` para etiquetado POS

3. Cálculos requeridos:
- **Tokens:** Conteo de todos los elementos tokenizados
- **Tipos:** Conteo de elementos únicos (case-sensitive)
- **Ratio TT:** total_tipos / total_tokens (redondeado a 3 decimales)

#### Codigo Base para implementar
```
def analisis_morfologico(oracion):
    """
    Realiza análisis morfológico completo de una oración en español.
    
    Args:
        oracion (str): Texto en español a analizar
    
    Returns:
        dict: Diccionario con tokens, tipos, ratio TT y POS tags
    """
    # Implementar aquí la solución
    pass
```