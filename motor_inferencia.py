"""
motor_inferencia.py
=====================
Motor de inferencia del sistema basado en reglas.

En un sistema experto clásico, el "motor de inferencia" es el componente que
recorre la base de hechos, la contrasta con las reglas del sistema (proceso
llamado EQUIPARACIÓN o "pattern matching") y, cuando una regla aplica, la
"DISPARA" (fires) generando nuevo conocimiento derivado que no estaba escrito
explícitamente en la base de hechos original.

Aquí implementamos una única regla, pero es exactamente ese mecanismo:

    REGLA DE SIMETRÍA (transporte bidireccional):
    SI  conecta(A, B, t)
    Y   el sistema de transporte es bidireccional (un bus/troncal se puede
        recorrer en ambos sentidos)
    ENTONCES  conecta(B, A, t)

Es decir: por cada hecho conecta(A, B, t) de base_conocimiento.py, el motor
"dispara" la regla y concluye el hecho simétrico conecta(B, A, t), sin que
nosotros tengamos que escribirlo dos veces a mano en la base de hechos.

El resultado de aplicar la regla sobre TODOS los hechos es un grafo de
adyacencias: una estructura que ya no es lógica pura, sino la representación
navegable que usarán los algoritmos de búsqueda (busqueda.py).
"""

from base_conocimiento import obtener_hechos


def construir_grafo():
    """
    Recorre los hechos conecta(A, B, t) y dispara la regla de simetría sobre
    cada uno para construir el grafo de adyacencias.

    Devuelve:
        dict: { "Estacion": [("EstacionVecina", tiempo), ...], ... }
    """
    hechos = obtener_hechos()
    grafo = {}

    for estacion_a, estacion_b, tiempo in hechos:
        # Nos aseguramos de que ambas estaciones existan como nodos del grafo,
        # incluso si alguna todavía no tiene vecinos agregados.
        grafo.setdefault(estacion_a, [])
        grafo.setdefault(estacion_b, [])

        # Hecho original: conecta(A, B, t) -> se agrega tal cual (equiparación).
        grafo[estacion_a].append((estacion_b, tiempo))

        # Disparo de la regla de simetría: se infiere y agrega conecta(B, A, t).
        grafo[estacion_b].append((estacion_a, tiempo))

    return grafo


def listar_estaciones(grafo):
    """Devuelve la lista de todas las estaciones del grafo, ordenadas alfabéticamente."""
    return sorted(grafo.keys())
