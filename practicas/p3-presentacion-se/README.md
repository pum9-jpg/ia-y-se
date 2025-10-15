


## 🐍 Instalación de Python

Para ejecutar correctamente el programa, es necesario tener **Python 3.10 o superior** instalado en tu sistema.
Existen tres métodos recomendados:

---

### **1️⃣ Instalación desde Microsoft Store (Windows)**

1. Abre la **Microsoft Store**.
2. Busca **“Python 3.13”** (o la versión más reciente).
3. Haz clic en **Obtener** e instálalo.
4. Una vez instalado, abre una terminal (CMD o PowerShell) y verifica con:

   ```bash
   python --version
   ```

   Debe mostrar algo como:

   ```
   Python 3.13.0
   ```

> 💡 Este método es el más sencillo y recomendado por los desarrolladores de Python.

---

### **2️⃣ Instalación desde Visual Studio Code**

1. Descarga e instala **Visual Studio Code**.
2. Ve al menú de **Extensiones** (icono de cuadrado con esquinas).
3. Busca `Python` y selecciona **Python Extension Pack**.
4. VSCode instalará automáticamente el intérprete de Python junto con herramientas de soporte (debugger, formateo, linters, etc.).
5. Puedes abrir el terminal interno de VSCode y verificar:

   ```bash
   python --version
   ```

---

### **3️⃣ Instalación manual desde línea de comandos**

#### En Windows:

```bash
winget install -e --id Python.Python.3.13
```

#### En Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### En macOS:

```bash
brew install python
```

Una vez instalado, verifica la instalación:

```bash
python3 --version
```

---

## 🚀 Ejecución del Programa

1. Guarda el archivo del juego, por ejemplo como:

   ```
   tres_en_raya_ia.py
   ```

2. Abre una terminal en la carpeta donde está el archivo.

3. Ejecuta el programa con:

   ```bash
   python tres_en_raya_ia.py
   ```


---

## 🤖 Funcionamiento

### 1. Funcionamiento convencional (Sin IA)
El enfoque convencional tiene la logica de descision dentro del codigo, teniendo las reglas implementadas en condiciones `if`, `elif`, o `else`.
Cambiar reglas implica cambiar el codigo fuente y reestructurar estas condiciones.

### 2. Funcionamiento basado en reglas (Con IA)

Este enfoque divide el codigo en dos partes: La base de conociemiento, y el motor de inferencia.

Esto sigue una logica de que si las condiciones de una regla se cumplen, se aplica la conclusion de la misma.



---

## 🧩 Conclusión

El enfoque convencional sigue instrucciones fijas paso a paso, mientras el enfoque de IA "razona" sobre un conjunto de reglas.

Esto permite una mejor flexibilidad y modularidad, siendo que solo añade a su base de conocimiento en lugar de modificar las reglas y sus conclusiones correspondientes dentro del codigo.

---


