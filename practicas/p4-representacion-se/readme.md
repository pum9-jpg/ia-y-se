Guía rápida de ejecucion

1. Ejecutar en Visual Studio Code (Windows/Mac/Linux)
   Prerrequisitos

Python 3.9+ instalado

Verifica en Terminal/PowerShell: python --version (o python3 --version)

Visual Studio Code instalado

Extensión de VS Code: Python (Microsoft)

A. Proyecto “Basado en Reglas”

Crea una carpeta de trabajo (p. ej. sistemas_expertos).

Abre la carpeta en VS Code (File > Open Folder).

Crea el archivo bebida_reglas.py.

Pega el código del “Enfoque Basado en Reglas”.

Selecciona intérprete de Python en VS Code

Haz clic en la barra de estado (esquina inferior derecha) y elige tu Python 3.x.

Ejecuta:

Opción 1: Botón ▶️ “Run Python File”.

Opción 2: Terminal integrada:

python bebida_reglas.py

(en algunos sistemas: python3 bebida_reglas.py)

Observa la salida en la terminal.

(Opcional) Cambia valores en hechos_usuario y vuelve a ejecutar para ver nuevas recomendaciones.

B. Proyecto “Frames (Marcos)”

En la misma carpeta, crea bicicleta_frames.py.

Pega el código del ejemplo de Frames/Marcos.

Ejecuta:

▶️ “Run Python File” o:

python bicicleta_frames.py

Observa la salida y prueba cambiando la lista hechos_usuario (síntomas) para ver diferentes resultados.

Resumen:

reglas

el codigo funca como un mini sistema experto en la cual esta actua mediante reglas ya definidas, este cuenta con un motor de inferencia que compara resultados que ingresa el usuario y de acuerdo a eso busca reglas que coinciden con las condiciones y asi tener un resultado de la recomendacion

frames

este sirve como un sistema de diagnostico simple, los frames se representan en un tipo de problema y cada uno de estos tiene sus atributos que lo describen, cuando el usuario ingresa un frame, se tiene ya informacion de lo que puede ser el problema, ya con esto puede devolver una posible solucion y lo que podamos necesitar para realizarlo
