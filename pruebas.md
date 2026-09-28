# Documento de Pruebas — Sistema Experto de Rutas TransMilenio

**Actividad 2 — Búsqueda y sistemas basados en reglas**

Este documento recoge la ejecución real del programa (`python main.py "Origen" "Destino"`)
para tres pares origen-destino distintos, junto con la tabla comparativa de
resultados. Todas las salidas de consola mostradas abajo son copia literal de
lo producido por el programa (no están inventadas ni editadas a mano).

---

## Prueba 1: Portal Norte → Portal Sur

**Comando ejecutado:**
```
python main.py "Portal Norte" "Portal Sur"
```

**Salida de consola:**
```
============================================================
 SISTEMA EXPERTO DE RUTAS - TRANSMILENIO (BOGOTÁ)
 Búsqueda y sistemas basados en reglas - Actividad 2
============================================================

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

------------------------------------------------------------
RECOMENDACIÓN: Dijkstra y A* garantizan el menor tiempo total de viaje
(58 min). BFS solo garantiza el menor número de estaciones,
y en este caso su ruta es más lenta (63 min) aunque tenga menos saltos.
------------------------------------------------------------
```

**Tabla comparativa:**

| Algoritmo | Ruta | N° estaciones | Tiempo total | Nodos explorados |
|---|---|---|---|---|
| BFS | Portal Norte → Toberín → Mazurén → CAN → Av. Rojas → Ricaurte → Comuneros → Portal Sur | 8 | 63 min | 18 |
| Dijkstra | Portal Norte → Toberín → Mazurén → Calle 100 → Héroes → CAN → Av. Rojas → Ricaurte → Comuneros → Portal Sur | 10 | **58 min** | 20 |
| A* | Portal Norte → Toberín → Mazurén → Calle 100 → Héroes → CAN → Av. Rojas → Ricaurte → Comuneros → Portal Sur | 10 | **58 min** | **17** |

**Análisis:** esta es la prueba más importante del proyecto porque muestra un
caso donde **BFS y Dijkstra/A* discrepan**. La base de conocimiento incluye
una ruta "alimentadora" directa `Mazurén → CAN` (25 min, un solo tramo que se
salta varias estaciones intermedias). BFS la elige porque tiene menos saltos
(8 estaciones), pero es 5 minutos más lenta en total. Dijkstra y A* ignoran el
número de saltos y encuentran la ruta genuinamente más rápida (58 min), pese a
tener 10 estaciones. Además, A* llega al mismo resultado óptimo que Dijkstra
explorando **menos nodos** (17 contra 20), gracias a la heurística geográfica
que dirige la búsqueda hacia el destino.

---

## Prueba 2: Portal El Dorado (Aeropuerto) → Av. Jiménez

**Comando ejecutado:**
```
python main.py "Portal El Dorado" "Av. Jiménez"
```

**Salida de consola:**
```
============================================================
 SISTEMA EXPERTO DE RUTAS - TRANSMILENIO (BOGOTÁ)
 Búsqueda y sistemas basados en reglas - Actividad 2
============================================================

============================================================
RUTAS DE Portal El Dorado A Av. Jiménez
============================================================

🔹 BFS (no informada, menor n° de saltos)
   Ruta:              Portal El Dorado -> Modelia -> Salitre El Greco -> CAN -> Héroes -> Calle 72 -> Av. Jiménez
   N° de estaciones:   7
   Tiempo total:       33 min
   Nodos explorados:   12

🔹 Dijkstra (no informada, costo uniforme)
   Ruta:              Portal El Dorado -> Modelia -> Salitre El Greco -> CAN -> Héroes -> Calle 72 -> Av. Jiménez
   N° de estaciones:   7
   Tiempo total:       33 min
   Nodos explorados:   10

🔹 A* (informada, con heurística geográfica)
   Ruta:              Portal El Dorado -> Modelia -> Salitre El Greco -> CAN -> Héroes -> Calle 72 -> Av. Jiménez
   N° de estaciones:   7
   Tiempo total:       33 min
   Nodos explorados:   10

------------------------------------------------------------
RECOMENDACIÓN: Dijkstra y A* garantizan el menor tiempo total de viaje
(33 min). BFS solo garantiza el menor número de estaciones,
y en este caso coincide con la ruta más rápida.
------------------------------------------------------------
```

**Tabla comparativa:**

| Algoritmo | Ruta | N° estaciones | Tiempo total | Nodos explorados |
|---|---|---|---|---|
| BFS | Portal El Dorado → Modelia → Salitre El Greco → CAN → Héroes → Calle 72 → Av. Jiménez | 7 | 33 min | 12 |
| Dijkstra | (misma ruta) | 7 | 33 min | 10 |
| A* | (misma ruta) | 7 | 33 min | **10** |

**Análisis:** en este caso los tres algoritmos coinciden en la misma ruta,
porque el camino con menos saltos también resulta ser el más rápido (no hay
ningún atajo "lento" en esta zona del grafo). Esto demuestra que BFS y
Dijkstra/A* no siempre difieren — solo lo hacen cuando existen tramos con
pesos desproporcionados, como en la Prueba 1. Se observa además que BFS, al
no usar cola de prioridad, explora más nodos (12) que Dijkstra y A* (10) para
llegar al mismo resultado.

---

## Prueba 3: Las Aguas → Portal Américas

**Comando ejecutado:**
```
python main.py "Las Aguas" "Portal Américas"
```

**Salida de consola:**
```
============================================================
 SISTEMA EXPERTO DE RUTAS - TRANSMILENIO (BOGOTÁ)
 Búsqueda y sistemas basados en reglas - Actividad 2
============================================================

============================================================
RUTAS DE Las Aguas A Portal Américas
============================================================

🔹 BFS (no informada, menor n° de saltos)
   Ruta:              Las Aguas -> Museo del Oro -> Av. Jiménez -> Tercer Milenio -> Ricaurte -> Banderas -> Portal Américas
   N° de estaciones:   7
   Tiempo total:       34 min
   Nodos explorados:   16

🔹 Dijkstra (no informada, costo uniforme)
   Ruta:              Las Aguas -> Museo del Oro -> Av. Jiménez -> Tercer Milenio -> Ricaurte -> Banderas -> Portal Américas
   N° de estaciones:   7
   Tiempo total:       34 min
   Nodos explorados:   18

🔹 A* (informada, con heurística geográfica)
   Ruta:              Las Aguas -> Museo del Oro -> Av. Jiménez -> Tercer Milenio -> Ricaurte -> Banderas -> Portal Américas
   N° de estaciones:   7
   Tiempo total:       34 min
   Nodos explorados:   12

------------------------------------------------------------
RECOMENDACIÓN: Dijkstra y A* garantizan el menor tiempo total de viaje
(34 min). BFS solo garantiza el menor número de estaciones,
y en este caso coincide con la ruta más rápida.
------------------------------------------------------------
```

**Tabla comparativa:**

| Algoritmo | Ruta | N° estaciones | Tiempo total | Nodos explorados |
|---|---|---|---|---|
| BFS | Las Aguas → Museo del Oro → Av. Jiménez → Tercer Milenio → Ricaurte → Banderas → Portal Américas | 7 | 34 min | 16 |
| Dijkstra | (misma ruta) | 7 | 34 min | 18 |
| A* | (misma ruta) | 7 | 34 min | **12** |

**Análisis:** de nuevo los tres algoritmos coinciden en la ruta óptima. Aquí
se ve con más claridad la ventaja de la búsqueda informada: A* llega al mismo
resultado que Dijkstra explorando solo 12 nodos frente a 18, porque la
heurística geográfica le permite descartar antes las direcciones que se
alejan de "Portal Américas".

---

## Prueba adicional: validación de entradas inválidas (modo interactivo)

Para verificar el manejo de errores del sistema, se ejecutó el programa en
modo interactivo ingresando primero una estación inexistente:

```
Estación de ORIGEN (punto A): Estacion Inventada
  ⚠️  "Estacion Inventada" no está en la lista de estaciones. Escríbela tal cual aparece arriba.

Estación de ORIGEN (punto A): Portal Norte
Estación de DESTINO (punto B): Calle 100
```

El programa rechazó la entrada inválida y volvió a pedir el dato, sin
detenerse ni lanzar errores, y luego calculó correctamente la ruta
`Portal Norte → Toberín → Mazurén → Calle 100` (19 min, 4 estaciones) con los
tres algoritmos.

---

## Resumen general

| Prueba | ¿BFS coincide con Dijkstra/A*? | Motivo |
|---|---|---|
| Portal Norte → Portal Sur | **No** | Existe una ruta alimentadora con menos paradas pero más lenta (25 min en un solo tramo) |
| Portal El Dorado → Av. Jiménez | Sí | No hay tramos con costo desproporcionado en ese trayecto |
| Las Aguas → Portal Américas | Sí | Ídem |

**Conclusión de las pruebas:** el sistema calcula correctamente rutas usando
tres estrategias de búsqueda distintas sobre la misma base de conocimiento.
Dijkstra y A* siempre coinciden en el costo óptimo (como es de esperar
teóricamente, dado que la heurística usada es admisible), mientras que A*
consistentemente explora menos o igual número de nodos que Dijkstra gracias a
la información adicional de la heurística. BFS, al ignorar los pesos, puede
producir una ruta subóptima en tiempo cuando existen tramos con costos no
uniformes, como se demuestra en la Prueba 1.
