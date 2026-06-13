import csv
import json

def leer_csv_login(ruta_archivo):
    """
    Lee el archivo CSV de credenciales de login.
    Retorna lista de tuplas para pytest.mark.parametrize.
    """
    datos_parametrizados = []
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Sanitización de datos y conversión del flag de control a booleano real
            usuario = fila["usuario"].strip()
            clave = fila["clave"].strip()
            debe_funcionar = fila["debe_funcionar"].strip().lower() == "true"
            descripcion = fila["descripcion"].strip()
            
            datos_parametrizados.append((usuario, clave, debe_funcionar, descripcion))
            
    return datos_parametrizados


def leer_json_productos(ruta_archivo):
    """
    Lee el archivo JSON de productos.
    Retorna lista de productos para parametrización.
    """
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        return json.load(archivo)