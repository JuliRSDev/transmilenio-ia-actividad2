"""
busqueda.py
=====================
Algoritmos de búsqueda sobre el grafo generado por el motor de inferencia.

Se implementan tres estrategias clásicas de búsqueda en espacios de estados
(cada "estado" es una estación, y cada movimiento es tomar un tramo de
troncal hacia una estación vecina):

1. BFS (Breadth-First Search) -> búsqueda NO INFORMADA.
   No usa ningún conocimiento adicional sobre el problema (no le importa el
   tiempo de los tramos, solo la cantidad de saltos). Es óptima únicamente
   respecto al NÚMERO DE ESTACIONES recorridas, no respecto al tiempo total.

2. Dijkstra -> búsqueda NO INFORMADA de costo uniforme.
   Tampoco usa conocimiento extra del problema, pero sí considera el peso
   (tiempo) de cada tramo. Es óptima respecto al TIEMPO TOTAL de viaje.

3. A* -> búsqueda INFORMADA.
   Usa una heurística (conocimiento adicional: la distancia geográfica en
   línea recta entre estaciones) para guiar la exploración hacia el destino
   más rápido que Dijkstra, sin sacrificar optimalidad (siempre que la
   heurística sea admisible, es decir, que nunca sobreestime el costo real).

Todas las funciones devuelven una tupla:
    (camino, costo_total, nodos_explorados)
o `None` si no existe una ruta entre origen y destino.
"""

import heapq
import math
from collections import deque


def bfs(grafo, inicio, destino):
    """
    Búsqueda no informada por amplitud (breadth-first).

    Encuentra el camino con el MENOR NÚMERO DE SALTOS (estaciones), sin
    considerar el tiempo de cada tramo. Por eso puede no ser el camino más
    rápido en minutos.
    """
    if inicio not in grafo or destino not in grafo:
        return None

    visitados = {inicio}
    cola = deque([(inicio, [inicio], 0)])
    nodos_explorados = 0

    while cola:
        actual, camino, costo_acumulado = cola.popleft()
        nodos_explorados += 1

        if actual == destino:
            return (camino, costo_acumulado, nodos_explorados)

        for vecino, tiempo in grafo[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino], costo_acumulado + tiempo))

    return None


def dijkstra(grafo, inicio, destino):
    """
    Búsqueda no informada de costo uniforme (algoritmo de Dijkstra).

    Encuentra el camino de MENOR TIEMPO TOTAL, explorando siempre primero el
    nodo con menor costo acumulado conocido hasta el momento (cola de
    prioridad / heapq).
    """
    if inicio not in grafo or destino not in grafo:
        return None

    cola_prioridad = [(0, inicio, [inicio])]
    costos_minimos = {inicio: 0}
    nodos_explorados = 0

    while cola_prioridad:
        costo_acumulado, actual, camino = heapq.heappop(cola_prioridad)
        nodos_explorados += 1

        if actual == destino:
            return (camino, costo_acumulado, nodos_explorados)

        # Si ya encontramos un camino más barato a "actual" antes, este
        # elemento de la cola quedó obsoleto: lo ignoramos.
        if costo_acumulado > costos_minimos.get(actual, math.inf):
            continue

        for vecino, tiempo in grafo[actual]:
            nuevo_costo = costo_acumulado + tiempo
            if nuevo_costo < costos_minimos.get(vecino, math.inf):
                costos_minimos[vecino] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino, camino + [vecino]))

    return None


def heuristica(estacion_a, estacion_b, coordenadas):
    """
    Heurística de A*: estima el tiempo de viaje entre dos estaciones a partir
    de la distancia euclidiana entre sus coordenadas geográficas.

    Es el "conocimiento adicional" que convierte esta búsqueda en informada.
    Para que A* siga siendo óptimo, la heurística debe ser ADMISIBLE (nunca
    debe sobreestimar el costo real): por eso se asume una velocidad
    optimista de 40 km/h, más rápida que cualquier tramo real del sistema.
    """
    lat_a, lon_a = coordenadas[estacion_a]
    lat_b, lon_b = coordenadas[estacion_b]

    # 1 grado de latitud/longitud equivale aproximadamente a 111 km en Bogotá.
    distancia_grados = math.sqrt((lat_a - lat_b) ** 2 + (lon_a - lon_b) ** 2)
    distancia_km = distancia_grados * 111

    velocidad_optimista_kmh = 40
    tiempo_estimado_minutos = distancia_km * (60 / velocidad_optimista_kmh)

    return tiempo_estimado_minutos


def a_estrella(grafo, inicio, destino, coordenadas):
    """
    Búsqueda informada A*.

    Igual que Dijkstra, pero la cola de prioridad ordena los nodos por
    f(n) = g(n) + h(n), donde:
        g(n) = costo real acumulado desde el inicio hasta n.
        h(n) = heurística (estimación optimista) desde n hasta el destino.

    Con una heurística admisible, A* garantiza el mismo camino óptimo que
    Dijkstra, pero típicamente explorando MENOS nodos.
    """
    if inicio not in grafo or destino not in grafo:
        return None

    g_inicial = 0
    f_inicial = g_inicial + heuristica(inicio, destino, coordenadas)
    cola_prioridad = [(f_inicial, g_inicial, inicio, [inicio])]
    costos_minimos = {inicio: 0}
    nodos_explorados = 0

    while cola_prioridad:
        _, costo_acumulado, actual, camino = heapq.heappop(cola_prioridad)
        nodos_explorados += 1

        if actual == destino:
            return (camino, costo_acumulado, nodos_explorados)

        if costo_acumulado > costos_minimos.get(actual, math.inf):
            continue

        for vecino, tiempo in grafo[actual]:
            nuevo_costo = costo_acumulado + tiempo
            if nuevo_costo < costos_minimos.get(vecino, math.inf):
                costos_minimos[vecino] = nuevo_costo
                f = nuevo_costo + heuristica(vecino, destino, coordenadas)
                heapq.heappush(cola_prioridad, (f, nuevo_costo, vecino, camino + [vecino]))

    return None
