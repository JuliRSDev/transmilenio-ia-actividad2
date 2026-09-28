"""
main.py
=====================
Interfaz de consola del sistema experto de rutas de TransMilenio.

Flujo del programa:
    1. Se construye el grafo a partir de la base de conocimiento, disparando
       la regla de simetría en el motor de inferencia.
    2. Se muestra el menú de estaciones disponibles.
    3. El usuario ingresa una estación de origen (punto A) y una de destino
       (punto B).
    4. Se ejecutan los tres algoritmos de búsqueda (BFS, Dijkstra, A*) sobre
       el mismo grafo y se muestran los tres resultados, para poder
       compararlos.

Este archivo se puede usar de dos formas:
    - Interactiva:   python main.py
    - Con argumentos (útil para pruebas automatizadas):
                     python main.py "Portal Norte" "Portal Sur"
"""

import sys

from motor_inferencia import construir_grafo, listar_estaciones
from busqueda import bfs, dijkstra, a_estrella
from base_conocimiento import obtener_coordenadas

# En Windows la consola a veces usa una codificación (cp1252) que no soporta
# tildes ni emojis. Forzamos UTF-8 en la salida estándar para evitar errores
# de impresión, sin afectar el comportamiento en Linux/Mac.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def mostrar_menu_estaciones(estaciones):
    print("\nEstaciones disponibles en el sistema:")
    print("-" * 60)
    for i, estacion in enumerate(estaciones, start=1):
        print(f"  {i:>2}. {estacion}")
    print("-" * 60)


def pedir_estacion(mensaje, estaciones):
    """Pide una estación por consola y valida que exista en el grafo."""
    while True:
        valor = input(mensaje).strip()
        if valor in estaciones:
            return valor
        print(f'  ⚠️  "{valor}" no está en la lista de estaciones. Escríbela tal cual aparece arriba.')


def formatear_resultado(nombre_algoritmo, resultado):
    """Da formato de impresión a un resultado (camino, costo, nodos_explorados) o None."""
    print(f"\n🔹 {nombre_algoritmo}")
    if resultado is None:
        print("   No existe una ruta entre las estaciones indicadas.")
        return

    camino, costo_total, nodos_explorados = resultado
    print(f"   Ruta:              {' -> '.join(camino)}")
    print(f"   N° de estaciones:   {len(camino)}")
    print(f"   Tiempo total:       {costo_total} min")
    print(f"   Nodos explorados:   {nodos_explorados}")


def calcular_y_mostrar_rutas(grafo, coordenadas, origen, destino):
    print("\n" + "=" * 60)
    print(f"RUTAS DE {origen} A {destino}")
    print("=" * 60)

    resultado_bfs = bfs(grafo, origen, destino)
    resultado_dijkstra = dijkstra(grafo, origen, destino)
    resultado_a_estrella = a_estrella(grafo, origen, destino, coordenadas)

    formatear_resultado("BFS (no informada, menor n° de saltos)", resultado_bfs)
    formatear_resultado("Dijkstra (no informada, costo uniforme)", resultado_dijkstra)
    formatear_resultado("A* (informada, con heurística geográfica)", resultado_a_estrella)

    print("\n" + "-" * 60)
    if resultado_dijkstra is None:
        print("No se encontró ninguna ruta posible entre esas dos estaciones.")
    else:
        _, costo_dijkstra, _ = resultado_dijkstra
        _, costo_bfs, _ = resultado_bfs
        print("RECOMENDACIÓN: Dijkstra y A* garantizan el menor tiempo total de viaje")
        print(f"({costo_dijkstra} min). BFS solo garantiza el menor número de estaciones,")
        if resultado_bfs is not None and costo_bfs > costo_dijkstra:
            print(f"y en este caso su ruta es más lenta ({costo_bfs} min) aunque tenga menos saltos.")
        else:
            print("y en este caso coincide con la ruta más rápida.")
    print("-" * 60)


def main():
    grafo = construir_grafo()
    coordenadas = obtener_coordenadas()
    estaciones = listar_estaciones(grafo)

    print("=" * 60)
    print(" SISTEMA EXPERTO DE RUTAS - TRANSMILENIO (BOGOTÁ)")
    print(" Búsqueda y sistemas basados en reglas - Actividad 2")
    print("=" * 60)

    # Modo con argumentos de línea de comandos: python main.py "Origen" "Destino"
    if len(sys.argv) == 3:
        origen, destino = sys.argv[1], sys.argv[2]
        if origen not in estaciones or destino not in estaciones:
            print("Una de las estaciones indicadas por argumento no existe en el grafo.")
            mostrar_menu_estaciones(estaciones)
            sys.exit(1)
        calcular_y_mostrar_rutas(grafo, coordenadas, origen, destino)
        return

    # Modo interactivo
    mostrar_menu_estaciones(estaciones)
    origen = pedir_estacion("\nEstación de ORIGEN (punto A): ", estaciones)
    destino = pedir_estacion("Estación de DESTINO (punto B): ", estaciones)
    calcular_y_mostrar_rutas(grafo, coordenadas, origen, destino)


if __name__ == "__main__":
    main()
