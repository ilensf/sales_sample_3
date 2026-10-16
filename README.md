
## Requisitos

- Python 3.9 o posterior
- Dependencias indicadas en `requirements.txt`

## Configuración

Desde la raíz del proyecto, crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell, actívalo con:

```powershell
.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Ejecuta el script desde la raíz del proyecto para que se resuelvan las rutas relativas a los datos:

```bash
python src/datos.py
```

El script lee los tres archivos de `datos/raw/`. Usan punto y coma como separador de campos y coma como separador decimal. El script concatena los archivos, conserva la primera fila de cada `id_venda` e imprime la suma de `importe` y el número de ventas únicas. Ambos valores se muestran con dos decimales. No se crea ningún archivo de salida.

## Estructura del proyecto

```text
datos/
	raw/       Archivos CSV de ventas originales
	clean/     Carpeta reservada para datos depurados
notebooks/   Cuadernos de Jupyter
output/      Carpeta reservada para resultados
sql/         Archivos SQL
src/         Scripts de Python
```
