## Glosario de Optimización (Segundo Corte)

## Grafo
Un grafo $G$ es un par ordenado, $G = (V, E)$, donde:
- $V$ es un conjunto de vértices o nodos.
- $E$ es un conjunto de aristas o arcos, que relacionan estos nodos.

### Nodo
Los nodos son los vértices de un grafo o red. Se definen a través del conjunto $V$ o $N$.

### Arco
Consiste en un par ordenado de vértices y representa una posible dirección o movimiento que puede ocurrir entre los vértices. Se define a través del conjunto $A$ o $E$.

### Orden del Grafo
El orden de un grafo es el número de vértices que contiene, $|V|$.

### Grado de un Vértice
El númerco de arcos de lo tienen como extremo. Se denota por $d(v)$.

### Bucle
Un bucle es un arco que relaciona al mismo nodo (el nodo inicial y el nodo final coinciden).

### Cadena
Una cadena es una secuencia de arcos tal que cada arco sólo tiene un vértice en común con el arco previo.

### Camino
Un camino es una cadena donde el nodo terminal de un arco es el nodo inicial del siguiente arco.

### Ciclo
Un ciclo es una sucesión de aristas adyacentes, donde no se recorre dos veces la misma arista, y se regresa al punto inicial. 

### Grafo Conexo
Un grafo es conexo si existe un camino entre cada par de nodos.

### Grafo No Dirigido
Un grafo no dirigido es un grafo en el que las aristas no tienen dirección.

### Ciclo Hamiltoniano
Un ciclo hamiltoniano recorre todos los vértices exactamente una vez (excepto el vértice del que parte y al cual llega).

### Árbol de Expansión Mínima (MST - Minimum Spanning Tree):
Dado un grafo conexo y no dirigido, un **árbol recubridor** o **árbol de expansión mínima** de ese grafo es un subgrafo que es un árbol y contiene todos los vértices del grafo inicial.

> Subconjunto de aristas de un grafo no dirigido y ponderado que conecta todos los vértices con el costo total mínimo y sin formar ciclos.

### Ruta Más Corta:
Problema de optimización en redes que busca encontrar el camino de menor costo entre dos nodos en un grafo, donde el costo puede representar distancia, tiempo, etc.

### Algoritmo de Kruskal
El algoritmo de Kruskal es un ejemplo de algoritmo voraz que funciona de la siguiente manera:

1. Se crea un bosque B (un conjunto de árboles), donde cada vértice del grafo es un árbol separado.
2. Se crea un conjunto C que contenga todas las aristas del grafo.
3. Mientras C no sea vacío:
   - Eliminar una arista de peso mínimo de C.
   - Si esa arista conecta dos árboles diferentes, se añade al bosque, combinando los dos árboles en un solo árbol.
   - En caso contrario, se desecha la arista.
4. Al acabar el algoritmo, el bosque tiene un solo componente, el cual forma un árbol de expansión mínima del grafo.

### Algoritmo de Prim
El algoritmo de Prim puede describirse informalmente con los siguientes pasos:

1. Inicializar un árbol con un único vértice, elegido arbitrariamente, del grafo.
2. Aumentar el árbol por un lado (la unión entre dos vértices). De las posibles uniones que pueden conectar el árbol a los vértices que no están aún en el árbol, encontrar el lado de menor distancia y unirlo al árbol.
3. Repetir el paso 2 hasta que todos los vértices pertenezcan al árbol.

### Problemas de Flujo en Redes

Tratan del movimiento de una mercancía a través de una red representada como un grafo dirigido. Este grafo consiste en **nodos** conectados por **arcos**, donde cada arco tiene una **capacidad** que limita la cantidad de flujo que puede transportar. A continuación se desglosan los elementos clave:

* **Red:** Representada como un grafo dirigido:
  * **Nodos:** Puntos en la red donde el flujo se origina (**origen**), termina (**destino**) o pasa a través de ellos (**nodos de transbordo**).
  * **Arcos:** Conexiones dirigidas entre nodos, que representan posibles rutas de flujo. Cada arco (i, j) tiene una capacidad (denotada como *c(i, j)* o *Uij* en las fuentes), que indica el flujo máximo permitido desde el nodo *i* al nodo *j*.

* **Flujo:** El movimiento de una mercancía a través de la red, cumpliendo con las restricciones:
  * **Restricciones de Capacidad:** El flujo en un arco no puede exceder su capacidad (0 ≤ *x(i, j)* ≤ *c(i, j)*, donde *x(i, j)* es el flujo en el arco (i, j)).
  * **Conservación del Flujo:** En cada nodo (excepto el origen y el destino), el flujo total entrante debe ser igual al flujo total saliente.

* **Objetivo:** Los problemas de flujo en redes buscan optimizar un objetivo relacionado con el flujo, típicamente minimizando el costo o maximizando el flujo.

Las fuentes detallan varios tipos específicos de problemas de flujo en redes:

## Problemas de Transporte
Es un tipo específico de problema de programación lineal que se enfoca en determinar la mejor manera de transportar bienes desde múltiples puntos de suministro (orígenes) a múltiples puntos de demanda (destinos). El objetivo es típicamente minimizar el costo total de envío mientras se satisfacen tanto las restricciones de oferta como de demanda.

Aquí hay un desglose de los elementos clave:
* **Puntos de Suministro:** Estos son los lugares que tienen una cierta cantidad de bienes disponibles para enviar. Cada punto de suministro *i* tiene una capacidad máxima de suministro, denotada como *s_i*.
* **Puntos de Demanda:** Estos son los lugares que necesitan recibir una cierta cantidad de bienes. Cada punto de demanda *j* tiene un requisito mínimo de demanda, denotado como *d_j*.
* **Costos de Envío:** Cada unidad de bienes enviada desde el punto de suministro *i* al punto de demanda *j* incurre en un costo variable, denotado como *c_ij*. Este costo generalmente representa factores como la distancia, el modo de transporte y otros gastos relevantes.

* **Problema Equilibrado vs. Desbalanceado:** 
    * Un problema de transporte se considera **equilibrado** si el suministro total es igual a la demanda total. En este caso, todos los bienes de los puntos de suministro se envían para satisfacer las demandas exactas de los puntos de destino.
    * Si el suministro total excede la demanda total, se agrega un **punto de demanda ficticio** con costos de envío cero para absorber el exceso de suministro. Este punto ficticio representa la capacidad de suministro no utilizada.
    * Cuando el suministro total es estrictamente menor que la demanda total, el problema no tiene una solución factible a menos que permitamos que parte de la demanda quede insatisfecha. Este escenario generalmente implica incorporar costos de penalización por demanda insatisfecha en el modelo.

La formulación matemática general de un problema de transporte de minimización es la siguiente:
$$
\begin{align*}
\text{Minimizar} &\sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} x_{ij} \\
\text{Sujeto a:} &\\
&\sum_{j=1}^{n} x_{ij} \leq s_i \quad &\text{para cada punto de suministro } i = 1, 2, \ldots, m \\
&\sum_{i=1}^{m} x_{ij} \geq d_j \quad &\text{para cada punto de demanda } j = 1, 2, \ldots, n \\
&x_{ij} \geq 0 \quad &\text{Restricciones de no negatividad para todos los envíos}
\end{align*}
$$

Donde:

* *x_{ij}* representa el número de unidades enviadas desde el punto de suministro *i* al punto de demanda *j*.
* *c_{ij}* es el costo de envío de una unidad desde el punto de suministro *i* al punto de demanda *j*.
* *s_i* es la capacidad de suministro del punto de suministro *i*.

Para resolver un problema de transporte, se pueden utilizar varios métodos y técnicas, incluyendo:
   * Encontrar una solución básica factible utilizando métodos como la Regla de la Esquina Noroeste, el Método de Costo Mínimo y el Método de Aproximación de Vogel.
   * El Método Simplex de Transporte para encontrar la solución óptima.
   * Análisis de Sensibilidad para entender cómo los cambios en la oferta, la demanda o los costos impactan la solución óptima.

### Tableau de Transporte:
Los datos para un problema de transporte, incluidos los costos de envío, los valores de suministro y los valores de demanda, suelen resumirse en un **tableau de transporte**.

* Este tableau es una matriz donde **las filas representan los puntos de suministro** y **las columnas representan los puntos de demanda**.
* La celda en la fila *i* y la columna *j* corresponde a la variable *x_{ij}* (el número de unidades enviadas desde el punto de suministro *i* al punto de demanda *j*).
* El costo de envío *c_{ij}* generalmente se muestra en cada celda.


### Problemas de Asignación
Estos son un caso especial de problemas de transporte donde cada punto de suministro tiene una oferta de una unidad y cada punto de demanda tiene una demanda de una unidad. Esto es análogo a asignar una tarea a un trabajador. Las fuentes presentan el Método Húngaro como una técnica eficiente de solución para problemas de asignación.

### Problemas de Transbordo
A diferencia de los problemas de transporte que solo permiten envíos directos desde los puntos de suministro a los puntos de demanda, los problemas de transbordo permiten envíos entre puntos de suministro, entre puntos de demanda, o a través de puntos de transbordo intermedios. Las fuentes ilustran cómo transformar un problema de transbordo en un problema de transporte equilibrado para una solución más sencilla.

### Problemas de Ruta Más Corta
Estos problemas tienen como objetivo encontrar la ruta más corta entre dos nodos en una red, donde la "distancia" puede representar tiempo, costo u otra métrica. Las fuentes explican cómo modelar un problema de ruta más corta como un problema de transbordo y también mencionan el Algoritmo de Dijkstra como un enfoque de solución.

### Problemas de Flujo Máximo
El objetivo aquí es determinar el flujo máximo posible que puede ser dirigido desde un nodo de origen a un nodo de destino en la red. Como se discutió en nuestro historial de conversación, las fuentes proporcionan explicaciones detalladas sobre:
   * La formulación de problemas de flujo máximo como programas lineales.
   * El Algoritmo de Ford-Fulkerson para encontrar el flujo máximo.
   * El concepto de cortes y el Teorema de Flujo Máximo-Corte Mínimo para verificar la optimalidad de la solución.

### Problemas de Flujo de Costo Mínimo (MCNFP)
El tipo más general discutido en las fuentes, que abarca todos los problemas anteriores como casos especiales. Los MCNFPs implican minimizar el costo total de enviar flujo a través de una red mientras se cumplen los requisitos de oferta y demanda en diferentes nodos. Se resuelven utilizando el método de simplex en redes, una generalización del método de transporte simplex.

### Método de la Ruta Crítica (CPM)
Aunque no está categorizado explícitamente como un problema de flujo en red en las fuentes, el CPM puede verse como un caso especial que se enfoca en encontrar la ruta más larga (ruta crítica) en una red de proyectos, lo que determina el tiempo mínimo de finalización del proyecto.


### Problemas de Flujo Máximo

Son un subconjunto de los problemas de flujo en redes, se centran en determinar el **mayor flujo posible** que puede dirigirse desde un **nodo de origen** designado a un **nodo de destino** designado dentro de una red. La red se representa como un grafo dirigido con nodos conectados por arcos, cada uno de los cuales tiene una capacidad que limita el flujo a través de él.


* **Nodos:** Representan puntos en la red donde el flujo puede originarse (origen), terminar (destino) o pasar a través de ellos (nodos de transbordo).
* **Arcos:** Representan las conexiones entre nodos, indicando las posibles rutas de flujo. Cada arco (i, j) que conecta el nodo *i* con el nodo *j* tiene una **capacidad**, denotada como *c(i, j)* o *Uij* en las fuentes, que representa el flujo máximo permitido a través de ese arco.

**2. Flujo Factible:**

Una asignación de flujo se considera factible si cumple con estos criterios:

* **Restricciones de Capacidad:** El flujo a través de cualquier arco no puede exceder su capacidad: 0 ≤ *x(i, j)* ≤ *c(i, j)*, donde *x(i, j)* denota el flujo en el arco (i, j).
* **Conservación del Flujo:** En cada nodo (excepto el origen y el destino), el flujo total que entra al nodo debe ser igual al flujo total que sale del nodo.

**3. Objetivo:**

El objetivo principal de un problema de flujo máximo es **maximizar el flujo** enviado desde el nodo de origen al nodo de destino. Este flujo es equivalente al flujo total que sale del origen o al flujo total que entra al destino, debido al principio de conservación del flujo.

**4. Métodos de Solución:**

Las fuentes presentan dos enfoques principales para resolver problemas de flujo máximo:

* **Programación Lineal (PL):** 
  * Podemos formular un problema de flujo máximo como un programa lineal. El objetivo es maximizar el flujo a través de un arco artificial añadido desde el destino de regreso al origen (representando el flujo total), sujeto a las restricciones de capacidad y ecuaciones de balance de flujo para cada nodo.
  * Las fuentes proporcionan un ejemplo específico utilizando esta formulación para resolver el problema de flujo en un oleoducto de Sunco Oil en la Figura 6. También demuestran cómo modelar el problema en LINGO para una solución eficiente.

* **Algoritmo de Ford-Fulkerson:**
  * Este algoritmo iterativo comienza con un flujo factible (a menudo un flujo cero) y encuentra repetidamente caminos de aumento de flujo a través de la red.
  * **Camino Aumentante:** Es un camino desde el origen hasta el destino a lo largo del cual el flujo puede incrementarse respetando las capacidades de los arcos.
  * El algoritmo identifica caminos aumentantes utilizando un procedimiento de etiquetado descrito en detalle en las fuentes (pasos 1-3 bajo 'Encontrar Flujo Máximo mediante el Método de Ford-Fulkerson'). El proceso involucra tanto arcos hacia adelante (donde el flujo puede incrementarse) como arcos hacia atrás (donde el flujo puede disminuir) para explorar todas las formas posibles de aumentar el flujo.
  * El algoritmo continúa aumentando el flujo a lo largo de los caminos hasta que no existen más caminos aumentantes. En este punto, el flujo es máximo. Las fuentes ilustran el método de Ford-Fulkerson a través de ejemplos en las Figuras 10, 11, 12, 13 y 17.

**5. Cortes y Optimalidad:**

* **Corte:** En una red de flujo, un corte es una partición de los nodos en dos conjuntos, uno que contiene el origen y el otro que contiene el destino. Cualquier arco que cruce esta partición (que vaya del conjunto del origen al conjunto del destino) forma parte del corte.
* **Capacidad de un Corte:** Es la suma de las capacidades de todos los arcos en el corte.
* **Teorema de Flujo Máximo-Corte Mínimo:** Este importante teorema establece que el flujo máximo desde el origen al destino es igual a la capacidad mínima de cualquier corte que separe el origen del destino. Esto proporciona una forma de verificar la optimalidad de una solución encontrada usando el método de Ford-Fulkerson.

**6. Aplicaciones:**

Las fuentes ilustran la relevancia de los problemas de flujo máximo a través de varios ejemplos prácticos, incluyendo:

* **Transporte:** Determinación del número máximo de vuelos que una aerolínea puede programar entre dos ciudades, considerando las limitaciones de escala (Ejemplo 4, Figura 7).
* **Asignación:** Encontrar el número máximo de emparejamientos compatibles que se pueden hacer, como emparejar mentores y alumnos o asignar tareas a trabajadores (Ejemplo 5, Figura 8).
* **Logística:** Maximización del flujo de bienes a través de una cadena de suministro con restricciones de capacidad en los enlaces de transporte.

**7. Implementación de Software:**

Las fuentes demuestran el uso de LINGO para resolver problemas de flujo máximo (ver 'Resolución de Problemas de Flujo Máximo con LINGO'). Esto resalta la practicidad de usar software de optimización para resolver eficientemente problemas de flujo en redes del mundo real.
``` 

Esta traducción conserva la estructura y los detalles del texto original en inglés, pero en español. ¡Si necesitas más ajustes o traducciones adicionales, házmelo saber!

### Programación Dinámica:
Técnica de optimización que resuelve problemas complejos dividiéndolos en subproblemas más pequeños, utilizando soluciones de subproblemas para construir soluciones a problemas más grandes.

### Programación Lineal Entera Mixta (MIP - Mixed Integer Programming):
Tipo de programación lineal en la cual algunas variables están restringidas a ser enteras, mientras que otras pueden ser continuas. Se utiliza para modelar problemas de optimización donde algunas decisiones son discretas.

### Gurobi:
Software comercial para la optimización matemática que permite resolver problemas de programación lineal, programación entera mixta, programación cuadrática, y otros tipos de problemas de optimización.

### OR Tools:
Conjunto de herramientas de optimización de código abierto desarrolladas por Google, que incluyen algoritmos para resolver problemas de programación lineal, programación entera mixta, programación de flujo de red, etc.

### Dualidad en Optimización de Redes:
Relación entre el problema primal de optimización de redes (por ejemplo, minimizar costos de transporte) y su problema dual correspondiente (por ejemplo, maximizar beneficios en un mercado).

### Análisis Post-Óptimo:
Evaluación de cómo cambian los resultados de la solución óptima de un problema de optimización cuando se modifican los parámetros del problema, como los costos, los recursos disponibles o las capacidades.

---

### Conceptos y Técnicas Clave del Segundo Corte

Modelado de Redes:
Representación matemática de problemas logísticos o de flujo mediante grafos, donde los nodos representan puntos (como almacenes o ciudades) y los arcos representan rutas o conexiones.

Teorema del Flujo Máximo-Mínimo Corte:
Teorema que establece que el valor del flujo máximo en una red es igual a la capacidad del corte mínimo, es decir, la menor capacidad total que debe ser eliminada para desconectar la fuente del destino.

Método de Dijkstra:
Algoritmo utilizado para encontrar la ruta más corta desde un nodo inicial a todos los demás nodos en un grafo con aristas no negativas.

Algoritmo de Prim y Kruskal:
Algoritmos utilizados para encontrar el árbol de expansión mínima (MST) en un grafo ponderado y no dirigido.

Método de Ford-Fulkerson:
Algoritmo utilizado para resolver problemas de flujo máximo en redes. Funciona encontrando caminos de aumento en un grafo residual.

Red de Transporte:
Tipo de red donde los nodos representan lugares (como fábricas, almacenes, mercados) y los arcos representan rutas para el transporte de bienes con costos asociados.

Variables Duales:
Variables que representan el valor marginal o precio sombra de cada restricción en un problema de optimización.

---

### Pasos para Resolver Problemas del Segundo Corte

Modelar el Problema de Red usando Grafos.
Formular las Restricciones y Función Objetivo.
Utilizar Software (Gurobi) para Resolver el Problema.
Interpretar los Resultados y Realizar Análisis de Sensibilidad.
