"""
modules/estadisticas.py
-----------------------
Estadisticas individuales y tabla de posiciones.
Usa sorted() con lambda (logica distinta a tu burbuja).
"""

from core import data as _data
from utils.helpers import limpiar, pausar
from menu.main_menu import titulo


def mostrar_estadisticas(eq):
    limpiar()
    print(titulo())
    print(f'\n--- ESTADISTICAS: {eq["nombre"]} ---\n')
    s = eq['estadisticas']
    dif = s['goles_a_favor'] - s['goles_en_contra']
    print(f'  Partidos jugados : {s["partidos_jugados"]}')
    print(f'  Victorias        : {s["victorias"]}')
    print(f'  Empates          : {s["empates"]}')
    print(f'  Derrotas         : {s["derrotas"]}')
    print(f'  Goles a favor    : {s["goles_a_favor"]}')
    print(f'  Goles en contra  : {s["goles_en_contra"]}')
    print(f'  Diferencia       : {dif:+d}')
    print(f'  Puntos           : {s["puntos"]}')
    if s['forma']:
        print(f'  Ultimos 5 (G/E/P): {"".join(s["forma"])}')
    pausar()


def tabla_posiciones():
    limpiar()
    print(titulo())
    print('\n--- TABLA DE POSICIONES ---\n')

    if not _data.ligaBetplay:
        print('No hay equipos registrados.')
        pausar()
        return

    # Ordenamiento con sorted y lambda (mas pythonico que burbuja)
    ranking = sorted(
        _data.ligaBetplay.values(),
        key=lambda eq: (
            eq['estadisticas']['puntos'],
            eq['estadisticas']['goles_a_favor'] - eq['estadisticas']['goles_en_contra'],
            eq['estadisticas']['goles_a_favor']
        ),
        reverse=True
    )

    print(f'{"#":<4}{"Equipo":<22}{"PJ":>4}{"G":>4}{"E":>4}{"P":>4}'
          f'{"GF":>5}{"GC":>5}{"Dif":>5}{"Pts":>5}  Forma')
    print('-' * 65)

    for i, eq in enumerate(ranking, 1):
        s = eq['estadisticas']
        dif = s['goles_a_favor'] - s['goles_en_contra']
        forma = ''.join(s['forma']) if s['forma'] else '-'
        print(f'{i:<4}{eq["nombre"]:<22}'
              f'{s["partidos_jugados"]:>4}{s["victorias"]:>4}{s["empates"]:>4}{s["derrotas"]:>4}'
              f'{s["goles_a_favor"]:>5}{s["goles_en_contra"]:>5}{dif:>+5}{s["puntos"]:>5}  {forma}')

    pausar()
