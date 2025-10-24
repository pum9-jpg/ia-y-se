
# Sistema de Diagnóstico de Problemas en Bicicletas

Este proyecto presenta dos enfoques diferentes para modelar y resolver problemas en bicicletas mediante sistemas de conocimiento: **Reglas de Producción** y **Frames (Estructuras de Datos)**. Ambos métodos permiten identificar problemas a partir de síntomas y proporcionar soluciones, pero cada uno tiene ventajas y características particulares.

## Ejecutar desde la consola (Bash o PowerShell)

1. Guarda el código en un archivo, por ejemplo, `diagnostico_bicicleta.py`.
2. Abre la terminal o PowerShell y navega a la carpeta:

```bash
cd ruta/a/tu/carpeta
```

3. Ejecuta el script con Python:

```bash
python diagnostico_bicicleta.py
```


### 1. Reglas de Producción

- **Descripción:** Se definen reglas que relacionan síntomas con diagnósticos y soluciones, en forma de reglas condicionales.
- **Funcionamiento:** Se evalúan los hechos (síntomas) del usuario y se busca la primera regla que coincida con todos los síntomas. Luego, se obtiene el diagnóstico y la solución asociados.
- **Ventajas:** Fácil de ampliar con nuevas reglas, lógica sencilla y clara.
- **Limitaciones:** La estructura de reglas puede volverse compleja con muchas reglas y relaciones.

### 2. Frames (Estructuras de Datos)

- **Descripción:** Se representan los problemas y sus detalles como "frames" o estructuras con atributos específicos.
- **Funcionamiento:** Se busca un problema cuya lista de síntomas coincida completamente con los síntomas proporcionados por el usuario. Se obtiene información adicional como el tipo de problema, solución y herramientas necesarias.
- **Ventajas:** Mejor organización de la información, fácil acceso a detalles específicos y extensible.
- **Limitaciones:** La búsqueda puede ser menos eficiente con muchas entradas, y requiere mantener la base de datos estructurada.


4. Si se encuentra, se imprime la información del problema, solución y herramientas necesarias.

---

## Conclusión

Ambos enfoques son útiles para sistemas de diagnóstico y resolución de problemas, cada uno con sus ventajas:

- **Reglas de Producción:** ideales para sistemas con reglas claras y fáciles de ampliar mediante reglas condicionales. Son sencillas de entender y modificar.
- **Frames:** ofrecen una representación más estructurada y organizada de los problemas, permitiendo acceder fácilmente a detalles específicos y facilitando la extensión del conocimiento.

La elección entre uno u otro depende de la complejidad del dominio, la necesidad de organización y la facilidad de mantenimiento. En sistemas más grandes o complejos, los frames pueden ser más adecuados, mientras que para reglas simples, las reglas de producción son eficientes y fáciles de gestionar.

