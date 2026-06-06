"""
modules/equipos.py
------------------
Registro y selector de equipos (logica distinta: usa leer_opcion).
"""

from core.data import ligaBetplay, nuevo_equipo, serializar
from core.persistence import guardar
from utils.helpers import limpiar, pausar, leer_texto
from menu.main_menu import titulo


def elegir_equipo():
    """Muestra la lista de equipos y devuelve el nombre elegido o None."""
    if len(ligaBetplay) == 0:
        print('Aun no hay equipos registrados.')
        pausar()
        return None

    nombres = list(ligaBetplay.keys())
    print('\nEquipos disponibles:')
    for i, n in enumerate(nombres, 1):
        print(f'  {i}. {n}')
    print('  0. Cancelar')

    opcion = input('Seleccione: ').strip()
    if opcion == '0':
        return None
    try:
        idx = int(opcion) - 1
        if 0 <= idx < len(nombres):
            return nombres[idx]
    except ValueError:
        pass
    print('Opcion no valida.')
    pausar()
    return None


def registrar_equipo():
    limpiar()
    print(titulo())
    print('\n--- REGISTRO DE EQUIPO ---\n')

    nombre = leer_texto('Nombre del equipo: ')
    if nombre in ligaBetplay:
        print('Ese equipo ya esta registrado.')
        pausar()
        return

    ciudad = leer_texto('Ciudad: ')

    ligaBetplay[nombre] = nuevo_equipo(nombre, ciudad)
    guardar(serializar())

    print(f'\nEquipo "{nombre}" registrado correctamente.')
    pausar()
