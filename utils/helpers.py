"""
utils/helpers.py
----------------
Funciones auxiliares para entrada/salida.
"""

import os


def limpiar():
    os.system('cls')


def pausar():
    input('\nPresione Enter para continuar...')


def leer_texto(msg, obligatorio=True):
    while True:
        v = input(msg).strip()
        if v != '' or not obligatorio:
            return v
        print('Error: el campo no puede estar vacio.')


def leer_opcion(msg, validas):
    """Lee una opcion validandola contra una tupla/lista de strings validos."""
    while True:
        op = input(msg).strip()
        if op in validas:
            return op
        print('Opcion no valida.')


def leer_entero(msg, minimo=None, maximo=None):
    while True:
        try:
            v = int(input(msg))
            if minimo is not None and v < minimo:
                print(f'Error: debe ser >= {minimo}.')
                continue
            if maximo is not None and v > maximo:
                print(f'Error: debe ser <= {maximo}.')
                continue
            return v
        except ValueError:
            print('Error: ingrese un numero entero.')


def validar_fecha(fecha):
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    d, m, a = partes
    if not (d.isdigit() and m.isdigit() and a.isdigit()):
        return False
    return 1 <= int(d) <= 31 and 1 <= int(m) <= 12 and int(a) >= 2000


def leer_fecha(msg):
    while True:
        f = input(msg)
        if validar_fecha(f):
            return f
        print('Formato invalido. Ejemplo: 15/06/2025')
