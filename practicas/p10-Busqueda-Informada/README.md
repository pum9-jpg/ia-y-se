


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
   Parte1.py
   ```

2. Abre una terminal en la carpeta donde está el archivo.

3. Ejecuta el programa con:

   ```bash
   Python Busqueda-En-Mapa.py
   ```
O correspondiente

---

## 🤖 Funcionamiento

El algoritmo A* considera los costes para saber que camino puede ser mejor.
Mientras, la búsqueda no informada explora primero todo el mapa, y despues evalua los costes para ver cual fue el camino más corto.

---

## 🧩 Conclusión

ambos metodods termina hallando la ruta más óptima, la forma en la que trabajan tiene una diferencia de eficiencia.
Con esto, los agentes inteligentes pueden tener busquedas más precisas y efectivas.


---