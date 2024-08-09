# Examen 1 - Optimización 2023-1

## 1. 

Carlos debe limitarse a una dieta de carne de res y queso. A él se le restringe la cantidad de estos artículos a elegir ya que solo dispone de $2,450 para adquirirlos, pero es importante satisfacer ciertos requerimientos mínimos y minimizar el consumo de colesterol. La tabla siguiente refleja la cantidad (en miligramos) de vitamina A, B y C que contiene cada uno de los productos alimenticios, así como también su nivel (unidades) de colesterol. La tabla también incluye los requerimientos mínimos diarios de vitaminas y el costo de cada uno de los productos.

| Componente de los alimentos | Queso (mg/Kg) | Carne de res (mg/lb) | Requerimientos diarios mínimos (mg) |
|-----------------------------|---------------|----------------------|-------------------------------------|
| Vitamina A                  | 2             | 3                    | 2                                   |
| Vitamina B                  | 200           | 20                   | 60                                  |
| Vitamina C                  | 200           | 200                  | 25                                  |
| Colesterol                  | 40 Ud/Kg      | 100 Ud/lb            | -                                   |
| Costo                       | $2,500/Kg     | $2.750/lb            | -                                   |

**Plantear el anterior problema a través de un modelo de Programación Lineal (P.L.). (50 puntos)**

## 2. 

A continuación se muestra el modelo de programación lineal de un problema de optimización.

$$
\begin{align*}
\text{Maximizar } z &= 180000x_1 + 220000x_2 + 20000x_3 \\
\text{sujeto a:} \\
15x_1 + 10x_2 + 8x_3 &\leq 18789 \\
15x_1 + 15x_2 + 4x_3 &\leq 18123 \\
3x_1 + 4x_2 + 2x_3 &\leq 9789 \\
x_1, x_2, x_3 &\geq 0
\end{align*}
$$

El valor $z^*$ es 26185000 correspondiente a $x_1 = 923$, $x_2 = 223$ y $x_3 = 233.75$.

a) **Formule el problema dual del problema anterior. (10 puntos)**

b) **Encuentre los valores de las variables duales. (25 puntos)**

## 3.

Una empresa productora de jugos vende bolsas de naranjas y cartones de jugo de naranja. El jugo de naranja califica la naranja en una escala del 1 (malo) al 10 (excelente). La empresa tiene disponibles en el momento 12000 libras de naranjas de grado 10 y 15000 libras de naranjas de grado 7. La calidad promedio (por peso) de las naranjas vendidas en bolsas debe ser al menos 8, y la calidad promedio de las naranjas utilizadas para producir jugo de naranja debe ser al menos 9. Cada libra de naranjas que se usa para jugo produce un ingreso de $7,500 e incluye una variable costo (que consiste de costos laborales, costos generales, costos de inventario, etc.) de $5,250. Cada libra de naranjas vendidas en bolsas genera un ingreso de $2,500 e incluye un costo variable de $1,000.

a) **Formule el problema de optimización de Programación Lineal (P.L.) para maximizar las utilidades definiendo las variables de decisión como $x_{ij}$, las libras del grado $i$, en donde $i \in \{7, 10\}$, usadas en el producto $j$, donde $j \in \{\text{jugo, bolsas naranjas}\} (10 puntos)**

b) **En la solución óptima todas las variables de decisión son básicas y la matriz $A_B^{-1}$ para un valor $z^*$ de 47250000 es:**

$$
A_B^{-1} = \begin{pmatrix}
-0.33333333 & 0.66666667 & -0.66666667 \\
1.33333333 & -0.66666667 & 0.33333333 \\
-0.66666667 & 1.33333333 & -0.66666667 \\
0.66666667 & -0.33333333 & 0.66666667
\end{pmatrix}
$$

**Encuentre los valores de las variables $x_{ij}$ para $i \in \{7, 10\}$ y $j \in \{\text{jugo, bolsas naranjas}\}. (10 puntos)**

c) **Encuentre los valores de las variables duales y determine en cuánto aumentarían las utilidades si se dispusiera de 1200 libras adicionales de naranjas de calidad 7. (15 puntos)**
