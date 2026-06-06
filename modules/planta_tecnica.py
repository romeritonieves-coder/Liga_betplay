"""
modules/planta_tecnica.py
-------------------------
Cuerpo tecnico: registro y consulta.
"""

from core.data import ligaBetplay, serializar
from core.persistence import guardar
from modules.equipos import elegir_equipo
from utils.helpers import limpiar, pausar, leer_texto
from menu.main_menu import titulo


def registrar_cuerpo_tecnico():
    limpiar()
    print(titulo())
    print('\n--- REGISTRO DE CUERPO TECNICO ---\n')

    nombre = elegir_equipo()
    if nombre is None:
        return

    eq = ligaBetplay[nombre]
    print(f'\nDatos para "{nombre}":\n')

    eq['plantel_tecnico']['director'] = leer_texto('Director tecnico: ')
    eq['plantel_tecnico']['preparador_arq'] = leer_texto('Preparador de arqueros: ')
    eq['plantel_tecnico']['preparador_fis'] = leer_texto('Preparador fisico: ')
    eq['plantel_tecnico']['medico'] = leer_texto('Medico: ')
    eq['plantel_tecnico']['fisioterapeuta'] = leer_texto('Fisioterapeuta: ')

    guardar(serializar())
    print('\nCuerpo tecnico guardado.')
    pausar()


def mostrar_cuerpo_tecnico(eq):
    limpiar()
    print(titulo())
    print(f'\n--- CUERPO TECNICO: {eq["nombre"]} ---\n')
    pt = eq['plantel_tecnico']
    print(f'Director tecnico      : {pt["director"]}')
    print(f'Preparador de arqueros: {pt["preparador_arq"]}')
    print(f'Preparador fisico     : {pt["preparador_fis"]}')
    print(f'Medico                : {pt["medico"]}')
    print(f'Fisioterapeuta        : {pt["fisioterapeuta"]}')
    pausar()
