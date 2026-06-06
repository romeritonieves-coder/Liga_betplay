"""
core/persistence.py
-------------------
Carga y guarda todo el estado en un unico archivo JSON.
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
ARCHIVO = os.path.join(DATA_DIR, 'liga.json')


def asegurar_directorio():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def guardar(estado):
    try:
        asegurar_directorio()
        with open(ARCHIVO, 'w', encoding='utf-8') as f:
            json.dump(estado, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Error al guardar: {e}')
        return False


def cargar():
    vacio = {'equipos': {}, 'partidos': [], 'proxima_jornada': 1}
    if not os.path.exists(ARCHIVO):
        return vacio
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        for k, v in vacio.items():
            datos.setdefault(k, v)
        return datos
    except (json.JSONDecodeError, IOError) as e:
        print(f'Advertencia: liga.json danado ({e}). Se inicia vacio.')
        return vacio
