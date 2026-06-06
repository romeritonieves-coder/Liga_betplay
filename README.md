# ⚽ Liga BetPlay v2

Versión alternativa del sistema de gestión de liga: misma estructura modular que la tuya, **sin POO**, pero con **lógica de desarrollo distinta**.

---

## 📌 Objetivo

Rehacer la versión original (con diccionarios) aplicando un **enfoque diferente** en la lógica: ordenamiento con `sorted/lambda`, sistema de **jornadas**, reportes extra, y un solo archivo JSON.

---

## 📁 Estructura del Proyecto

```
liga_betplay_amigo/
├── main.py                    # Entrada (if __name__ == '__main__')
│
├── core/
│   ├── __init__.py
│   ├── data.py                # Almacenes + moldes (nuevo_equipo, nuevo_partido)
│   └── persistence.py         # Carga/guarda en liga.json
│
├── data/
│   └── liga.json              # Unico archivo con todo el estado
│
├── modules/
│   ├── __init__.py
│   ├── equipos.py             # Modulo 1
│   ├── planta_tecnica.py      # Modulo 2
│   ├── jugadores.py           # Modulo 3
│   ├── partidos.py            # Modulo 4 - jornada
│   ├── resultados.py          # Modulo 5 - por jornada
│   ├── informacion.py         # Modulo 6 - consulta
│   ├── estadisticas.py        # Modulo 7 - tabla con sorted/lambda
│   └── reportes.py            # Modulo 8 - goleadores y forma
│
├── menu/
│   ├── __init__.py
│   └── main_menu.py           # Unica fuente de menus
│
├── utils/
│   ├── __init__.py
│   └── helpers.py             # leer_texto, leer_entero, leer_fecha, leer_opcion...
│
└── README.md
```
## 🔄 Diferencias de Lógica con la Versión Original

| Aspecto | Tu versión | Esta versión |
|---------|-----------|--------------|
| Ordenamiento tabla | Burbuja manual | `sorted(key=lambda ..., reverse=True)` |
| Programación partidos | Por fecha suelta | Por **jornada** (matchday) auto-incremental |
| Resultados | Por fecha | Por **jornada** |
| Persistencia | 2 JSON separados | 1 solo `liga.json` |
| Forma reciente (W/D/L) | No existía | Lista `forma` con últimos 5 resultados |
| Goleadores | No existía | Ranking ordenado con `sorted + lambda` |
| Validación opciones | Repetida en cada módulo | Función `leer_opcion()` reutilizable |
| Moldes de datos | Repetidos | Funciones `nuevo_equipo()` y `nuevo_partido()` en `core/data.py` |
| Acceso a datos | Import directo | `import core.data as _data` para mutar el estado |

---

## 🧩 Opciones del Menú

| # | Opción | Módulo |
|---|--------|--------|
| 1 | Registrar equipo | `equipos.py` |
| 2 | Registrar cuerpo técnico | `planta_tecnica.py` |
| 3 | Registrar jugador | `jugadores.py` |
| 4 | Programar jornada | `partidos.py` |
| 5 | Registrar resultados | `resultados.py` |
| 6 | Consultar información | `informacion.py` |
| 7 | Tabla de posiciones | `estadisticas.py` |
| 8 | Reportes | `reportes.py` |
| 0 | Salir | - |

---
