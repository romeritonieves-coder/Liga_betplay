"""
menu/main_menu.py
-----------------
Unica fuente de los menus del sistema.
"""


def titulo():
    return '================================\n   LIGA BETPLAY  (v2)\n================================'


def menu_principal():
    return [
        '1. Registrar equipo',
        '2. Registrar cuerpo tecnico',
        '3. Registrar jugador',
        '4. Programar jornada',
        '5. Registrar resultados',
        '6. Consultar informacion',
        '7. Tabla de posiciones',
        '8. Reportes (goleadores / forma reciente)',
        '0. Salir'
    ]


def submenu_consulta():
    return [
        '1. Ver cuerpo tecnico',
        '2. Ver jugadores',
        '3. Ver estadisticas',
        '4. Ver todo',
        '5. Volver'
    ]


def submenu_reportes():
    return [
        '1. Ranking de goleadores',
        '2. Forma reciente de los equipos',
        '3. Volver'
    ]


def imprimir(items):
    for it in items:
        print(it)
