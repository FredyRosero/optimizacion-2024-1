"""
## Segundo Punto (40 Puntos)

Dado un inventario de rollos de ancho W metros, determine cuánto de estos rollos cortar de tal manera que \(b_i\), \(i = 1, ..., m\) unidades de ancho \(w_i\) sean producidas, minimizando el total en centímetros cuadrados de desperdicio de rollos. Deben satisfacerse los requerimientos presentados en los datos para los m diferentes tamaños dados.

### Datos del segundo punto
El tamaño del rollo maestro es 2500 y se consideran desperdicios los rollos cortados y no vendidos. Las longitudes y demandas de los rollos a cortar son:

Piece longitud: 701, Demand: 27

| Pieza | Longitud (mm) | Demanda (unidades) |
| ----- | ------------- | ------------------ |
| 1     | 692           | 14                 |
| 2     | 627           | 25                 |
| 3     | 491           | 50                 |
| 4     | 253           | 38                 |
| 5     | 271           | 19                 |
| 6     | 628           | 32                 |
| 7     | 533           | 50                 |
| 8     | 708           | 18                 |
| 9     | 520           | 12                 |
| 10    | 580           | 16                 |
| 11    | 630           | 39                 |
| 12    | 406           | 39                 |
| 13    | 587           | 36                 |
| 14    | 346           | 40                 |
| 15    | 632           | 45                 |
| 16    | 310           | 49                 |
| 17    | 617           | 30                 |
| 18    | 729           | 11                 |
| 19    | 723           | 27                 |
| 20    | 701           | 27                 |

### a) (15 puntos)
Formular el modelo de Programación Lineal Entera Mixta (PLEM) definiendo los patrones de cortes posibles.

### b) (25 puntos)
Encuentre la solución al modelo anterior con los datos provistos a través del algoritmo de Branch and Bound usando Gurobi. Presentar el árbol de decisión.
"""
import itertools
import gurobipy as gp
from gurobipy import GRB
import matplotlib.pyplot as plt
import networkx as nx

# Generar patrones posibles de corte
def generar_patrones(piezas, W):
    m = len(piezas)
    patrones = []
    # Generar combinaciones de piezas que no excedan el ancho del rollo
    for i in range(1, m + 1):
        for combinacion in itertools.combinations_with_replacement(range(m), i):
            longitud_total = sum(piezas[idx]["longitud"] for idx in combinacion)
            if longitud_total <= W:
                patron = [0] * m
                for idx in combinacion:
                    patron[idx] += 1
                patrones.append(patron)    
    return patrones

# Datos de las piezas
piezas = [
    {"longitud": 692, "demanda": 14},
    {"longitud": 627, "demanda": 25},
    {"longitud": 491, "demanda": 50},
    {"longitud": 253, "demanda": 38},
    {"longitud": 271, "demanda": 19},
    {"longitud": 628, "demanda": 32},
    {"longitud": 533, "demanda": 50},
    {"longitud": 708, "demanda": 18},
    {"longitud": 520, "demanda": 12},
    {"longitud": 580, "demanda": 16},
    {"longitud": 630, "demanda": 39},
    {"longitud": 406, "demanda": 39},
    {"longitud": 587, "demanda": 36},
    {"longitud": 346, "demanda": 40},
    {"longitud": 632, "demanda": 45},
    {"longitud": 310, "demanda": 49},
    {"longitud": 617, "demanda": 30},
    {"longitud": 729, "demanda": 11},
    {"longitud": 723, "demanda": 27},
    {"longitud": 701, "demanda": 27}
]

# Ancho del rollo maestro
W = 2500

import math

# Ordenar las piezas de mayor a menor longitud
piezas.sort(key=lambda x: -x['longitud'])

# Heurística inicial: First Fit Decreasing (FFD)
def generar_patrones_heuristica(piezas, W):
    patrones = []  # Lista para almacenar los patrones generados
    demanda_restante = [pieza['demanda'] for pieza in piezas]

    while sum(demanda_restante) > 0:
        espacio_disponible = W  # Inicializar el espacio disponible en el rollo
        patron_actual = [0] * len(piezas)  # Cantidades de cada pieza en este patrón

        for i, pieza in enumerate(piezas):
            while demanda_restante[i] > 0 and pieza['longitud'] <= espacio_disponible:
                # Si la pieza cabe en el espacio disponible, añadirla al patrón
                patron_actual[i] += 1
                espacio_disponible -= pieza['longitud']
                demanda_restante[i] -= 1

        patrones.append(patron_actual)

    return patrones

# Función para calcular el desperdicio de un patrón
def calcular_desperdicio(patron, piezas, W):
    total_corte = sum(patron[i] * piezas[i]['longitud'] for i in range(len(piezas)))
    return W - total_corte

# Función de generación de columnas: buscar patrones más eficientes
def generar_columnas(piezas, W):
    # Resolver un problema de mochila para generar nuevos patrones
    # Usamos un enfoque greedy para crear patrones con menor desperdicio
    patrones = []
    espacio_disponible = W
    patron = [0] * len(piezas)

    for i, pieza in enumerate(piezas):
        while pieza['longitud'] <= espacio_disponible:
            patron[i] += 1
            espacio_disponible -= pieza['longitud']

    patrones.append(patron)
    return patrones

# Generar patrones iniciales usando la heurística
patrones_iniciales = generar_patrones_heuristica(piezas, W)

# Mostrar patrones iniciales
print("Patrones iniciales generados:")
for i, patron in enumerate(patrones_iniciales):
    desperdicio = calcular_desperdicio(patron, piezas, W)
    print(f"Patrón {i + 1}: {patron} con desperdicio {desperdicio}")

# Generar nuevos patrones usando generación de columnas (problema de mochila)
nuevos_patrones = generar_columnas(piezas, W)

# Mostrar los nuevos patrones generados
print("\nNuevos patrones generados mediante generación de columnas:")
for i, patron in enumerate(nuevos_patrones):
    desperdicio = calcular_desperdicio(patron, piezas, W)
    print(f"Nuevo Patrón {i + 1}: {patron} con desperdicio {desperdicio}")

# Combinar patrones iniciales y nuevos patrones en un solo conjunto
def combinar_patrones(patrones_iniciales, nuevos_patrones):
    # Usamos un set para evitar duplicados. Convertimos las listas a tuplas.
    patrones_unicos = set()

    # Agregar los patrones iniciales como tuplas
    for patron in patrones_iniciales:
        patrones_unicos.add(tuple(patron))

    # Agregar los nuevos patrones generados como tuplas
    for patron in nuevos_patrones:
        patrones_unicos.add(tuple(patron))

    # Convertir de nuevo los patrones a listas para consistencia
    patrones_combinados = [list(patron) for patron in patrones_unicos]

    return patrones_combinados

patrones = combinar_patrones(patrones_iniciales, nuevos_patrones)
# Generar patrones de corte
#patrones = generar_patrones(piezas, W)
# Imprimir los primero 50 patrones generados
def print_pattern(array):
    return "\t".join([f'{p}' for p in array])
n = len(patrones)  # Cantidad de patrones generados
m = len(piezas)
print(f"\nSe generaron {n} patrones de corte posibles.")

# Preguntar si continuar con la ejecución
respuesta = input("¿Desea continuar con la ejecución? (s/n): ")
if respuesta.lower() != "s":
    print("Ejecución cancelada.")
    exit()

# Definir el callback para capturar la información de las iteraciones
class IterationLogger:
    def __init__(self):
        self.iterations_data = []

    def callback(self, model, where):
        if where == GRB.Callback.MIP: # Si es un evento MIP, MIP es Mixed Integer Programming
            # Obtener información de la iteración
            node_count = model.cbGet(GRB.Callback.MIP_NODCNT)
            obj_bound = model.cbGet(GRB.Callback.MIP_OBJBND)
            obj_value = model.cbGet(GRB.Callback.MIP_OBJBST)
            # Evitar el acceso a MIP_GAP si no hay un valor óptimo aún
            if obj_value < GRB.INFINITY:
                gap = (obj_value - obj_bound) / obj_value
            else:
                gap = None       
            # Guardar la información de la iteración
            self.iterations_data.append({
                'node_count': node_count,
                'obj_bound': obj_bound,
                'obj_value': obj_value,
                'gap': gap,
            })
        
        elif where == GRB.Callback.MIPNODE: # Si es un evento MIPNODE, MIPNODE es Mixed Integer Programming Node
            # Obtener las variables fraccionarias candidatas para la ramificación
            node_solution = model.cbGetNodeRel(model.getVars())
            fractional_vars = [(v.varName, node_solution[i]) for i, v in enumerate(model.getVars()) if node_solution[i] > 1e-5 and node_solution[i] < 1 - 1e-5]
            integer_vars = [(v.varName, node_solution[i]) for i, v in enumerate(model.getVars()) if node_solution[i] < 1e-5 or node_solution[i] > 1 - 1e-5]
            
            # Guardar las variables fraccionarias candidatas
            self.iterations_data[-1]['fractional_vars'] = fractional_vars  

            self.iterations_data[-1]['integer_vars'] = integer_vars                

# Crear el logger de iteraciones
iteration_logger = IterationLogger()

# Crear el modelo en Gurobi
model = gp.Model('Corte_min_desperdicio')
model.setParam('OutputFlag', 1)  # Mostrar todas las iteraciones del solver
#model.setParam('MIPGap', 1e-9)  # Esto fuerza una mayor precisión en la solución
model.setParam('Heuristics', 0)  # Esto desactiva las heurísticas
model.setParam('Cuts', 0)  # Esto minimiza el uso de cortes
#model.setParam('NodeLimit', 10)  # Esto obliga al solver a explorar más nodos
#model.setParam('IntFeasTol', 1e-9)  # Reduces la tolerancia para soluciones fraccionarias

# Variables de decisión: 
# x_j: Número de veces que se usa el patrón j
x = model.addVars(n, vtype=GRB.INTEGER, name="x")

# s_i: Desperdicio de piezas (piezas cortadas en exceso)
s = model.addVars(m, vtype=GRB.INTEGER, name="s")

# Función objetivo: minimizar el desperdicio
desperdicio_material = gp.quicksum(
    (W - sum(piezas[i]["longitud"] * patrones[j][i] for i in range(m))) * x[j]
    for j in range(n)
)

# Desperdicio de piezas excedentes
desperdicio_piezas = gp.quicksum(s[i] for i in range(m))

# Establecer el objetivo de minimizar el desperdicio total
model.setObjective(desperdicio_material + desperdicio_piezas, GRB.MINIMIZE)

# Restricciones: 
# Satisfacer la demanda de cada pieza, permitiendo desperdicio de piezas
for i in range(m):
    model.addConstr(
        gp.quicksum(patrones[j][i] * x[j] for j in range(n)) - s[i] >= piezas[i]["demanda"],
        name=f"demanda_{i}"
    )

# Optimizar el modelo
model.optimize(callback=iteration_logger.callback)


# Mostrar resultados
if model.status == GRB.OPTIMAL:
    print(f"\nSolución óptima encontrada:\n")
    print("Patrón\t", end="")
    print("\t".join([f'{i+1}' for i in range(m)]), end="")
    print("\tDesperdicio")
    # Mostrar los patrones utilizados y el desperdicio en cada uno
    for j in range(n):
        if x[j].x > 0.5:
            desperdicio = W - sum(patrones[j][i] * piezas[i]["longitud"] for i in range(m))           
            print(f"#{j+1}\t{print_pattern(patrones[j])}\tutilizado {x[j].x:.0f} veces. Desperdicio: {desperdicio * x[j].x:.0f} und. ln.")
    # Total por pieza
    pieza_patron = []
    print("Cant.\t", end="")
    for i in range(m):
        pieza_patron.append(sum(patrones[j][i] * x[j].x for j in range(n)))
    print("\t".join([f'{p:.0f}' for p in pieza_patron]), end="")
    # Demanda
    print("\nDemanda\t", end="")
    for i in range(m):
        print(f'{piezas[i]["demanda"]}', end="\t")
    # Desperdicio total
    print(f"\nDesperdicio total: {model.objVal:.0f} unidades de longitud") 
else:
    print("No se encontró una solución óptima.")

# # Árbol de decisión:
# Mostrar información de las iteraciones
print()
if model.status == GRB.OPTIMAL:
    print
    for iteration in iteration_logger.iterations_data:        
        gap_str = f"{iteration['gap']:.4f}" if iteration['gap'] is not None else "N/A"
        print(f"Nodo: {iteration['node_count']}, Mejor límite: {iteration['obj_bound']}, "
              f"Mejor valor: {iteration['obj_value']}, Gap: {gap_str}")
        if 'fractional_vars' in iteration:
            print(f"\tVariables fraccionarias (candidatas): {iteration['fractional_vars']}")
        if 'integer_vars' in iteration:
            print(f"\tVariables enteras: {iteration['integer_vars']}")
    print(f"\nDetalles del árbol de decisión:")
    print(f"Nodos explorados: {model.nodecount}")
    print(f"Valor óptimo encontrado: {model.objVal:.2f}")
    print(f"Tiempo total de ejecución: {model.runtime:.2f} segundos")

else:
    print("No se encontró una solución óptima.")