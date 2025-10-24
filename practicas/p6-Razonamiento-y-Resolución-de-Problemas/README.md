


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

3. Antes de ejecutar el programa, asegurate de tener installadas las librerias. En este caso se usa:

```bash
pip install scikit-learn pandas
```
##### :warning: Es posible que la instalacion se realize en otro entorno distinto al usado en Visual Studio Code
Si tras la installacion se muetra error y aun no detecta las librerias, verifica con:

```bash
pip show scikit-learn
```

Esto mostrará la dirección donde se instaló, y presionando `Ctrl + Shift + P` se abrirá la paleta de comandos, ahi busca: `Python: Select Interpreter`. En este, busca uno con la dirección descrita previamente.
Si no encuentras dicha dirección, añadela con `Enter interpretrer path`. Esto abrirá el navegador de archivos, y selecciona el archivo `python.exe` dentro del direcctorio especificado.

4. Ejecuta el programa con:

   ```bash
   Parte1.py
   ```
O correspondiente

---

## 🤖 Funcionamiento

En la parte uno (1) las reglas ya estan descritas y la conclusion sigue una linea logica.

En cambio, la parte dos (2), tiene una lista de ejemplos de la que se basa para nuevos datos.

---

## 🧩 Conclusión

El sistema, en sus dos partes, muestra las diferencias entre deducción e inducción.
Siendo que la deducción replica un razonamiento. Mientras la inducción "aprende" sus propias reglas en base a conocimientos previos.
Si bien en este se muestran separados, son mas bien complementarios.

---