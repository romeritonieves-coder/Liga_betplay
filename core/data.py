"""
core/data.py
------------
Almacenes en memoria. Al importar se cargan desde JSON.
"""

from core.persistence import cargar

_estado = cargar()

# { nombre: { ...datos... } }
ligaBetplay = _estado['equipos']

# [ {jornada, fecha, local, visitante, goles_local, goles_visitante}, ... ]
calendario = _estado['partidos']

# Numero de la siguiente jornada a programar
proxima_jornada = _estado.get('proxima_jornada', 1)


def nuevo_equipo(nombre, ciudad=''):
    """Moldes/plantilla para un equipo nuevo (sin POO)."""
    return {
        'nombre': nombre,
        'ciudad': ciudad,
        'plantel_tecnico': {
            'director': '',
            'preparador_arq': '',
            'preparador_fis': '',
            'medico': '',
            'fisioterapeuta': ''
        },
        'jugadores': [],
        'estadisticas': {
            'partidos_jugados': 0,
            'victorias': 0,
            'empates': 0,
            'derrotas': 0,
            'goles_a_favor': 0,
            'goles_en_contra': 0,
            'puntos': 0,
            'forma': []   # ultimos 5 resultados: 'G','E','P'
        }
    }


def nuevo_partido(jornada, fecha, local, visitante):
    return {
        'jornada': jornada,
        'fecha': fecha,
        'local': local,
        'visitante': visitante,
        'goles_local': None,
        'goles_visitante': None
    }


def serializar():
    return {
        'equipos': ligaBetplay,
        'partidos': calendario,
        'proxima_jornada': proxima_jornada
    }
