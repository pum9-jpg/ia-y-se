


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

1. Guarda el archivo del programa, por ejemplo como:

   ```
   SE-diagnostico.py
   ```

2. Abre una terminal en la carpeta donde está el archivo.

3. Ejecuta el programa con:

   ```bash
   python SE-diagnostico.py
   ```
O correspondiente

---

## 🤖 Funcionamiento

El sistema separa claramente la base de conocimiento y el motor de inferencia, basando el resultado en solamente las reglas de esta.

Asi mismo, se muestra una explicacion de las reglas usadas para la conclucion dada.

---

## 🧩 Conclusión

En este sistema se muestra una base de conocimiento en base a reglas, como se vio en la  [practica 4](https://github.com/pum9-jpg/ia-y-se/tree/AlarconAriel/Practica4/practicas/p4-representacion-del-conocimiento), siendo altamente modular al presentar una separacion clara entre datos y procesamiento.

Esto tambien permite la explicacion de la inferencia basandose en los distintos datos presentes, permitiendo no solo dar la respuesta, si no mostrar el proceso que se siguio para tal conclucion, mostrando que puede ser replicable y simplificada.

---
