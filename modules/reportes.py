"""
modules/reportes.py
-------------------
Reportes extra: ranking de goleadores y forma reciente.
"""

from core import data as _data
from menu.main_menu import titulo
from utils.helpers import limpiar, pausar


def ranking_goleadores():
    limpiar()
    print(titulo())
    print('\n--- RANKING DE GOLEADORES ---\n')

    # aplanar todos los jugadores en una sola lista
    lista = []
    for nombre_eq, eq in _data.ligaBetplay.items():
        for j in eq['jugadores']:
            lista.append((j['nombre'], nombre_eq, j.get('goles', 0)))

    if not lista:
        print('No hay jugadores registrados.')
        pausar()
        return

    ranking = sorted(lista, key=lambda x: x[2], reverse=True)

    print(f'{"#":<4}{"Jugador":<22}{"Equipo":<22}{"Goles":>6}')
    print('-' * 54)
    for i, (nom, eq, g) in enumerate(ranking, 1):
        print(f'{i:<4}{nom:<22}{eq:<22}{g:>6}')

    pausar()


def forma_reciente():
    limpiar()
    print(titulo())
    print('\n--- FORMA RECIENTE (ULTIMOS 5) ---\n')

    if not _data.ligaBetplay:
        print('No hay equipos.')
        pausar()
        return

    print(f'{"Equipo":<22}{"PJ":>4}  Forma')
    print('-' * 40)
    for nombre in sorted(_data.ligaBetplay.keys()):
        s = _data.ligaBetplay[nombre]['estadisticas']
        cadena = ''.join(s['forma']) if s['forma'] else '-'
        print(f'{nombre:<22}{s["partidos_jugados"]:>4}  {cadena}')

    pausar()
