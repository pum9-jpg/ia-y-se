# 🧩 DOCUMENTACIÓN – MODELOS DE REPRESENTACIÓN DEL CONOCIMIENTO EN PYTHON

## **Codigo 1: Reglas de Producción (IF – THEN)**

### 📌 **Cómo ejecutar el programa**
1. Abre un editor de código como **VS Code** o **IDLE de Python**.  
2. Crea un archivo nuevo y nómbralo por ejemplo: `Reglas_Producción.py`
3. Copia y pega el **Código 1** completo.  
4. Guarda el archivo.  
5. Ejecútalo presionando **F5** o desde la terminal con:
   ```bash
   python reglas_produccion.py
   ```
6. El programa llegaria a imprimir en consola el **diagnóstico** y la **solución** correspondientes a los síntomas definidos.

### ⚙️ **Explicación del código **

#### 🟩 Base de conocimiento
```python
base_conocimiento_reglas = { ... }
base_conocimiento_soluciones = { ... }
```
Se crean **dos conjuntos de reglas**:
- **Diagnóstico:** Asocia síntomas con un problema.
- **Solución:** Asocia un diagnóstico con la reparación correspondiente.

#### 🟩 Hechos del usuario
```python
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]
```
Son los **síntomas observados** por el usuario.

#### 🟩 Función principal
```python
def diagnosticar_con_reglas(hechos, reglas_diagnostico, reglas_solucion):
```
Analiza los síntomas y busca coincidencias en la base de conocimiento.

- Usa `all()` para comprobar si todos los síntomas del usuario están en la regla.
- Si se encuentra un diagnóstico, busca su solución.
- Si no hay coincidencia, muestra un mensaje.

#### 🟩 Ejecución final
```python
diagnosticar_con_reglas(hechos_usuario, base_conocimiento_reglas, base_conocimiento_soluciones)
```
## **Codigo 2: Representación mediante Marcos (Frames)**

### 📌 **Cómo ejecutar el programa**
1. Abre un nuevo archivo en tu editor y nómbralo: `Marcos_Frames.py`
2. Copia y pega el **Código 2** completo.
3. Guarda el archivo.
4. Ejecútalo con:
   ```bash
   python marcos_frames.py
   ```
5. El programa mostrará el **problema identificado**, el **tipo**, la **solución** y las **herramientas necesarias**.

### ⚙️ **Explicación del código (resumen por bloques)**

#### 🟩 Base de conocimiento
```python
base_conocimiento_frames = { ... }
```
Cada **frame** representa un **objeto o concepto**, con atributos o **slots** como:
- `es_un` → tipo de problema  
- `sintomas` → lista de síntomas  
- `solucion` → reparación recomendada  
- `herramientas_necesarias` → objetos necesarios

#### 🟩 Función de búsqueda
```python
def buscar_problema_por_sintomas(sintomas_usuario, base_de_datos):
```
- Recorre todos los frames.
- Usa `all()` para comparar los síntomas del usuario.
- Devuelve el **nombre del problema** y sus **detalles**.

#### 🟩 Hechos del usuario
```python
hechos_usuario = ["chasquido_al_pedalear", "cadena_salta"]
```

#### 🟩 Impresión de resultados
Si se encuentra coincidencia, se muestran:
- Tipo de problema.  
- Solución sugerida.  
- Herramientas necesarias.

### 🧠 Conclusiónes 

# codigo1
* El modelo basado en Reglas de Producción es ideal para representar conocimiento lógico o causal, donde una condición (SI) llegaria a generar una acción (ENTONCES).   
Esta se llegaria a utilizar comúnmente en sistemas expertos de diagnóstico.

# codigo2 
* El modelo de Marcos o Frames llega a organizar la información de manera estructurada y jerárquica, siendo similar a un objeto en POO.  
Esta llega a ser ideal para representar conocimiento descriptivo, agrupando todas las características de un elemento como ser síntomas, soluciones y herramientas.  
Esta llega a ser más flexible que las reglas, ya que permite añadir nuevos atributos fácilmente.

---
