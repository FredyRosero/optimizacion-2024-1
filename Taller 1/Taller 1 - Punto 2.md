# Taller 1 - Punto 2
*Problema de Mezcla de Paquetes de Comida Saludable*

Una tienda vende tres tipos diferentes de paquetes de comida saludable: masticable, crujiente y granulado. Estos paquetes son hechos mezclando semillas de girasol, uvas pasas y maní. Las especificaciones para cada tipo de paquete de comida se dan en la siguiente tabla:

| Mezcla    | Semillas de girasol | Uvas pasas        | Maní             | Precio de venta $/Kg |
|-----------|---------------------|-------------------|------------------|----------------------|
| Masticable| -                   | al menos 60%      | a lo sumo 25%    | $2.700               |
| Crujiente | al menos 60%        | -                 | -                | $1.670               |
| Granulada | a lo sumo 20%       | -                 | al menos 60%     | $1.270               |

Los proveedores de los ingredientes pueden entregar cada semana máximo 100 Kg de semillas de girasoles a $1.140/Kg, 80 Kg de uvas pasas a $1.514/Kg y 60 Kg de maní a $814/Kg. Asumiendo que no hay límite en la demanda de los paquetes, formule el problema de encontrar el esquema de mezclado que maximiza la ganancia semanal **(15 puntos)**. Resuelva el problema usando Gurobi **(20 puntos)**.

## Desarrollo
Es un problema de maximización de ganancias a partir de la mezcla de diferentes ingredientes (semillas de girasol, uvas pasas y maní) para producir tres tipos de paquetes de comida saludable (masticable, crujiente y granulado).

#### Formulación del PL

**Variables de decisión:**

Definimos las variables de decisión como \( x_{ij} \) Kilogramos del componente $j$ (semillas de girasol, uvas pasas, maní) en la mezcla $i$ (masticable, crujiente, granulada), donde:
- \( x_{11} \): Kg de semillas de girasol en mezcla masticable.
- \( x_{12} \): Kg de uvas pasas en mezcla masticable.
- \( x_{13} \): Kg de maní en mezcla masticable.
- \( x_{21} \): Kg de semillas de girasol en mezcla crujiente.
- \( x_{22} \): Kg de uvas pasas en mezcla crujiente.
- \( x_{23} \): Kg de maní en mezcla crujiente.
- \( x_{31} \): Kg de semillas de girasol en mezcla granulada.
- \( x_{32} \): Kg de uvas pasas en mezcla granulada.
- \( x_{33} \): Kg de maní en mezcla granulada.

**Parámetros:**

$v_i$: Precio de venta por kilogramo de la mezcla $i$. donde $i \in \{1, 2, 3\}$:
 - $v_1 = 2700$: Precio de venta por kilogramo de la mezcla masticable.
 - $v_2 = 1670$: Precio de venta por kilogramo de la mezcla crujiente.
 - $v_3 = 1270$: Precio de venta por kilogramo de la mezcla granulada.

$c_i$: Costo por kilogramo del componente $j$, donde $j \in \{1, 2, 3\}$:
 - $c_1 = 1140$: Costo por kilogramo de semillas de girasol.
 - $c_2 = 1514$: Costo por kilogramo de uvas pasas.
 - $c_3 = 814$: Costo por kilogramo de maní.
  
$p_{ij}$: Porcentaje requerido del componente $j$ en la mezcla $i$, donde $i \in \{1, 2, 3\}$ y $j \in \{1, 2, 3\}$:
 - $p_{11} = 0$: No se requiere semillas de girasol en la mezcla masticable.
 - $p_{12} = 0.6$: Se requiere al menos 60% de uvas pasas en la mezcla masticable.
 - $p_{13} = 0.25$: Se requiere a lo sumo 25% de maní en la mezcla masticable.
 - $p_{21} = 0.6$: Se requiere al menos 60% de semillas de girasol en la mezcla crujiente.
 - $p_{22} = 0$: No se requiere uvas pasas en la mezcla crujiente.
 - $p_{23} = 0$: No se requiere maní en la mezcla crujiente.
 - $p_{31} = 0$: No se requiere semillas de girasol en la mezcla granulada.
 - $p_{32} = 0$: No se requiere uvas pasas en la mezcla granulada.
 - $p_{33} = 0.6$: Se requiere al menos 60% de maní en la mezcla granulada.

$k_j$: Disponibilidad semanal en kilogramos del componente $j$, donde $j \in \{1, 2, 3\}$:
 - $k_1 = 100$: Disponibilidad semanal en kilogramos de semillas de girasol.
 - $k_2 = 80$: Disponibilidad semanal en kilogramos de uvas pasas.
 - $k_3 = 60$: Disponibilidad semanal en kilogramos de maní.

**Función objetivo:** Maximizar las ganancias totales restando los costos de los ingredientes: 
$$
\begin{align*}
\text{Maximizar } z &= \sum_{i=1}^{3} {\sum_{j=1}^{3} {x_{ij} \cdot v_i} } & - \sum_{j=1}^{3} {\sum_{i=1}^{3} {x_{ij} \cdot c_i} }
\\
\text{Maximizar } z &= v_1 \sum_{j=1}^{3} x_{1j} + v_2 \sum_{j=1}^{3} x_{2j} + v_3 \sum_{j=1}^{3} x_{3j} & - c_1 \sum_{i=1}^{3} x_{i1} - c_2 \sum_{i=1}^{3} x_{i2} - c_3 \sum_{i=1}^{3} x_{i3}
\\
\text{Maximizar } z &= 2700\sum_{j=1}^{3} x_{1j}  + 1670 \sum_{j=1}^{3} x_{2j} + 1270 \sum_{j=1}^{3} x_{3j} & - 1140 \sum_{i=1}^{3} x_{i1} - 1514 \sum_{i=1}^{3} x_{i2} - 814 \sum_{i=1}^{3} x_{i3}
\\
\text{Maximizar } z &= 2700(x_{11}+x_{12}+x_{13}) + 1670(x_{21}+x_{22}+x_{23}) + 1270(x_{31}+x_{32}+x_{33}) & - 1140(x_{11}+x_{21}+x_{31}) - 1514(x_{12}+x_{22}+x_{32}) - 814(x_{13}+x_{23}+x_{33})
\end{align*}
$$

**Restricciones:**

Como sumatorias

$$
\begin{align*}
x_{12} \geq p_{12} \sum_{j=1}^{3} x_{1j} \\
x_{13} \leq p_{13} \sum_{j=1}^{3} x_{1j} \\
x_{21} \geq p_{21} \sum_{j=1}^{3} x_{2j} \\
x_{31} \leq p_{31} \sum_{j=1}^{3} x_{3j} \\
x_{33} \geq p_{33} \sum_{j=1}^{3} x_{3j} \\
\sum_{i=1}^{3} x_{ij} \leq k_j \text{ para } j \in \{1, 2, 3\} \\
x_{ij} \geq 0 \text{ para } i \in \{1, 2, 3\} \text{ y } j \in \{1, 2, 3\}
\end{align*}
$$

Simplificación de las restricciones:

1. $x_{12} \geq 0.6 \sum_{j=1}^{3} x_{1j}$: Se requiere al menos 60% de uvas pasas $x_i2$ en la mezcla masticable $x_1j$.
2. $x_{13} \leq 0.25 \sum_{j=1}^{3} x_{1j}$: Se requiere a lo sumo 25% de maní $x_i3$ en la mezcla masticable $x_1j$.
3. $x_{21} \geq 0.6 \sum_{j=1}^{3} x_{2j}$: Se requiere al menos 60% de semillas de girasol $x_i1$ en la mezcla crujiente $x_2j$. 
4. $x_{31} \leq 0.2 \sum_{j=1}^{3} x_{3j}$: Se requiere a lo sumo 20% de semillas de girasol $x_i1$ en la mezcla granulada $x_3j$.
5. $x_{33} \geq 0.6 \sum_{j=1}^{3} x_{3j}$: Se requiere al menos 60% de maní $x_i3$ en la mezcla granulada $x_3j$.
6. $\sum_{i=1}^{3} x_{i1} \leq 100$: Disponibilidad semanal de semillas de girasol $x_i1$ para las 3 mezclas.
7. $\sum_{i=1}^{3} x_{i2} \leq 80$: Disponibilidad semanal de uvas pasas $x_i2$ para las 3 mezclas.
8. $\sum_{i=1}^{3} x_{i3} \leq 60$: Disponibilidad semanal de maní $x_i3$ para las 3 mezclas.
9. $x_{ij} \geq 0$: No negatividad de las variables de decisión.

