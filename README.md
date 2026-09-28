# Sistema Experto de Rutas — TransMilenio (Bogotá)

Proyecto para la **Actividad 2 — "Búsqueda y sistemas basados en reglas"** del
curso de Inteligencia Artificial.

## Descripción

Sistema inteligente en Python que representa el sistema de transporte masivo
**TransMilenio (Bogotá)** como una **base de conocimiento escrita en reglas
lógicas** (hechos del tipo `conecta(EstaciónA, EstaciónB, tiempo)`), y que a
partir de ella:

1. Construye un **grafo navegable** mediante un motor de inferencia que
   dispara la regla de simetría (el transporte es bidireccional).
2. Calcula la mejor ruta entre dos estaciones usando **tres algoritmos de
   búsqueda** distintos, para poder comparar sus resultados:
   - **BFS** — búsqueda no informada, minimiza el número de estaciones.
   - **Dijkstra** — búsqueda no informada de costo uniforme, minimiza el
     tiempo total de viaje.
   - **A\*** — búsqueda informada (usa una heurística de distancia geográfica
     entre estaciones), llega al mismo resultado óptimo que Dijkstra
     explorando normalmente menos nodos.

> **Nota:** las estaciones incluidas son reales de TransMilenio, pero las
> coordenadas y los tiempos de viaje entre estaciones son **aproximados**,
> estimados con fines exclusivamente académicos. No son datos oficiales de
> TransMilenio S.A.

## Estructura del proyecto

```
proyecto-transmilenio-ia/
├── base_conocimiento.py   # Hechos: coordenadas y conexiones (reglas lógicas)
├── motor_inferencia.py    # Construye el grafo a partir de los hechos (regla de simetría)
├── busqueda.py            # BFS, Dijkstra y A* (con función de heurística)
├── main.py                # Interfaz de consola
├── pruebas.md             # Documento de pruebas realizadas
├── guion_video.md         # Guion del video explicativo
└── README.md
```

## Requisitos

- Python 3.8 o superior.
- No requiere librerías externas (solo módulos estándar: `heapq`, `math`,
  `collections`, `sys`).

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

El programa mostrará el listado de estaciones disponibles y pedirá una
estación de **origen** y una de **destino**. Luego mostrará las tres rutas
calculadas (BFS, Dijkstra y A*) con su tiempo total, número de estaciones y
número de nodos explorados por cada algoritmo.

También se puede ejecutar en modo no interactivo, pasando origen y destino
como argumentos (útil para pruebas rápidas):

```bash
python main.py "Portal Norte" "Portal Sur"
```

### Ejemplo de uso

```
$ python main.py "Portal Norte" "Portal Sur"

============================================================
RUTAS DE Portal Norte A Portal Sur
============================================================

🔹 BFS (no informada, menor n° de saltos)
   Ruta:              Portal Norte -> Toberín -> Mazurén -> CAN -> Av. Rojas -> Ricaurte -> Comuneros -> Portal Sur
   N° de estaciones:   8
   Tiempo total:       63 min
   Nodos explorados:   18

🔹 Dijkstra (no informada, costo uniforme)
   Ruta:              Portal Norte -> Toberín -> Mazurén -> Calle 100 -> Héroes -> CAN -> Av. Rojas -> Ricaurte -> Comuneros -> Portal Sur
   N° de estaciones:   10
   Tiempo total:       58 min
   Nodos explorados:   20

🔹 A* (informada, con heurística geográfica)
   Ruta:              Portal Norte -> Toberín -> Mazurén -> Calle 100 -> Héroes -> CAN -> Av. Rojas -> Ricaurte -> Comuneros -> Portal Sur
   N° de estaciones:   10
   Tiempo total:       58 min
   Nodos explorados:   17
```

Este ejemplo es intencional: existe una "ruta alimentadora" directa
(`Mazurén -> CAN`, 25 min) con menos paradas pero más lenta que ir por el
troncal. BFS la elige porque solo minimiza saltos; Dijkstra y A* la descartan
porque sí consideran el tiempo, y encuentran la ruta realmente más rápida
aunque tenga más estaciones. Más ejemplos y su análisis en
[`pruebas.md`](./pruebas.md).

## Conceptos de IA aplicados

- **Lógica y representación del conocimiento** (Cap. 2): los hechos
  `conecta(A, B, t)` como proposiciones de lógica de primer orden.
- **Sistemas basados en reglas** (Cap. 3): la regla de simetría, el proceso
  de equiparación (pattern matching) y disparo de reglas en
  `motor_inferencia.py`.
- **Búsquedas heurísticas** (Cap. 9): búsqueda no informada (BFS, Dijkstra) e
  informada (A*) con una heurística admisible.

*(Benítez, R. (2014). Inteligencia artificial avanzada. Barcelona: Editorial UOC.)*
