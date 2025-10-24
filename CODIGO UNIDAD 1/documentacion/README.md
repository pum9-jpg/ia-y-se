# Comandos de Git Bash

Aquí tienes una referencia de los comandos más comunes para trabajar con Git y la línea de comandos, basados en tu historial.

---

### Comandos de Navegación y Gestión de Archivos

Estos comandos te permiten moverte entre directorios y ver su contenido.

| Comando | Explicación | Ejemplo |
|---|---|---|
| `cd <directorio>` | Cambia al directorio especificado. El atajo `..` te lleva al directorio padre. | `cd ucatec/` |
| `mkdir <directorio>` | Crea un nuevo directorio. | `mkdir ia-y-se` |
| `ls` | Lista los archivos y subdirectorios del directorio actual. | `ls` |
| `ls -la` | Lista todos los archivos, incluyendo los ocultos (`.` y `..`), en un formato detallado. | `ls -la` |
| `ls -l` | Muestra el contenido con información extra como permisos, propietario y fecha de modificación. | `ls -l` |

---

### Comandos de Inicialización y Configuración de Git

Estos comandos se usan para empezar un proyecto con Git y conectarlo a un repositorio remoto.

| Comando | Explicación | Ejemplo |
|---|---|---|
| `git init` | Convierte el directorio actual en un repositorio de Git, creando la carpeta oculta `.git`. | `git init` |
| `git branch -M <nombre_rama>` | Renombra la rama actual. `-M` significa que la renombrará incluso si no existe. | `git branch -M master` |
| `git remote add <alias> <url>` | Conecta tu repositorio local a uno remoto, usando un alias (generalmente `origin`). | `git remote add origin git@github.com:pum9-jpg/ia-y-se.git` |
| `git clone <url> <directorio>` | Descarga un repositorio de Git completo a tu máquina local. Puedes especificar un nombre para la nueva carpeta. | `git clone git@github.com:pum9-jpg/ia-y-se.git ia-y-se-para-borrar` |

---

### Comandos para el Flujo de Trabajo de Git

Estos son los comandos clave para trabajar con tus archivos y subir los cambios.

| Comando | Explicación | Ejemplo |
|---|---|---|
| `git status` | Muestra el estado actual de tu repositorio. Te dice qué archivos han sido modificados, cuáles están listos para un commit y cuáles no tienen seguimiento. | `git status` |
| `git add .` | Agrega todos los archivos modificados o nuevos al área de *staging*, preparándolos para el próximo commit. | `git add .` |
| `git commit -m "<mensaje>"` | Guarda los cambios del área de *staging* como un nuevo commit con un mensaje descriptivo. | `git commit -m "Primer commit"` |
| `git log` | Muestra el historial de commits de tu rama actual. | `git log` |
| `git branch` | Lista todas las ramas en tu repositorio local. | `git branch` |
| `git push -u <alias> <rama>` | Sube los commits de tu rama local al repositorio remoto. La opción `-u` configura un enlace permanente entre tu rama local y la remota. | `git push -u origin master` |

---

### Comandos de Utilidad

| Comando | Explicación | Ejemplo |
|---|---|---|
| `code .` | Abre el editor de código Visual Studio Code en el directorio actual. | `code .` |
| `history` | Muestra los comandos que has ejecutado en tu sesión actual. | `history` |