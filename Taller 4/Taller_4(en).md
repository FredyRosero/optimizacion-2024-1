# Workshop 4 Optimization
**Department of Systems Engineering and Industrial Engineering**

**National University of Colombia**

XXX = 270, YYY = 114
---

## First Problem (40 Points)

A company produces a certain type of accessories. These accessories are produced in one of the production facilities, then sent to one of the distribution centers, and finally shipped to retail sellers. Each retail seller has a demand forecast, each production facility has a minimum and maximum number of accessories it can manufacture during this period, and each distribution center has a maximum capacity of accessories it can distribute. The transportation cost per unit is only valid if a minimum number of accessory units are transported either from the factories to the distribution centers or from the latter to the retail sellers, meaning that any shipment from the production facilities to the distribution centers must be greater than N units, and any shipment from the distribution centers to the retail sellers must be greater than M units.

In addition to the first problem, it must be ensured that each factory produces at least 80% of its maximum supply capacity, and the minimum quantity to transport between any two nodes must be greater than the total minimum demand of a demand center (city).

### Data for the First Problem

| Factories     | Capacity |
| ------------- | -------- |
| Bogotá        | 5502     |
| Medellín      | 5909     |
| Pereira       | 1497     |
| Cali          | 5862     |
| Barranquilla  | 5161     |
| Bucaramanga   | 1254     |

The warehouse locations are:
Bogotá, Medellín, Pereira, Cali, Barranquilla, Bucaramanga, Tenjo, Itagüí, Palmira, Manizales, Santa Marta, Popayán, Montería

#### Location and demand for each point...

City: Bogotá
Point 1: Coordinates: (4.568565647912089, -74.00270535750907), Demand: 333 units  
Point 2: Coordinates: (4.699675267272541, -74.07013834007228), Demand: 275 units  
Point 3: Coordinates: (4.605959459359155, -73.90746369562126), Demand: 234 units  
Point 4: Coordinates: (4.659937063543658, -74.19389215200056), Demand: 184 units  
Point 5: Coordinates: (4.738392236201863, -73.96694806082473), Demand: 824 units  
Point 6: Coordinates: (4.745245132662214, -74.05316646428159), Demand: 385 units  
Point 7: Coordinates: (4.641713414509857, -74.12465194138828), Demand: 252 units  
Point 8: Coordinates: (4.570809571300359, -73.92035359354273), Demand: 569 units  
Point 9: Coordinates: (4.552916274446604, -74.10994941504137), Demand: 437 units  
Point 10: Coordinates: (4.62600534010459, -74.05028318114154), Demand: 830 units  
Point 11: Coordinates: (4.618542022125971, -74.13280565976245), Demand: 560 units  
Point 12: Coordinates: (4.612961297506587, -74.05915339775301), Demand: 354 units  
Point 13: Coordinates: (4.668352608761532, -73.90056673165957), Demand: 316 units  
Point 14: Coordinates: (4.79212846131582, -74.19311557774746), Demand: 695 units  
Point 15: Coordinates: (4.768387148819588, -73.91357516563635), Demand: 273 units  
Point 16: Coordinates: (4.676193393539264, -74.03070168231001), Demand: 524 units  
Point 17: Coordinates: (4.613825560227022, -74.14791329582887), Demand: 306 units  
Point 18: Coordinates: (4.620253419081813, -74.03801851849347), Demand: 211 units  
Point 19: Coordinates: (4.631651143383878, -74.08450952246882), Demand: 349 units  
Point 20: Coordinates: (4.584826182628852, -74.00492640453885), Demand: 94 units  
Point 21: Coordinates: (4.847285437118325, -73.98975277454807), Demand: 347 units  
Total Demand 8352

City: Medellín  
Point 1: Coordinates: (6.24678283335728, -75.55975056917285), Demand: 76 units  
... [similar structure for other cities and points] ...

Total Demand: 2572 (Medellín), 480 (Pereira), 2200 (Cali), 1380 (Barranquilla), etc.

### a) (25 points)
Formulate the Mixed Integer Linear Programming (MILP) model that minimizes the total transportation cost.

### b) (15 points)
Find the solution to the previous model with the provided data using Gurobi.

### NotenookLM AI reponse

This problem presents a classic operations research challenge focusing on **optimising the supply chain** of a company that produces accessories. While the provided context sets up the scenario effectively, the sources primarily contain examples and problem formulations related to production planning, inventory management, and transportation problems. They **do not offer a direct solution** to the specific scenario outlined in the query.

To effectively address this supply chain optimisation problem, one would typically need to formulate a mixed-integer linear programming (MILP) model. 

Let's break down why the sources fall short and how an MILP approach could be applied:

* **Missing Demand Data:** The query mentions demand forecasts for retail sellers but doesn't provide the actual data. Without this crucial information, it's impossible to model the objective function, which would likely be minimising total costs or maximising profits, taking into account production, transportation, and potentially storage costs.
* **Unclear Values for N and M:** The query introduces minimum transportation quantities (N for factory to distribution centre and M for distribution centre to retail seller) but doesn't specify their values. These are critical for accurately modelling transportation costs and constraints.
* **Source Relevance:** The sources provided mainly illustrate different production planning and scheduling scenarios. For instance, examples involve determining optimal production quantities for different products given resource constraints (), managing inventory costs (), or handling transportation costs between various points in a supply chain (). These examples, while useful for understanding the broader concepts, don't directly translate to a solution for the query's scenario with its specific requirements.

**Applying an MILP Approach:**

An MILP model would be suitable for this scenario because it can handle:

1. **Minimising Transportation Costs**: By incorporating variables for shipment quantities between each factory-warehouse-retailer combination and using the given transportation costs (with the minimum quantity considerations), the model can determine the most cost-effective transportation plan.
2. **Production Constraints**: Each factory's minimum (80% of maximum capacity) and maximum production limits can be represented as constraints in the model.
3. **Warehouse Capacity Limits**:  Constraints can be added to ensure that the inflow of accessories to each distribution centre doesn't exceed its maximum capacity.
4. **Demand Fulfilment**:  The model ensures all retail seller demands are met by enforcing constraints on the total inflow to each retailer.

**Key Variables and Constraints:**

* **Decision Variables**: Quantities of accessories shipped between each node (factory, distribution centre, retailer).
* **Objective Function**: Minimise total cost (production + transportation), potentially including any relevant storage costs.
* **Constraints**:
    * Production capacity constraints for each factory.
    * Distribution centre capacity constraints.
    * Minimum shipment quantity constraints.
    * Demand fulfilment constraints for each retailer.

**Additional Notes:**

* The model may need to incorporate binary variables to handle the "all or nothing" aspect of transportation costs when the minimum quantity constraint comes into play.
* Software like LINGO or solvers within platforms like Excel can be used to solve the formulated MILP and arrive at an optimal solution.

In summary, formulating a well-defined MILP model, incorporating all the necessary data and constraints, is essential to solving the company's supply chain optimisation problem as described in the query. 

### Solution

### **a) Formulación del Modelo de Programación Lineal Entera Mixta (PLEM)**

#### **Conjuntos:**

* $I$: Conjunto de fábricas ($i = 1, 2, ..., 6$)
* $J$: Conjunto de centros de distribución ($j = 1, 2, ..., 13$)
* $K$: Conjunto de ciudades/puntos de demanda ($k = 1, 2, ..., 12$)

#### **Parámetros:**

* $\text{Capacidad}_i$: Capacidad máxima de producción de la fábrica $i$
* $\text{Demanda}_k$: Demanda total de la ciudad $k$ (suma de las demandas de sus puntos)
* $\text{Dist}_{ij}$: Distancia entre fábrica $i$ y centro de distribución $j$
* $\text{Dist}_{jk}$: Distancia entre centro de distribución $j$ y ciudad $k$
* $\text{PesoUnidad} = 2.114$ kg
* $\text{CostoKgKm} = 1270$ pesos/kg-km
* $\text{CostoIntraCiudad} = 2270$ pesos/unidad
* $N = 270$ unidades
* $M = 114$ unidades

#### **Variables de Decisión:**

* $X_{ij} \geq 0$: Unidades enviadas desde fábrica $i$ al centro de distribución $j$
* $Y_{jk} \geq 0$: Unidades enviadas desde centro de distribución $j$ a la ciudad $k$
* $Z_{ij} \in \{0,1\}$: 1 si se realiza envío desde $i$ a $j$, 0 en caso contrario
* $W_{jk} \in \{0,1\}$: 1 si se realiza envío desde $j$ a $k$, 0 en caso contrario

#### **Función Objetivo:**

Minimizar el costo total de transporte:

$$\begin{align*}  
\text{Minimizar} \quad & \sum_{i \in I} \sum_{j \in J} \left( X_{ij} \times \text{Dist}_{ij} \times \text{PesoUnidad} \times \text{CostoKgKm} \right) \\  
& + \sum_{j \in J} \sum_{k \in K} \left( Y_{jk} \times \text{Dist}_{jk} \times \text{PesoUnidad} \times \text{CostoKgKm} \right) \\  
& + \sum_{k \in K} \left( \text{Demanda}_k \times \text{CostoIntraCiudad} \right)  
\end{align*}$$

#### **Restricciones:**

1. **Capacidad de Producción de las Fábricas:**
    
    $$0.8 \times \text{Capacidad}_i \leq \sum_{j \in J} X_{ij} \leq \text{Capacidad}_i \quad \forall i \in I$$
2. **Balance en los Centros de Distribución:**
    
    $$\sum_{i \in I} X_{ij} = \sum_{k \in K} Y_{jk} \quad \forall j \in J$$
3. **Satisfacción de la Demanda:**
    
    $$\sum_{j \in J} Y_{jk} = \text{Demanda}_k \quad \forall k \in K$$
4. **Envíos Mínimos desde Fábricas a Centros de Distribución:**
    
    $$X_{ij} \geq N \times Z_{ij} \quad \forall i \in I, \forall j \in J$$
5. **Envíos Mínimos desde Centros de Distribución a Ciudades:**
    
    $$Y_{jk} \geq M \times W_{jk} \quad \forall j \in J, \forall k \in K$$
6. **Limitaciones por Variables Binarias:**
    
    * Si no hay envío, las variables continuas deben ser cero.
        
        $$
        X_{ij} \leq \left( \text{Capacidad}_i \times Z_{ij} \right) \quad \forall i \in I, \forall j \in J
        $$ 
        $$Y_{jk} \leq \left( \text{Demanda}_k \times W_{jk} \right) \quad \forall j \in J, \forall k \in K$$
7. **Variables Binarias:**
    
    $$Z_{ij} \in \{0,1\} \quad \forall i \in I, \forall j \in J$$ 
    $$W_{jk} \in \{0,1\} \quad \forall j \in J, \forall k \in K$$

#### **Consideraciones Adicionales:**

* **Distancias ($\text{Dist}_{ij}$ y $\text{Dist}_{jk}$)**: Calcula las distancias geográficas utilizando las coordenadas proporcionadas (promedio de los puntos de demanda en cada ciudad). La fórmula de Haversine es adecuada para calcular distancias entre coordenadas geográficas.

#### **b) Resolución del Modelo con Gurobi**

**Pasos para Implementar el Modelo:**

1. **Preparación de Datos:**
    
    * **Cálculo de Distancias:**
        
        * Utiliza las coordenadas de las fábricas, centros de distribución y ciudades (promedio de las coordenadas de los puntos de demanda) para calcular $\text{Dist}_{ij}$ y $\text{Dist}_{jk}$.
    * **Organización de Datos:**
        
        * Crea estructuras de datos (diccionarios o matrices) para almacenar:
            
            * Capacidades de fábricas ($\text{Capacidad}_i$)
            * Demandas de ciudades ($\text{Demanda}_k$)
            * Distancias ($\text{Dist}_{ij}$, $\text{Dist}_{jk}$)
            * Otros parámetros (costos, pesos, N, M)
2. **Implementación en Gurobi:**
    
    * **Importar la Librería:**
        
        ```python
        import gurobipy as gp
        from gurobipy import GRB
        ```
        
    * **Crear el Modelo:**
        
        ```python
        model = gp.Model('Optimización_Transporte')
        ```
        
    * **Definir los Conjuntos:**
        
        * $I$, $J$, $K$ como listas o índices.
    * **Definir los Parámetros:**
        
        * Utiliza los datos preparados en el paso 1.
    * **Declarar las Variables de Decisión:**
        
        ```python
        # Variables continuas
        X = model.addVars(I, J, vtype=GRB.CONTINUOUS, name='X')
        Y = model.addVars(J, K, vtype=GRB.CONTINUOUS, name='Y')
        
        # Variables binarias
        Z = model.addVars(I, J, vtype=GRB.BINARY, name='Z')
        W = model.addVars(J, K, vtype=GRB.BINARY, name='W')
        ```
        
    * **Definir la Función Objetivo:**
        
        ```python
        # Costo desde fábricas a centros de distribución
        cost_fabricas = gp.quicksum(
            X[i,j] * Dist_ij[i,j] * PesoUnidad * CostoKgKm
            for i in I for j in J
        )
        
        # Costo desde centros de distribución a ciudades
        cost_centros = gp.quicksum(
            Y[j,k] * Dist_jk[j,k] * PesoUnidad * CostoKgKm
            for j in J for k in K
        )
        
        # Costo de distribución intraurbana
        cost_intra = gp.quicksum(
            Demanda[k] * CostoIntraCiudad
            for k in K
        )
        
        # Establecer la función objetivo
        model.setObjective(cost_fabricas + cost_centros + cost_intra, GRB.MINIMIZE)
        ```
        
    * **Agregar las Restricciones:**
        
        * **Capacidad de Producción de las Fábricas:**
            
            ```python
            for i in I:
                model.addConstr(
                    gp.quicksum(X[i,j] for j in J) >= 0.8 * Capacidad[i],
                    name=f'ProdMin_{i}'
                )
                model.addConstr(
                    gp.quicksum(X[i,j] for j in J) <= Capacidad[i],
                    name=f'ProdMax_{i}'
                )
            ```
            
        * **Balance en los Centros de Distribución:**
            
            ```python
            for j in J:
                model.addConstr(
                    gp.quicksum(X[i,j] for i in I) == gp.quicksum(Y[j,k] for k in K),
                    name=f'BalanceCD_{j}'
                )
            ```
            
        * **Satisfacción de la Demanda:**
            
            ```python
            for k in K:
                model.addConstr(
                    gp.quicksum(Y[j,k] for j in J) == Demanda[k],
                    name=f'Demanda_{k}'
                )
            ```
            
        * **Envíos Mínimos y Variables Binarias:**
            
            ```python
            for i in I:
                for j in J:
                    model.addConstr(
                        X[i,j] >= N * Z[i,j],
                        name=f'MinEnvioFabrica_{i}_{j}'
                    )
                    model.addConstr(
                        X[i,j] <= Capacidad[i] * Z[i,j],
                        name=f'MaxEnvioFabrica_{i}_{j}'
                    )
            
            for j in J:
                for k in K:
                    model.addConstr(
                        Y[j,k] >= M * W[j,k],
                        name=f'MinEnvioCD_{j}_{k}'
                    )
                    model.addConstr(
                        Y[j,k] <= Demanda[k] * W[j,k],
                        name=f'MaxEnvioCD_{j}_{k}'
                    )
            ```
            
        * **Coherencia entre Variables Continuas y Binarias:**
            
            * Ya se incluyó en las restricciones anteriores.
    * **Configurar Parámetros del Solver (Opcional):**
        
        * Por ejemplo, establecer un límite de tiempo:
            
            ```python
            model.Params.TimeLimit = 600  # 10 minutos
            ```
            
3. **Ejecución y Solución:**
    
    ```python
    model.optimize()
    ```
    
    * **Revisar el Estado de la Solución:**
        
        ```python
        if model.status == GRB.OPTIMAL:
            print('Costo mínimo total:', model.objVal)
        elif model.status == GRB.INFEASIBLE:
            print('El modelo es infactible.')
        else:
            print('El estado del modelo es', model.status)
        ```
        
4. **Análisis de Resultados:**
    
    * **Extracción de Variables Óptimas:**
        
        ```python
        # Cantidades enviadas desde fábricas a centros de distribución
        for i in I:
            for j in J:
                if X[i,j].X > 0:
                    print(f'Enviar {X[i,j].X} unidades desde fábrica {i} a centro {j}')
        
        # Cantidades enviadas desde centros de distribución a ciudades
        for j in J:
            for k in K:
                if Y[j,k].X > 0:
                    print(f'Enviar {Y[j,k].X} unidades desde centro {j} a ciudad {k}')
        ```
        
    * **Verificación de Restricciones:**
        
        * Confirma que todas las demandas se satisfacen y que las capacidades y mínimos se respetan.
    * **Análisis de Sensibilidad (Opcional):**
        
        * Explora cómo cambios en los costos o en $N$ y $M$ afectan la solución.

#### **Consideraciones Finales:**

* **Datos Precisos:**
    
    * Asegúrate de ingresar correctamente todos los datos, especialmente las distancias y demandas.
* **Validación de Resultados:**
    
    * Revisa que las fábricas estén produciendo al menos el 80% de su capacidad.
* **Interpretación:**
    
    * Utiliza los resultados para elaborar un plan logístico que minimice los costos.

#### **Conclusión**

Con los valores actualizados de $\text{XXX} = 270$ y $\text{YYY} = 114$, hemos reformulado el modelo de optimización para reflejar los costos y restricciones reales del problema. Al implementar este modelo en Gurobi, podrás encontrar la solución óptima que minimiza el costo total de transporte, cumpliendo con todas las restricciones operativas.


---

## Second Problem (40 Points)

Given an inventory of rolls with width W meters, determine how much of these rolls to cut so that \(b_i\), \(i = 1, ..., m\) units of width \(w_i\) are produced, minimizing the total square centimeters of roll waste. The requirements presented in the data for the m different sizes must be satisfied.

### Data for the Second Problem
The master roll size is 2500, and cut rolls that are not sold are considered waste. The lengths and demands of the rolls to be cut are:

Piece Length: 692, Demand: 14
Piece Length: 627, Demand: 25
Piece Length: 491, Demand: 50
Piece Length: 253, Demand: 38
Piece Length: 271, Demand: 19
Piece Length: 628, Demand: 32
Piece Length: 533, Demand: 50
Piece Length: 708, Demand: 18
Piece Length: 520, Demand: 12
Piece Length: 580, Demand: 16
Piece Length: 630, Demand: 39
Piece Length: 406, Demand: 39
Piece Length: 587, Demand: 36
Piece Length: 346, Demand: 40
Piece Length: 632, Demand: 45
Piece Length: 310, Demand: 49
Piece Length: 617, Demand: 30
Piece Length: 729, Demand: 11
Piece Length: 723, Demand: 27
Piece Length: 701, Demand: 27

### a) (15 points)
Formulate the Mixed Integer Linear Programming (MILP) model defining the possible cutting patterns.

### b) (25 points)
Find the solution to the previous model with the provided data using the Branch and Bound algorithm with Gurobi. Present the decision tree.

---

## Third Problem (40 Points)

You must schedule \(n\) jobs through a two-stage series process, where each stage has a machine. Each job \(j\) takes a time \(p_{ij}\), \(i = 1, 2\), and \(j = 1, ..., n\) to be processed on machine \(i\). Each job has a common due date \(d\) and an associated cost per unit of time for early delivery \(a_j\) and late delivery \(b_j\).

### Data for the Third Problem
To calculate the due date, follow the ORLIB library guidelines using h=0.4.

| **Trabajos** | **Máquina 1** | **Máquina 2** | **ai** | **bi** |
| ------------ | ------------- | ------------- | ------ | ------ |
| 1            | 41            | 34            | 199    | 1120   |
| 2            | 37            | 32            | 366    | 1264   |
| 3            | 44            | 24            | 443    | 1343   |
| 4            | 58            | 28            | 575    | 1378   |
| 5            | 43            | 29            | 542    | 1374   |
| 6            | 49            | 22            | 195    | 1342   |
| 7            | 53            | 36            | 453    | 1297   |
| 8            | 50            | 29            | 493    | 1182   |
| 9            | 43            | 24            | 321    | 1273   |
| 10           | 42            | 30            | 453    | 1328   |
| 11           | 45            | 28            | 136    | 1171   |

### a) (25 points)
Formulate the Mixed Integer Linear Programming (MILP) model minimizing the objective function provided in the data.

### b) (15 points)
Find the solution to the previous model with the provided data using Gurobi.
