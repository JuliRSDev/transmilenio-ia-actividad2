"""
base_conocimiento.py
=====================
Base de conocimiento del sistema experto de rutas de TransMilenio (Bogotá).

En un sistema basado en reglas, el conocimiento del "mundo" se representa como
HECHOS en lógica de primer orden. Aquí el hecho fundamental es:

    conecta(EstacionA, EstacionB, tiempo_en_minutos)

que se lee como: "existe una conexión directa (un tramo de troncal) entre
EstacionA y EstacionB, y recorrerla toma 'tiempo_en_minutos' minutos".

Estos hechos NO son un grafo todavía: son solo proposiciones lógicas sueltas.
Es tarea del motor de inferencia (motor_inferencia.py) "disparar" la regla de
simetría sobre estos hechos y construir la estructura de grafo navegable.

IMPORTANTE (alcance académico): las estaciones son reales del sistema
TransMilenio de Bogotá, pero las coordenadas y los tiempos de viaje entre
estaciones son APROXIMADOS, estimados con fines exclusivamente académicos
para esta actividad. No son datos oficiales de TransMilenio S.A.
"""

# ---------------------------------------------------------------------------
# HECHOS TIPO 1: coordenadas(Estacion, latitud, longitud)
# ---------------------------------------------------------------------------
# Se usan únicamente como apoyo para la heurística de A* (busqueda.py), que
# necesita estimar la distancia geográfica "en línea recta" entre dos
# estaciones para guiar la búsqueda informada.
coordenadas = {
    "Portal Norte":        (4.7590, -74.0460),
    "Toberín":             (4.7480, -74.0470),
    "Mazurén":             (4.7290, -74.0500),
    "Calle 100":           (4.6870, -74.0530),
    "Héroes":              (4.6650, -74.0640),
    "Calle 72":            (4.6580, -74.0650),
    "Av. Jiménez":         (4.6015, -74.0715),
    "Tercer Milenio":      (4.5970, -74.0850),
    "Museo del Oro":       (4.6015, -74.0720),
    "Las Aguas":           (4.5985, -74.0665),
    "CAN":                 (4.6555, -74.0930),
    "Av. Rojas":           (4.6470, -74.0950),
    "Ricaurte":            (4.6155, -74.0925),
    "Comuneros":           (4.5950, -74.0980),
    "Portal Sur":          (4.5560, -74.1520),
    "Salitre El Greco":    (4.6635, -74.1020),
    "Modelia":             (4.6605, -74.1230),
    "Portal El Dorado":    (4.6960, -74.1470),
    "Banderas":            (4.6270, -74.1180),
    "Portal Américas":     (4.6250, -74.1660),
}

# ---------------------------------------------------------------------------
# HECHOS TIPO 2: conecta(EstacionA, EstacionB, tiempo_en_minutos)
# ---------------------------------------------------------------------------
# Cada tupla es un hecho independiente de la base de conocimiento. Solo se
# declara UNA dirección de cada tramo: la regla de simetría (transporte
# bidireccional) que agrega la dirección inversa se aplica después, en el
# motor de inferencia, no aquí. Esto evita duplicar conocimiento a mano.
#
# El último hecho (Mazurén -> CAN) representa una ruta alimentadora directa
# (un bus expreso que se salta varias estaciones intermedias): tiene MENOS
# paradas que ir por el troncal, pero por congestión tarda más tiempo total.
# Este hecho es clave para la actividad: permite mostrar en la demo que BFS
# (que minimiza número de saltos) y Dijkstra/A* (que minimizan tiempo) pueden
# dar respuestas distintas.
conexiones = [
    # --- Troncal Autonorte / Caracas (norte -> centro) ---
    ("Portal Norte", "Toberín", 6),
    ("Toberín", "Mazurén", 5),
    ("Mazurén", "Calle 100", 8),
    ("Calle 100", "Héroes", 7),
    ("Héroes", "Calle 72", 3),
    ("Calle 72", "Av. Jiménez", 6),
    ("Av. Jiménez", "Tercer Milenio", 5),

    # --- Ramal Eje Ambiental ---
    ("Av. Jiménez", "Museo del Oro", 2),
    ("Museo del Oro", "Las Aguas", 2),

    # --- Troncal NQS ---
    ("Héroes", "CAN", 5),
    ("CAN", "Av. Rojas", 4),
    ("Av. Rojas", "Ricaurte", 6),
    ("Ricaurte", "Tercer Milenio", 4),   # cruce NQS <-> Caracas
    ("Ricaurte", "Comuneros", 5),
    ("Comuneros", "Portal Sur", 12),

    # --- Troncal Calle 26 (hacia el Aeropuerto) ---
    ("CAN", "Salitre El Greco", 4),
    ("Salitre El Greco", "Modelia", 6),
    ("Modelia", "Portal El Dorado", 9),

    # --- Troncal Américas ---
    ("Ricaurte", "Banderas", 7),
    ("Banderas", "Portal Américas", 14),

    # --- Ruta alimentadora directa (menos paradas, más tiempo) ---
    ("Mazurén", "CAN", 25),
]


def obtener_hechos():
    """Devuelve la lista de hechos conecta(A, B, t) de la base de conocimiento."""
    return conexiones


def obtener_coordenadas():
    """Devuelve el diccionario de hechos coordenadas(Estacion, lat, lon)."""
    return coordenadas
