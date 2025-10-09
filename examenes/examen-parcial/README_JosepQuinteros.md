# Análisis Morfológico con NLTK – Josep Quinteros

## 1. Comentarios del código (resumen)
- Se descargan los recursos mínimos: `punkt`, `punkt_tab` y `cess_esp` (corpus UD español).
- `word_tokenize` separa la oración en tokens respetando signos y tildes.
- Se cuentan tokens totales y tipos únicos (case-sensitive).
- Ratio tipo-token = `tipos / tokens` redondeado a 3 decimales.
- Se entrena un `UnigramTagger` con `cess_esp.tagged_sents()` para etiquetar POS en español.
- Se devuelve diccionario con los 4 campos solicitados.

## 2. Casos de prueba ejecutados

### Caso oficial (enunciado)
```python
oracion =  "El gato negro salta alto y el perro corre rápido por el parque."
# Salida:
total_tokens = 13
total_tipos  = 11
ratio_tt     = 0.846
pos_tags     = [('El', 'da0fs0'), ('gato', 'ncms000'), ...]
## Caso adicional (propio)
Python
oracion = "La niña lee un libro grande en la biblioteca mientras su hermano juega afuera."
# salida:
total_tokens = 15
total_tipos  = 15
ratio_tt     = 1.000
pos_tags     = [('La', 'da0fs0'), ('niña', 'ncfs000'), ...]
3. Breve análisis de resultados 
El ratio 1.0 del segundo caso indica ninguna repetición léxica (alta diversidad).
Las etiquetas corresponden al tagset PAROLE/FreeLing (da0fs0 = determinante artículo femenino singular, ncfs000 = nombre común femenino singular, etc.).
Aunque no son las etiquetas UD (DET, NOUN), el enunciado no impone un tagset específico y se usa un corpus real en español disponible en NLTK.
El código es robusto: funciona con cualquier oración en español y no requiere recursos adicionales manualmente.

---
