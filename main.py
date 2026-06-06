"""
main.py
-------
Punto de entrada de Liga BetPlay.
Muestra el menu principal y enruta cada opcion al modulo correspondiente.
"""

from core import data as _data
from core.persistence import guardar
from menu.main_menu import titulo, menu_principal, submenu_reportes, imprimir
from modules.equipos import registrar_equipo
from modules.planta_tecnica import registrar_cuerpo_tecnico
from modules.jugadores import registrar_jugador
from modules.partidos import programar_jornada
from modules.resultados import registrar_resultados
from modules.informacion import consultar_informacion
from modules.estadisticas import tabla_posiciones
from modules.reportes import ranking_goleadores, forma_reciente
from utils.helpers import limpiar, pausar


def submenu_reportes_loop():
    while True:
        limpiar()
        print(titulo())
        print('\n--- REPORTES ---\n')
        imprimir(submenu_reportes())
        op = input('\nOpcion: ').strip()
        if op == '1':
            ranking_goleadores()
        elif op == '2':
            forma_reciente()
        elif op == '3':
            return
        else:
            print('Opcion invalida.')
            pausar()


def ejecutar(opcion):
    """Enruta la opcion al modulo correspondiente."""
    try:
        if opcion == '1':
            registrar_equipo()
        elif opcion == '2':
            registrar_cuerpo_tecnico()
        elif opcion == '3':
            registrar_jugador()
        elif opcion == '4':
            programar_jornada()
        elif opcion == '5':
            registrar_resultados()
        elif opcion == '6':
            consultar_informacion()
        elif opcion == '7':
            tabla_posiciones()
        elif opcion == '8':
            submenu_reportes_loop()
        elif opcion == '0':
            return False
        else:
            print('Opcion no valida.')
            pausar()
    except Exception as e:
        print(f'\nError inesperado: {e}')
        pausar()
    return True


def main():
    continuar = True
    while continuar:
        limpiar()
        print(titulo())
        imprimir(menu_principal())
        opcion = input('\nSeleccione una opcion: ').strip()
        continuar = ejecutar(opcion)

    guardar(_data.serializar())
    print('\nDatos guardados. Hasta pronto.')


if __name__ == '__main__':
    main()
