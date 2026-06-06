"""
modules/resultados.py
---------------------
Registro de resultados por JORNADA.
"""

from core import data as _data
from core.persistence import guardar
from utils.helpers import limpiar, pausar, leer_entero
from menu.main_menu import titulo


def registrar_resultados():
    limpiar()
    print(titulo())
    print('\n--- REGISTRO DE RESULTADOS ---\n')

    pendientes = [p for p in _data.calendario if p['goles_local'] is None]
    if not pendientes:
        print('No hay partidos pendientes.')
        pausar()
        return

    jornadas = sorted({p['jornada'] for p in pendientes})
    print('Jornadas con partidos pendientes:')
    for j in jornadas:
        cant = sum(1 for p in pendientes if p['jornada'] == j)
        print(f'  Jornada {j}: {cant} partidos')

    jor = leer_entero('\nNumero de jornada: ',
                      minimo=min(jornadas), maximo=max(jornadas))

    de_jornada = [p for p in pendientes if p['jornada'] == jor]
    if not de_jornada:
        print('No hay partidos en esa jornada.')
        pausar()
        return

    print(f'\nPartidos de la jornada {jor}:')
    for i, p in enumerate(de_jornada, 1):
        print(f'  {i}. {p["local"]} vs {p["visitante"]} ({p["fecha"]})')
    print('  0. Cancelar')

    while True:
        op = input('\nSeleccione partido: ').strip()
        if op == '0':
            return
        try:
            idx = int(op) - 1
            if 0 <= idx < len(de_jornada):
                partido = de_jornada[idx]
                break
        except ValueError:
            pass
        print('Opcion invalida.')

    gl = leer_entero(f'Goles de {partido["local"]}: ', minimo=0)
    gv = leer_entero(f'Goles de {partido["visitante"]}: ', minimo=0)

    partido['goles_local'] = gl
    partido['goles_visitante'] = gv

    # actualizar estadisticas
    eq_local = _data.ligaBetplay[partido['local']]
    eq_visita = _data.ligaBetplay[partido['visitante']]

    for eq, gf, gc in [(eq_local, gl, gv), (eq_visita, gv, gl)]:
        s = eq['estadisticas']
        s['partidos_jugados'] += 1
        s['goles_a_favor'] += gf
        s['goles_en_contra'] += gc
        if gf > gc:
            s['victorias'] += 1
            s['puntos'] += 3
            s['forma'].append('G')
        elif gf < gc:
            s['derrotas'] += 1
            s['forma'].append('P')
        else:
            s['empates'] += 1
            s['puntos'] += 1
            s['forma'].append('E')
        # mantener ultimos 5
        if len(s['forma']) > 5:
            s['forma'] = s['forma'][-5:]

    guardar(_data.serializar())

    print('\nResultado registrado:')
    print(f'  {partido["local"]} {gl} - {gv} {partido["visitante"]}')
    pausar()
