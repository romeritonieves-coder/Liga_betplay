"""
modules/informacion.py
----------------------
Submenu de consultas.
"""

from core import data as _data
from modules.equipos import elegir_equipo
from modules.planta_tecnica import mostrar_cuerpo_tecnico
from modules.jugadores import mostrar_jugadores
from modules.estadisticas import mostrar_estadisticas
from menu.main_menu import titulo, submenu_consulta, imprimir
from utils.helpers import limpiar, pausar


def consultar_informacion():
    limpiar()
    print(titulo())
    print('\n--- CONSULTAR INFORMACION ---\n')

    nombre = elegir_equipo()
    if nombre is None:
        return

    while True:
        limpiar()
        print(titulo())
        print(f'\nEquipo: {nombre}\n')
        imprimir(submenu_consulta())
        op = input('\nOpcion: ').strip()

        eq = _data.ligaBetplay[nombre]
        if op == '1':
            mostrar_cuerpo_tecnico(eq)
        elif op == '2':
            mostrar_jugadores(eq)
        elif op == '3':
            mostrar_estadisticas(eq)
        elif op == '4':
            mostrar_cuerpo_tecnico(eq)
            mostrar_jugadores(eq)
            mostrar_estadisticas(eq)
        elif op == '5':
            break
        else:
            print('Opcion invalida.')
            pausar()
