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
Basado en Reglas

Es un mini “sistema experto”. La lógica de negocio está con un diccionarios con condiciones y un motor que las evalúa y n base a eso toma decisiones claras y auditables que pueden cambiar a menudo sin tocar el motor.

Frames

Este es como una IA simbólica. Cada frame describe un objeto-problema como síntomas, solución, herramientas, y demas.
sirve para saber donde conviene agrupar atributos de entidades tambien para consultar y razonar sobre propiedades de objetos y relaciones
