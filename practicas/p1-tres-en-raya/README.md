# 🎮 Tres en raya en Python con IA (Groq)

Este proyecto es un juego de **Tres en Raya (Tic-Tac-Toe)** desarrollado en **Python**, donde puedes jugar:

- 🧍‍♂️ **Entre dos jugadores humanos**  
- 🤖 **Contra una IA** usando la **API de Groq**

---

## ⚙️ Requisitos para ejecutar el programa

Antes de ejecutar el juego, asegúrate de tener lo siguiente:

### 1. 🐍 Python 3.10 o superior
Comprueba si tienes Python instalado ejecutando en la terminal:

```bash
python --version
```

Si no lo tienes, descárgalo desde [python.org/downloads](https://www.python.org/downloads/)

---

### 2. 📦 Librería `requests`
Esta librería permite que el programa se comunique con la API de Groq.  
Instálala ejecutando:

```bash
pip install requests
```

---

### 3. 🌐 Conexión a Internet
Solo necesaria si deseas jugar **contra la IA**, ya que el programa se conecta con la **API de Groq**.

---

### 4. 🔑 API Key de Groq
Para usar la IA, reemplaza tu clave en el archivo `jg.py`:

```python
API_KEY = "TU_API_KEY_AQUI"
```

Puedes obtener una API Key en: [https://console.groq.com/](https://console.groq.com/)

---

## ▶️ Cómo ejecutar el programa

1. Abre una terminal o consola en la carpeta donde se encuentra el archivo:

   ```bash
   cd ruta/a/tu/proyecto
   ```

2. Ejecuta el script principal:

   ```bash
   python jg.py
   ```

3. Aparecerá el menú principal:

   ```
   1) Instrucciones
   2) Jugar 2 jugadores
   3) Jugar contra IA (Groq)
   4) Salir
   ```

4. Ingresa la opción deseada y sigue las instrucciones en pantalla.

---

## 🧠 Modo IA (Groq)

Cuando eliges el modo contra la IA, el programa envía el estado actual del tablero a la **API de Groq**, la cual devuelve la mejor jugada posible según el modelo de lenguaje.  
Esto permite que el juego tenga un comportamiento inteligente y competitivo.

---

## 📁 Estructura del proyecto

```
📦 Tres_en_raya_groq/
│
├── jg.py       # Código principal del juego
└──  README.md             # Documentación del proyecto
```

---

## 💡 Sugerencias

- Puedes modificar la lógica de la IA para probar distintos modelos de Groq.  
- Si prefieres jugar sin conexión, usa el modo **2 jugadores**.  
- Asegúrate de mantener tu **API Key privada** y no subirla a repositorios públicos.

---
