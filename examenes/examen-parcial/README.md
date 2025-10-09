# 🧠 Análisis Morfológico en Español con NLTK

Este script realiza un **análisis morfológico básico** de una oración en
español utilizando la biblioteca `nltk`.\
Su propósito es identificar categorías gramaticales (como sustantivos,
verbos, adjetivos, etc.) y calcular métricas lingüísticas simples.

------------------------------------------------------------------------

## 📜 Descripción del Código

El programa utiliza el módulo `nltk` para tokenizar una oración en
español y luego aplica **reglas simples** para etiquetar cada palabra
con su **categoría gramatical (POS)**.

### 🔍 Función principal: `analisis_morfologico(oracion)`

#### Parámetros

-   `oracion` *(str)*: Texto en español a analizar.

#### Retorna

Un diccionario con la siguiente información:

  Clave            Descripción
  ---------------- --------------------------------------------------------
  `total_tokens`   Número total de palabras y signos en la oración
  `total_tipos`    Número de palabras únicas
  `ratio_tt`       Proporción de tipos/tokens (diversidad léxica)
  `pos_tags`       Lista de tuplas con la forma `(palabra, etiqueta_POS)`

------------------------------------------------------------------------

## ⚙️ Instalación de dependencias

Antes de ejecutar el script, instala `nltk` si no lo tienes:

``` bash
pip install nltk
```

Y descarga los recursos necesarios:

``` python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('universal_tagset')
```

------------------------------------------------------------------------

## 💡 Ejemplo de uso

``` python
oracion_ejemplo = "El gato negro salta alto y el perro corre rápido por el parque."
resultado = analisis_morfologico(oracion_ejemplo)
print(resultado)
```

### 🧩 Salida esperada

``` python
{
    'total_tokens': 13,
    'total_tipos': 11,
    'ratio_tt': 0.846,
    'pos_tags': [
        ('El', 'DET'), ('gato', 'NOUN'), ('negro', 'ADJ'), ('salta', 'VERB'),
        ('alto', 'ADV'), ('y', 'CCONJ'), ('el', 'DET'), ('perro', 'NOUN'),
        ('corre', 'VERB'), ('rápido', 'ADJ'), ('por', 'ADP'), ('el', 'DET'),
        ('parque', 'NOUN'), ('.', 'PUNCT')
    ]
}
```

------------------------------------------------------------------------

## 🧩 Reglas básicas utilizadas

El etiquetado se basa en coincidencias simples y terminaciones comunes
del español:

-   **DET** → Determinantes: `el`, `la`, `un`, `una`...
-   **CCONJ** → Conjunciones: `y`, `o`, `pero`...
-   **ADP** → Preposiciones: `de`, `a`, `por`, `en`...
-   **ADV** → Palabras terminadas en `-mente`.
-   **VERB** → Palabras terminadas en `-ar`, `-er`, `-ir`, `-ando`,
    `-iendo`, `-ado`, `-ido`.
-   **PRON** → Pronombres personales (`yo`, `tú`, `él`, `nosotros`,
    `ellos`...)
-   **NOUN** → Se asigna por defecto si no coincide con ninguna regla.

---------------------------------------------------------------------
