\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{graphicx}
\usepackage{multirow}
\usepackage{booktabs}

\title{Taller 4 Optimización}
\author{Departamento de Ingeniería de Sistemas e Ingeniería Industrial\\Universidad Nacional de Colombia}

\begin{document}

\maketitle

\section*{Primer Punto (40 Puntos)}

Una compañía produce cierto tipo de accesorios. Estos accesorios se producen en una de las instalaciones de producción, luego se envían a uno de los centros de distribución y finalmente se despachan a los vendedores al detal.

Cada vendedor al detal tiene un pronóstico de demanda, cada instalación de producción tiene una cantidad mínima y máxima de accesorios que puede fabricar durante este período y cada centro de distribución tiene una capacidad máxima de accesorios que puede distribuir.

El costo de transporte por unidad sólo es válido si se transporta un número mínimo de unidades del accesorio ya sea desde las fábricas a los centros de distribución o desde estos últimos hacia los vendedores al detal, lo que significa que cualquier envío desde las instalaciones de producción a los centros de distribución debe ser mayor a N unidades y cualquier envío desde los centros de distribución a los vendedores al detal debe ser mayor a M unidades.

Como complemento del punto uno debe asegurarse que cada una de las fábricas produzca al menos el 80\% de su capacidad máxima de suministro y la cantidad mínima a transportar entre cualquier dos nodos debe ser mayor al valor de mínimo demanda total de un centro de demanda (ciudad).

\subsection*{Datos del Primer Punto}

\begin{table}[ht]
\centering
\begin{tabular}{ll}
\toprule
\textbf{Fábricas}     & \textbf{Capacidad} \\
\midrule
Bogotá       & 5502 \\
Medellín     & 5909 \\
Pereira      & 1497 \\
Cali         & 5862 \\
Barranquilla & 5161 \\
Bucaramanga  & 1254 \\
\bottomrule
\end{tabular}
\end{table}

\noindent Los sitios de las bodegas son: Bogotá, Medellín, Pereira, Cali, Barranquilla, Bucaramanga, Tenjo, Itagüí, Palmira, Manizales, Santa Marta, Popayán, Montería.

\subsection*{Ubicación y demanda de cada punto...}

City: Bogotá

\begin{itemize}
    \item Point 1: Coordinates: (4.568565647912089, -74.00270535750907), Demand: 333 units
    \item Point 2: Coordinates: (4.699675267272541, -74.07013834007228), Demand: 275 units
    \item ...
\end{itemize}

\noindent Total Demand: 8352 units

City: Medellín

\begin{itemize}
    \item Point 1: Coordinates: (6.24678283335728, -75.55975056917285), Demand: 76 units
    \item Point 2: Coordinates: (6.39187735180898, -75.45636631092621), Demand: 132 units
    \item ...
\end{itemize}

\noindent Total Demand: 2572 units

\subsection*{Costos}

Para los puntos de ubicación de la demanda en cada zona de demanda usar el promedio. El costo por kilogramo por kilómetro es 1270 pesos por kilogramo y cada unidad pesa 2.114 kilogramos. El costo de distribuir una unidad al interior de las ciudades considerarlo igual a 2270 pesos.

\subsection*{a) (25 puntos)}

Formular el modelo de Programación Lineal Entera Mixta (PLEM) que minimice el costo total de transporte.

\subsection*{b) (15 puntos)}

Encuentre la solución al modelo anterior con los datos provistos en el correo usando Gurobi.

\section*{Solución}

\subsection*{a) Formulación del Modelo de Programación Lineal Entera Mixta (PLEM)}

\subsubsection*{Parámetros}

\begin{itemize}
    \item \textbf{FABRICAS} ($f$): Conjunto de fábricas que producen accesorios.
    \item \textbf{BODEGAS} ($b$): Conjunto de centros de distribución a los que se envían los accesorios desde las fábricas.
    \item \textbf{TIENDAS} ($t$): Conjunto de tiendas que representan los puntos de demanda de los productos.
    \item $Capacidad_f$: Capacidad máxima de producción de la fábrica $f$.
    \item $Demanda_t$: Demanda total de la tienda $t$.
    \item $PesoUnidad$: Peso de cada unidad producida, 2.114 kg.
    \item $CostoInterCiudad$: Costo por kilogramo por kilómetro entre ciudades, 1270 pesos/kg-km.
    \item $CostoIntraCiudad$: Costo de distribución dentro de la misma ciudad, 2270 pesos por unidad.
    \item $Dist_{fb}$: Distancia entre la fábrica $f$ y el centro de distribución $b$.
    \item $Dist_{bt}$: Distancia entre el centro de distribución $b$ y la tienda $t$.
    \item $N$: Mínimo de unidades a enviar entre fábricas y bodegas, establecido en 210 unidades.
    \item $M$: Mínimo de unidades a enviar entre bodegas y tiendas, establecido en 4 unidades.
    \item $\alpha$: Porcentaje mínimo de utilización de la capacidad de las fábricas (80\%, es decir, $\alpha = 0.8$).
\end{itemize}

\subsubsection*{Variables de Decisión}

\begin{itemize}
    \item $X_{fb}$: Cantidad de unidades enviadas desde la fábrica $f$ al centro de distribución $b$.
    \item $Y_{bt}$: Cantidad de unidades enviadas desde el centro de distribución $b$ a la tienda $t$.
    \item $Z_{fb}$: Variable binaria que indica si se realiza envío desde la fábrica $f$ al centro de distribución $b$.
    \item $W_{bt}$: Variable binaria que indica si se realiza envío desde el centro de distribución $b$ a la tienda $t$.
\end{itemize}

\subsubsection*{Función Objetivo}

Minimizar el costo total de transporte, que se compone de dos partes:

\begin{itemize}
    \item \textbf{Intra-ciudad}: Cuando la fábrica y la bodega están en la misma ciudad, el costo por unidad es $CostoIntraCiudad$.
    \begin{equation}
        \sum_{f \in F} \sum_{b \in B} X_{fb} \times Dist_{fb} \times CostoIntraCiudad
    \end{equation}
    \item \textbf{Inter-ciudad}: Cuando la fábrica y la bodega están en diferentes ciudades, el costo depende del peso de las unidades transportadas y la distancia.
    \begin{equation}
        \sum_{f \in F} \sum_{b \in B} X_{fb} \times Dist_{fb} \times PesoUnidad \times CostoInterCiudad
    \end{equation}
\end{itemize}

... (continúa con la función objetivo y las restricciones, igual que en el markdown)

\section*{Segundo Punto (40 Puntos)}

Dado un inventario de rollos de ancho W metros, determine cuánto de estos rollos cortar de tal manera que $b_i$, $i = 1, ..., m$ unidades de ancho $w_i$ sean producidas, minimizando el total en centímetros cuadrados de desperdicio de rollos. 

\subsection*{Datos del segundo punto}

El tamaño del rollo maestro es 2500 y se consideran desperdicios los rollos cortados y no vendidos. Las longitudes y demandas de los rollos a cortar son:

\begin{table}[ht]
\centering
\begin{tabular}{ccc}
\toprule
\textbf{Pieza} & \textbf{Longitud (mm)} & \textbf{Demanda (unidades)} \\
\midrule
1 & 692 & 14 \\
2 & 627 & 25 \\
... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}

\subsection*{a) (15 puntos)}

Formular el modelo de Programación Lineal Entera Mixta (PLEM) definiendo los patrones de cortes posibles.

\subsection*{b) (25 puntos)}

Encuentre la solución al modelo anterior con los datos provistos a través del algoritmo de Branch and Bound usando Gurobi. Presentar el árbol de decisión.

\subsection*{Solución}

... (continúa con la solución del segundo punto)

\end{document}
