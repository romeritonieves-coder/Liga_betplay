"""
modules/jugadores.py
--------------------
Registro y consulta de jugadores.
"""

from core.data import ligaBetplay, serializar
from core.persistence import guardar
from modules.equipos import elegir_equipo
from utils.helpers import limpiar, pausar, leer_texto, leer_entero
from menu.main_menu import titulo


def registrar_jugador():
    limpiar()
    print(titulo())
    print('\n--- REGISTRO DE JUGADOR ---\n')

    nombre = elegir_equipo()
    if nombre is None:
        return

    eq = ligaBetplay[nombre]

    while True:
        limpiar()
        print(titulo())
        print(f'\n--- REGISTRANDO JUGADOR EN: {nombre} ---')
        print(f'Jugadores actuales: {len(eq["jugadores"])}\n')

        nom = leer_texto('Nombre del jugador: ')
        nac = leer_texto('Nacionalidad: ')
        pos = leer_texto('Posicion: ')
        num = leer_entero('Numero de camiseta: ', minimo=1, maximo=99)
        edad = leer_entero('Edad: ', minimo=10, maximo=60)

        eq['jugadores'].append({
            'nombre': nom,
            'nacionalidad': nac,
            'posicion': pos,
            'numero': num,
            'edad': edad,
            'goles': 0
        })

        if leer_texto('\nAgregar otro? (s/n): ').lower() != 's':
            break

    guardar(serializar())
    print('Jugadores guardados.')
    pausar()


def mostrar_jugadores(eq):
    limpiar()
    print(titulo())
    print(f'\n--- JUGADORES: {eq["nombre"]} ---\n')

    jugadores = eq['jugadores']
    if not jugadores:
        print('No hay jugadores registrados.')
    else:
        print(f'{"N":>3}  {"Nombre":<20} {"Pos":<14} {"Cam":>3} {"Edad":>4} {"Nac":<12} {"G":>3}')
        print('-' * 65)
        for i, j in enumerate(jugadores, 1):
            print(f'{i:>3}  {j["nombre"]:<20} {j["posicion"]:<14} '
                  f'{j["numero"]:>3} {j["edad"]:>4} {j["nacionalidad"]:<12} {j["goles"]:>3}')

    pausar()
