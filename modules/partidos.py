"""
modules/partidos.py
-------------------
Programacion por JORNADA (no por fecha suelta).
"""

from core import data as _data
from core.persistence import guardar
from utils.helpers import limpiar, pausar, leer_entero, leer_fecha
from menu.main_menu import titulo


def _seleccionar(msg, excluir=None):
    nombres = [n for n in _data.ligaBetplay.keys() if n != excluir]
    if not nombres:
        return None
    print('\nEquipos:')
    for i, n in enumerate(nombres, 1):
        print(f'  {i}. {n}')
    while True:
        op = input(msg).strip()
        try:
            idx = int(op) - 1
            if 0 <= idx < len(nombres):
                return nombres[idx]
        except ValueError:
            pass
        print('Opcion invalida.')


def programar_jornada():
    limpiar()
    print(titulo())
    print('\n--- PROGRAMACION DE JORNADA ---\n')

    if len(_data.ligaBetplay) < 2:
        print('Necesita al menos 2 equipos.')
        pausar()
        return

    jornada = _data.proxima_jornada
    print(f'Programando JORNADA N. {jornada}\n')
    cantidad = leer_entero('Cuantos partidos tiene?: ', minimo=1)

    equipos_disponibles = list(_data.ligaBetplay.keys())

    for n in range(1, cantidad + 1):
        limpiar()
        print(titulo())
        print(f'\nJornada {jornada} - Partido {n} de {cantidad}\n')

        fecha = leer_fecha('Fecha (dd/mm/aaaa): ')

        # excluir los que ya juegan como local en esta jornada
        locales_usados = {p['local'] for p in _data.calendario if p['jornada'] == jornada}
        nombres = [nom for nom in equipos_disponibles if nom not in locales_usados]
        if len(nombres) < 2:
            print('No quedan equipos para emparejar.')
            break

        print('Equipos disponibles para LOCAL:')
        for i, nom in enumerate(nombres, 1):
            print(f'  {i}. {nom}')

        while True:
            op = input('Seleccione local: ').strip()
            try:
                idx = int(op) - 1
                if 0 <= idx < len(nombres):
                    local = nombres[idx]
                    break
            except ValueError:
                pass
            print('Opcion invalida.')

        visitante = _seleccionar('Seleccione visitante: ', excluir=local)
        if visitante is None:
            continue

        _data.calendario.append(_data.nuevo_partido(jornada, fecha, local, visitante))
        guardar(_data.serializar())
        print(f'\nPartido agregado: {local} vs {visitante} ({fecha})')

    # avanzar a la siguiente jornada
    _data.proxima_jornada = jornada + 1
    guardar(_data.serializar())
    pausar()
