# Primer corte

## Definiciones en Programación Lineal

### Función lineal
Una función en la cual cada variable se multiplica por una constante y se suman.
 **Ejemplo**: $f(x, y) = 3x + 4y$.

### Inecuación lineal
Una inecuación que involucra una función lineal.
**Ejemplo**: $2x + 3y \leq 5$.

### Sistema de ecuaciones lineales
Conjunto de ecuaciones lineales que deben satisfacerse simultáneamente. **Ejemplo**: 
$$\begin{aligned}  
2x_1 + 3x_2 &= 6 \\  
x_1 - x_2 &= 2  
\end{aligned}
$$

### PL: Programación Lineal
Método de optimización que se utiliza para encontrar la mejor solución a un problema matemático lineal, dadas ciertas restricciones.

### Forma General Matricial

Modelo de minimización
$$
\begin{align*}
\text{Minimizar } & z = \mathbf{c} \mathbf{x} \\
\text{Sujeto a:} & \\
&\mathbf{A} \mathbf{x} \leq \mathbf{b} \\
&\mathbf{x} \geq \mathbf{0}
\end{align*}
$$

Modelo de maximización
$$
\begin{align*}
\text{Maximizar } & z = \mathbf{c} \mathbf{x} \\
\text{Sujeto a:} & \\
&\mathbf{A} \mathbf{x} \geq \mathbf{b} \\
&\mathbf{x} \geq \mathbf{0}
\end{align*}
$$

Donde
* $\mathbf{c}$: Vector de coeficientes de la función objetivo.
* $\mathbf{x}$: Vector de variables de decisión.
* $\mathbf{b}$: Vector del RHS las restricciones.
* $\mathbf{A}$: Matriz de coeficientes de las restricciones.

**Referencia**: Bula, Slides de Programación Lineal: Método Simplex, 2024, p. 5.

**Componentes del Modelo**

* **$\mathbf{c}$**: Vector de coeficientes de la función objetivo.
    
    $$\mathbf{c} = [c_1 \; c_2 \; \cdots \; c_n]$$

* **$\mathbf{x}$**: Vector de variables de decisión. $\mathbf{x} \in \mathbb{R}^{n \times 1}$. $\mathbf{x} \geq \mathbf{0}$: Todas las variables de decisión deben ser no negativas, es decir, deben ser iguales o mayores que cero.
    
    $$\mathbf{x} = \begin{pmatrix}  
    x_1 \\  
    x_2 \\  
    \vdots \\  
    x_n  
    \end{pmatrix}$$

* **$\mathbf{b}$**: Vector del lado derecho de las restricciones. $\mathbf{b} \in \mathbb{R}^{m \times 1}$
    
    $$\mathbf{b} = \begin{pmatrix}  
    b_1 \\  
    b_2 \\  
    \vdots \\  
    b_m  
    \end{pmatrix}$$

* **$\mathbf{A}$**: Matriz de coeficientes de las restricciones. $\mathbf{A} \in \mathbb{R}^{m \times n}$
    
    $$\mathbf{A} = \begin{pmatrix}  
    a_{11} & a_{12} & \cdots & a_{1n} \\  
    a_{21} & a_{22} & \cdots & a_{2n} \\  
    \vdots & \vdots & \ddots & \vdots \\  
    a_{m1} & a_{m2} & \cdots & a_{mn}  
    \end{pmatrix}$$

* **$\mathbf{0}$**: Vector de ceros que establece la no negatividad de las variables de decisión. $\mathbf{0} \in \mathbb{R}^{n \times 1}$
    
    $$\mathbf{0} = \begin{pmatrix}  
    0 \\  
    0 \\  
    \vdots \\  
    0  
    \end{pmatrix}$$

### Suposiciones en Programación Lineal

1. **Proporcionalidad**:
    
    * **Descripción**: La contribución de cada variable a la función objetivo y a las restricciones es proporcional a su nivel de actividad.
    * **Implicación**: Si el coeficiente de $x_j$ en la función objetivo es $c_j$, entonces incrementar $x_j$ en una unidad incrementará la función objetivo en $c_j$. Similarmente, si el coeficiente de $x_j$ en una restricción es $a_{ij}$, incrementar $x_j$ en una unidad incrementará la cantidad del recurso usado en $a_{ij}$.
    * **Ejemplo**: Si producir una unidad de un producto genera $10 de beneficio, entonces producir 10 unidades generará $100 de beneficio.
    * **Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 53.
2. **Aditividad**:
    
    * **Descripción**: La contribución total de todas las variables a la función objetivo y a las restricciones es la suma de sus contribuciones individuales.
    * **Implicación**: Las funciones objetivo y las restricciones son lineales, es decir, pueden expresarse como una suma de términos individuales que involucran variables de decisión.
    * **Ejemplo**: Si la función objetivo es $3x_1 + 5x_2$, el beneficio total es la suma de $3x_1$ (beneficio del primer producto) y $5x_2$ (beneficio del segundo producto).
    * **Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 53.

3. **Divisibilidad**:
    
    * **Descripción**: Las variables de decisión pueden tomar valores fraccionarios, no solo enteros.
    * **Implicación**: Se asume que los productos pueden producirse y los recursos pueden usarse en cualquier cantidad fraccionaria.
    * **Ejemplo**: Si $x_1$ representa el número de unidades producidas, $x_1 = 2.5$ es una solución válida.

4. **Certeza**:
    
    * **Descripción**: Todos los coeficientes en la función objetivo y en las restricciones son conocidos con certeza y son constantes.
    * **Implicación**: No hay incertidumbre en los valores de los parámetros del modelo. Los coeficientes $c_j$, $a_{ij}$ y $b_i$ son todos conocidos y no cambian.
    * **Ejemplo**: El costo de producción, la disponibilidad de recursos y los coeficientes de las restricciones son todos valores fijos y conocidos.
    * **Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 54.

**Ejemplo de Aplicación de Suposiciones en Programación Lineal**:

Supongamos que una empresa fabrica dos productos, $P1$ y $P2$. La función objetivo es maximizar el beneficio total, y las restricciones son la disponibilidad de tiempo de trabajo y material.

* **Función Objetivo**:
    
    $$Z = 30P1 + 40P2$$
    
    donde $30$ es el beneficio por unidad de $P1$ y $40$ es el beneficio por unidad de $P2$.
    
* **Restricciones**:
    
    $$\begin{aligned}  
    2P1 + 1P2 &\leq 100 \quad \text{(Tiempo de trabajo disponible)} \\  
    1P1 + 2P2 &\leq 80 \quad \text{(Material disponible)}  
    \end{aligned}$$
    
* **Suposiciones Aplicadas**:
    
    * **Proporcionalidad**: Si producimos una unidad adicional de $P1$, el beneficio se incrementa en $30 y el tiempo de trabajo usado se incrementa en 2 horas.
    * **Aditividad**: El beneficio total es la suma de los beneficios de $P1$ y $P2$. Similarmente, el uso total de recursos es la suma del uso individual por $P1$ y $P2$.
    * **Divisibilidad**: Podemos producir fracciones de unidades de $P1$ y $P2$, como $P1 = 3.5$ y $P2 = 4.2$.
    * **Certeza**: Los coeficientes $30$, $40$, $2$, $1$, $100$, $1$ y $2$ son todos conocidos y constantes.

### Variable de decisión
**$x_i$**: Variables que representan las cantidades que se van a determinar para optimizar la función objetivo. **Ejemplo**: En un problema de producción, $x_1$ y $x_2$ pueden representar el número de unidades de producto 1 y producto 2 a producir.

### Función objetivo
**$z = \mathbf{c}\mathbf{x}$**: es una combinación lineal de las variables de decisión ponderadas por sus respectivos coeficientes. El objetivo es minimizar o mazimizar esta función. **Ejemplo**: $Z = 3x_1 + 4x_2$ representa la ganancia total que se desea maximizar.

Tambien se le puede llamar **función de costo** o **función de beneficio**, según si el objetivo es minimizar o maximizar.

**¿Cuál es el costo para la base $\mathbf{B}$?**

$$
\begin{aligned}
z = \mathbf{c}\mathbf{x} \quad &= \quad \mathbf{c}_{BV} \mathbf{x}_{BV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \left(\mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} \right) + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} + \left(\mathbf{c}_{BV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{B}\right) \mathbf{x}_{BV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{A}\right) \mathbf{x}
\end{aligned}
$$

Define $\Pi = \mathbf{c}_{BV} \mathbf{B}^{-1}$ como los multiplicadores del método simplex

$$\mathbf{c}\mathbf{x} = \Pi \mathbf{b} + \left(\mathbf{c} - \Pi \mathbf{A}\right) \mathbf{x}$$

### Restricciones
**$a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n = b_m$**: son un conjunto de ecuaciones o inecuaciones lineales que limitan los valores que pueden tomar las variables de decisión. **Ejemplo**: $2x_1 + x_2 \leq 100$ puede representar una restricción de disponibilidad de recursos.

* $\geq$: Las restricciones de mayor o igual en los enunciados se presentan con frases como:
  * "al menos"
  * "como mínimo"
  * "no menos de"
  * "no inferior a"
* $\leq$: Las restricciones de menor o igual en los enunciados se presentan con frases como:
  * "a lo sumo"
  * "como máximo"
  * "no más de"
  * "no superior a"
* $=$: Las restricciones de igualdad en los enunciados se presentan con frases como:
  * "exactamente"
  * "igual a"
  * "debe ser"
  * "se requiere"
* $\geq$ y $\leq$: Las restricciones de rango en los enunciados se presentan con frases como:
  * "entre"
  * "en el rango de"
  * "debe estar entre"
  * "no menos de" y "no más de"

#### Restricciones activas
Son aquellas restricciones que se cumplen como igualdad en la solución óptima.

### Coeficientes de Función Objetivo ("Costos")
<aside>
💡 La literatura parte de los problemas de minimización, de ahí que se suele utilizar el término *costos* para referirse a los coeficientes
</aside>

$c_i$: Números constantes que multiplican a las **variables de decisión** en la **función objetivo**. Representan los costos o beneficios unitarios asociados con esas variables. Estos coeficientes determinan cómo cada variable afecta el valor total que se está maximizando o minimizando. 

- Problemas de Maximización: representan **beneficios**
- Problemas de Minimización: representan **costos**

### Coeficiente Tecnológico
**$a_i$**, Es el coeficiente que multiplica a la variable de decisión en una restricción. Representa la cantidad de recursos que se requieren para producir una unidad de la variable de decisión. **Ejemplo**: Si $2x_1 + x_2 \leq 100$, entonces $2$ y $1$ son los coeficientes tecnológicos.
**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 267. y Bula, Slides de Programación Lineal: Método Simplex, 2024, p.112.

### Espacio factible
Conjunto de todas las posibles soluciones que satisfacen las restricciones del problema. **Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 54.

### Solución factible
Cualquier conjunto de valores para las variables de decisión que satisface todas las restricciones. **Ejemplo**: $x_1 = 2, x_2 = 1$ puede ser una solución factible si satisface todas las restricciones del problema.

### Solución óptima
Para un problema de **maximización**, una solución óptima de un problema de Programación Lineal (PL) es un punto en la región factible con el mayor valor de la función objetivo. De manera similar, para un problema de **minimización**, una solución óptima es un punto en la región factible con el menor valor de la función objetivo (Winston, Operations Research: Applications and Algorithms, 4th ed., p. 54.).

Un PL puede tener una solución óptima única, no tener solucion (*infeasible*), puede tener multiples soluciones (*alternative optimal solutions*), o puede ser ilimitado (*unbounded*). En el caso de que un PL tenga múltiples soluciones óptimas, todas las soluciones óptimas tendrán el mismo valor de la función objetivo. (Winston, Operations Research: Applications and Algorithms, 4th ed., p. 113.)

### Restricción de signo
Condición que especifica que una variable debe ser no negativa o sin restricción de signo. **Ejemplo**: $x \geq 0$.

### Forma estándar
<aside>
💡 Necesario para resolver un problema de PL mediante el Método Simplex. 
</aside>
La forma estándar de un problema de programación lineal segun Winston es una representación donde todas las restricciones son igualdades y todas las variables son no negativas. 

$$
\begin{aligned}  
\text{Maximizar} \quad & z = \mathbf{c}^T \mathbf{x} \\  
\text{sujeto a} \quad & \mathbf{A} \mathbf{x} = \mathbf{b} \\  
& \mathbf{x} \geq 0  
\end{aligned}
$$

$$
\begin{aligned}  
\text{Maximizar} \quad & z = c_1x_1 + c_2x_2 + \ldots + c_nx_n \\  
\text{sujeto a} \quad & a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n = b_1 \\  
& a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n = b_2 \\  
& \quad \vdots \\  
& a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n = b_m \\  
& x_i \geq 0 \quad \text{para} \ i = 1, 2, \ldots, n  
\end{aligned}
$$
**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 267.

Un problema de PL está en forma estándar si:

1. **Todas las restricciones son igualdades**:
    
    $$\begin{aligned}  
    a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\  
    a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\  
    &\vdots \\  
    a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m  
    \end{aligned}$$
2. **Todas las variables son no negativas**:
    
    $$x_i \geq 0 \quad \text{para} \quad i = 1, 2, \ldots, n$$
3. **Función objetivo es de maximización o minimización**:
    
    $$\text{Maximizar} \quad z = c_1x_1 + c_2x_2 + \cdots + c_nx_n$$
    
    o
    
    $$\text{Minimizar} \quad z = c_1x_1 + c_2x_2 + \cdots + c_nx_n$$

Para convertir cualquier problema de PL a su forma estándar:

* **Desigualdades a Igualdades**:
    
    * Para cada restricción de tipo "≤" (menor o igual), añade una variable de holgura $+s$.
    * Para cada restricción de tipo "≥" (mayor o igual), resta una variable de exceso $-e$.

* **Variables no restringidas en signo (urs)**:
    
    * Divide cada variable unrestricted ($x_i$) en la diferencia de dos variables no negativas: $x_i = x_i^+ - x_i^-$ donde $x_i^+ \geq 0$ y $x_i^- \geq 0$.

### Variable de holgura $+s$ (Slack Variables)
Variables que se agregan a las restricciones de un problema de programación lineal para convertir las desigualdades tipo **menor o igual** (≤) en igualdades. Su significado es la cantidad de recursos no utilizados, "cantidad no utilizada" o "espacio libre", por lo que la variable se **suma** a la restricción. 

Para una restricción del tipo $\leq$, $x_1$ y $x_2$ pueden llegar hasta un máximo de $b$. Si $x_1 + x_2$ está por debajo de $b$, entonces $s$ representa la "distancia" para llegar a $b$.

**Mnemotecnia**: "Menor o igual a $b_i$: El LHS de la restricción debe ser $b_i$ o estar por debajo de $b_i$. Si está por debajo, $s$ (holgura) es el valor por el cual el LHS está por debajo de $b_i$, y se suma al LHS para alcanzar exactamente $b_i$."

**Ejemplo**: Si la restricción es $a_1x_1 + a_2x_2 \leq b_i$, entonces para alcanzar $b_i$ se suma la holgura: $a_1x_1 + a_2x_2 + s = b_i$.

### Variable de exceso $-e$ (Surplus Variables)
Variables que se agregan a las restricciones de un problema de programación lineal para convertir las desigualdades tipo **mayor o igual** "≥" en igualdades. Su significado es la cantidad de recursos excedidos o "cantidad por encima", por lo que la variable se **resta** de la restricción. 

Para una restricción del tipo $\geq$, $x_1$ y $x_2$ deben ser al menos $b$. Si $x_1 + x_2$ está por encima de $b$, $e$ representa el "exceso" por encima de $b$.
    
**Mnemotecnia**: "Mayor o igual a $b_i$: El LHS de la restricción debe ser $b_i$ o estar por encima de $b_i$. Si se pasa de $b_i$, $e$ (exceso) es el valor por el cual el LHS se pasó de $b_i$, y se resta del LHS para llevarlo a $b_i$."

**Ejemplo**: Si la restricción es $a_1x_1 + a_2x_2 \geq b_i$, entonces para alcanzar $b_i$ se resta el exceso: $a_1x_1 + a_2x_2 - e = b_i$.

### Forma Canónica
La forma canónica de un problema de programación lineal en el contexto de las clases del profesor Bula, una representación estándar del problema de optimización, que varía según se trate de un problema de minimización o maximización.

**Para el caso de la forma canónica de minimización:**

* La función objetivo es minimizada.
* Las restricciones son de tipo *mayor o igual* ($\geq$).
* Las variables de decisión son no negativas.

$$
\text{Minimizar} \quad z = c_1x_1 + c_2x_2 + \cdots + c_nx_n \\
\text{Sujeto a:} \\
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \geq b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \geq b_2 \\
\vdots  \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \geq b_m \\
x_1, x_2, \dots, x_n \geq 0
$$

**Para el caso de la forma canónica de maximización:**

* La función objetivo debe ser de maximización.
* Las variables de decisión no negativas.
* Las restricciones son del tipo *menor o igual* ($\leq$).

$$
\text{Maximizar} \quad z = c_1x_1 + c_2x_2 + \cdots + c_nx_n \\
\text{Sujeto a:} \\
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \leq b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \leq b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \leq b_m \\
x_1, x_2, \dots, x_n \geq 0
$$

**Cambio de signo en las restricciones**

Si tienes una restricción del tipo $\sum a_i x_i \leq b$, puedes multiplicar ambos lados de la inecuación por $-1$ para convertirla en una forma $\geq$: $-\sum a_i x_i \geq -b$
    
**Memotécnia**: *Min max, max min*: En forma canónica el modelo del PL la...
* minimización es mayor.
* maximización es menor.

### Forma Aumentada

es una representación extendida de un problema de programación lineal que incluye tanto la función objetivo como las restricciones en una sola matriz, junto con las variables de decisión, las variables de holgura, exceso y artificiales, y las restricciones de no negatividad. Esta forma es útil para el Método Simplex, ya que facilita la manipulación de las restricciones y la función objetivo en un único sistema de ecuaciones.

$$
\begin{aligned}
&\text{Maximizar } z \text{ en:}
\\
&\begin{pmatrix}  
1 & -\mathbf{c}^T & 0 \\  
0 & \mathbf{A} & \mathbf{I}  
\end{pmatrix}  
\begin{pmatrix}  
z \\  
\mathbf{x} \\  
\mathbf{x}_s  
\end{pmatrix}  
 =  
\begin{pmatrix}  
0 \\  
\mathbf{b}  
\end{pmatrix}
\\
& \mathbf{x}, \mathbf{x}_s \geq 0
\end{aligned}
$$

**Referencia**: Bula, Slides de Programación Lineal: Método Simplex, 2024, p. 6.

El sistema de ecuaciones en forma aumentada se estructura de la siguiente manera:

* La primera fila de la matriz aumentada representa la función objetivo $z$.
    
    $$\begin{pmatrix}  
    1 & -\mathbf{c}^T & 0  
    \end{pmatrix}  
    \begin{pmatrix}  
    z \\  
    \mathbf{x} \\  
    \mathbf{x}_s  
    \end{pmatrix}  
    = 0$$

* Las siguientes filas representan las restricciones del problema con las variables originales $\mathbf{x}$ y las variables de holgura $\mathbf{x}_s$.
    
    $$\begin{pmatrix}  
    0 & \mathbf{A} & \mathbf{I}  
    \end{pmatrix}  
    \begin{pmatrix}  
    z \\  
    \mathbf{x} \\  
    \mathbf{x}_s  
    \end{pmatrix}  
    = \mathbf{b}$$

**Componentes del Modelo**

* **$\mathbf{c}$**: Vector de coeficientes de la función objetivo.
    
    $$\mathbf{c} = [c_1 \; c_2 \; \cdots \; c_n]$$

* **$\mathbf{x}$**: Vector de variables de decisión originales.
    
    $$\mathbf{x} = \begin{pmatrix}  
    x_1 \\  
    x_2 \\  
    \vdots \\  
    x_n  
    \end{pmatrix}$$

* **$\mathbf{x}_s$**: Vector de variables de holgura.
    
    $$\mathbf{x}_s = \begin{pmatrix}  
    s_1 \\  
    s_2 \\  
    \vdots \\  
    s_m  
    \end{pmatrix}$$

* **$\mathbf{A}$**: Matriz de coeficientes de las restricciones.
    
    $$\mathbf{A} = \begin{pmatrix}  
    a_{11} & a_{12} & \cdots & a_{1n} \\  
    a_{21} & a_{22} & \cdots & a_{2n} \\  
    \vdots & \vdots & \ddots & \vdots \\  
    a_{m1} & a_{m2} & \cdots & a_{mn}  
    \end{pmatrix}$$

* **$\mathbf{I}$**: Matriz identidad que representa las variables de holgura.
    
    $$\mathbf{I} = \begin{pmatrix}  
    1 & 0 & \cdots & 0 \\  
    0 & 1 & \cdots & 0 \\  
    \vdots & \vdots & \ddots & \vdots \\  
    0 & 0 & \cdots & 1  
    \end{pmatrix}$$

* **$\mathbf{b}$**: Vector del lado derecho de las restricciones.
    
    $$\mathbf{b} = \begin{pmatrix}  
    b_1 \\  
    b_2 \\  
    \vdots \\  
    b_m  
    \end{pmatrix}$$

* **$\mathbf{z}$**: Variable objetivo que se maximiza.

### Método Simplex
Algoritmo de optimización para resolver problemas de programación lineal moviéndose de una solución básica factible a otra. 

### Tableau
Un tableau es una representación tabular utilizada en el método Simplex para resolver problemas de programación lineal. En un tableau, las ecuaciones del problema se organizan en filas y columnas, donde cada fila representa una restricción y cada columna corresponde a una variable (incluyendo variables de holgura y artificiales). La última fila muestra la función objetivo, y se utilizan operaciones elementales de fila para iterativamente ajustar el tableau hacia una solución óptima. El tableau facilita el seguimiento de las soluciones básicas y las operaciones de pivoteo necesarias en el método Simplex.

La tabla en forma canónica de un problema de programación lineal (PL) con $n$ variables de decisión y $m$ restricciones se puede escribir de la siguiente manera:

| Row | Ecuación en forma canónica                                  | Variable Básica |
| --- | ----------------------------------------------------------- | --------------- |
| 0   | $z + \sum_{j=1}^{n} c_j x_j = 0$                            | $z$             |
| 1   | $a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n + s_1 = b_1$ | $s_1$           |
| 2   | $a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n + s_2 = b_2$ | $s_2$           |
| ... | ...                                                         | ...             |
| m   | $a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n + s_m = b_m$ | $s_m$           |

Notaciones:

1. **Fila 0 (Función Objetivo)**: Representa la función objetivo del problema. Los coeficientes $c_j$ corresponden a las variables de decisión $x_j$. El objetivo es maximizar (o minimizar) $z$.
    
2. **Filas 1 a m (Restricciones)**: Cada fila representa una restricción del problema original. Las variables $a_{ij}$ son los coeficientes de las variables de decisión $x_j$ en la restricción $i$-ésima. Las variables de holgura $s_i$ se introducen para convertir las desigualdades en igualdades.
    
3. **Variables Básicas**: Cada fila tiene una variable básica ($s_i$) con coeficiente 1, y todas las demás variables en esa fila tienen coeficientes 0. Las variables básicas $s_i$ tienen valores en el lado derecho de las ecuaciones $b_i$.

### Tableau Óptimo
Es una representación tabular del problema de programación lineal donde se han encontrado los valores óptimos para las variables de decisión y la función objetivo. Este tableau cumple con las siguientes condiciones:

1. **Condición de optimalidad**: Los **costos reducidos** de todas las variables no básicas (NBV) son no negativos en un problema de maximización (o no positivos en un problema de minimización). Esto indica que no hay más mejorías posibles en la función objetivo.

    * En maximización: $\bar{c}_j \geq 0$ para todas las $j$ no básicas.
    * En minimización: $\bar{c}_j \leq 0$ para todas las $j$ no básicas.
  
2. **Condición de factibilidad**: Las soluciones básicas correspondientes a las restricciones deben ser no negativas. Es decir, todas las variables básicas deben ser mayores o iguales a cero.
    
3. **Valor óptimo**: La celda de la función objetivo en el tableau óptimo proporciona el valor máximo o mínimo alcanzado por la función objetivo.

### Prueba de optimalidad

### Solución actual
Una solución actual es aquella que se ha derivado utilizando las variables básicas y no básicas, y puede no ser óptima.

### Solución básica (BS)

La **solución básica (BS)** es simplemente la solución obtenida al fijar las variables no básicas ($\mathbf{x}_{NBV}$) en cero y resolver el sistema resultante para las variables básicas ($\mathbf{x}_{BV}$). Esta solución no necesariamente cumple con las restricciones de no negatividad de las variables básicas, por lo que puede incluir valores negativos.

### Solución básica factible (BFS)
Solución básica que también satisface todas las restricciones del problema PL. 

Se parte del sistema de ecuaciones 
$$
\mathbf{A}\mathbf{x} = \mathbf{b}
$$

La ecuación se descompone como: 
$$
\mathbf{B}\mathbf{x}_{BV} + \mathbf{N}\mathbf{x}_{NBV} = \mathbf{b}
$$
Donde,
* $\mathbf{B}\mathbf{x}_{BV}$ representa la contribución de las variables básicas.
* $\mathbf{N}\mathbf{x}_{NBV}$ representa la contribución de las variables no básicas.

**Solución de las variables básicas:**

Se reescribe la ecuación como: 
$$
\mathbf{B}\mathbf{x}_{BV} = \mathbf{b} - \mathbf{N}\mathbf{x}_{NBV}$$
Al resolver para $\mathbf{x}_{BV}$: 
$$
\mathbf{x}_{BV} = \mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV}
$$
Aquí muestra cómo las variables básicas ($\mathbf{x}_{BV}$) se calculan en función de las variables no básicas ($\mathbf{x}_{NBV}$).

**Condición de factibilidad:**
    
La solución es factible (BFS) si $\mathbf{b}' \geq 0$, es decir, si todas las variables básicas $\mathbf{x}_{BV}$ son no negativas.

1. **$\mathbf{x}_{NBV} = 0$**:
    
    * En la BFS, todas las **variables no básicas** ($\mathbf{x}_{NBV}$) son iguales a cero. Estas variables corresponden a las columnas de la matriz $\mathbf{A}$ que no están incluidas en la base $\mathbf{B}$.
2. **$\mathbf{x}_{BV} \geq 0$**:
    
    * Los valores de las **variables básicas** ($\mathbf{x}_{BV}$), que se obtienen resolviendo el sistema $\mathbf{B}\mathbf{x}_{BV} = \mathbf{b}$, son **no negativos**. Para que la solución sea factible, es necesario que todos los valores de $\mathbf{x}_{BV}$ sean no negativos.

**Notación**: 
* $\bar{\mathbf{x}} = [\bar{\mathbf{x}}_{BV}, \bar{\mathbf{x}}_{NBV}]$ [Winston]
* ${\mathbf{x}^*} = [{\mathbf{x}^*}_{BV}, {\mathbf{x}^*}_{NBV}]$ [Bula]

### Multiplicador Simplex
**¿Cuál es el costo para la base $\mathbf{B}$?**

$$
\begin{aligned}
z = \mathbf{c}\mathbf{x} \quad &= \quad \mathbf{c}_{BV} \mathbf{x}_{BV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \left(\mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} \right) + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} + \left(\mathbf{c}_{BV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{B}\right) \mathbf{x}_{BV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{A}\right) \mathbf{x}
\end{aligned}
$$

Define $\Pi = \mathbf{c}_{BV} \mathbf{B}^{-1}$ como los multiplicadores del método simplex

### Solución Básica Factible Inicial (IBFS):
Se refiere a la primera solución básica factible utilizada como punto de partida para el método simplex. La SBFI se puede obtener de diferentes maneras dependiendo de la forma del problema:

1. Problemas con Restricciones de Igualdad.
2. Problemas con Restricciones de Desigualdad
3. Método de las Dos Fases

### Variables básicas (BV)
$BV = \{BV_1, BV_2, \ldots, BV_m\}$ es un conjunto de $m$ variables (donde $m$ es el número de restricciones) que forman una solución básica factible (BFS) del sistema de ecuaciones asociado. Una varaible BV no está fijada en cero en la solución básica factible (BFS).

### Vector BV
$x_{b}$ (en la literatuva del profesor Bula) o $x_{BV}$ es el vector columna $n \times 1$ $[x_{BV1}, x_{BV2}, \ldots, x_{BVn}]$: son los valores variables básicas VB en la solución básica (BS).

### Coeficientes BV
$\mathbf{c}_{BV}$ es el vector fila $1 \times m$ $[\mathbf{c}_{BV1}, \mathbf{c}_{BV2}, \ldots, \mathbf{c}_{BVn}]$: son los coeficientes de la función objetivo para las variables básicas VB del tableau óptimo.

### Variables no básicas (NBV)
$NBV = \{NBV_1, NBV_2, \ldots, NBV_{n-m}\}$ es un conjunto de $n-m$ variables que no forman parte de la solución básica factible (BFS) del sistema de ecuaciones asociado. Una varaible NBV está fijada en cero en la solución básica factible (BFS).

### Vector NBV
$x_{n}$ (en la literatuva del profesor Bula) $x_{NBV}$ es el vector columna $n \times 1$ $[x_{NBV1}, x_{NBV2}, \ldots, x_{NBVn}]$: son los valores de las variables no básicas NBV en la solución básica (BS).

### Coeficientes NBV
$\mathbf{c}_{NBV}$ es el vector fila $1 \times (n - m)$ cuyos elementos son los coeficientes de las variables no básicas (en el orden de NBV).

### Matriz básica o Base
Puesto que en $\mathbf{A}$ corresponde una columna para cada variable de decisión $x_i$, la matriz $\mathbf{A_B}$ (en la literatuva del profesor Bula) o  $\mathbf{B}$ ($m \times m$) es una submatriz de $\mathbf{A}$, donde la columna $j$ de $\mathbf{B}$ es la columna de $\mathbf{A}$ correspondiente a la variable básica $x_{BV_j}$. En otras palabras, $\mathbf{B}$ es una matriz cuadrada formada por las columnas de $\mathbf{A}$ correspondientes a las variables básicas BV.

Una variable **entra en la base** durante el proceso del método simplex cuando se selecciona una variable no básica (NBV) $x_j$ para que aumente desde cero y se convierta en una variable básica (BV). Esto implica que una de las variables básicas actuales debe salir de la base para mantener el número de variables básicas igual al número de restricciones.

### Matriz no básica
La matriz $\mathbf{A_N}$ (en la literatuva del profesor Bula) o $\mathbf{N}$ ($m \times (n - m)$) es una submatriz de $\mathbf{A}$, donde la columna $j$ de $\mathbf{N}$ es la columna de $\mathbf{A}$ correspondiente a la variable no básica $x_{NBV_j}$. En otras palabras, $\mathbf{N}$ es una matriz formada por las columnas de $\mathbf{A}$ correspondientes a las variables no básicas NBV.

### Partición de A
$$\mathbf{A} = [\mathbf{B} \quad \mathbf{N}]$$
Donde $\mathbf{B}$ es una matriz $m \times m$ formada por las columnas de $\mathbf{A}$ correspondientes a las variables básicas (BV), y $\mathbf{N}$ es una matriz $m \times (n-m)$ formada por las columnas correspondientes a las variables no básicas (NBV).

### Inversa de la Base
Expresando las restricciones en cualquier tableau en términos de $B^{-1}$ y el PL original

**Función Objetivo:**

$$z = \mathbf{c}_{BV} \mathbf{x}_{BV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV}$$

**Restricciones:**

$$\mathbf{B} \mathbf{x}_{BV} + \mathbf{N} \mathbf{x}_{NBV} = \mathbf{b}$$

**No negatividad:**

$$\mathbf{x}_{BV}, \mathbf{x}_{NBV} \geq 0$$

Multiplicando las restricciones por $\mathbf{B}^{-1}$, obtenemos:

$$
\mathbf{B}^{-1} \mathbf{B} \mathbf{x}_{BV} + \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} = \mathbf{B}^{-1} \mathbf{b}
$$

o

$$
\mathbf{x}_{BV} + \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} = \mathbf{B}^{-1} \mathbf{b}
$$

En donde $\mathbf{BV}_i$ ocurre con un coeficiente de 1 en la i-ésima restricción y un coeficiente de cero en cada otra restricción. Así, $\mathbf{BV}$ es el conjunto de variables básicas, y proporciona las restricciones para el tableau óptimo.

Podemos obtener una solución básica factible (BFS) a partir de la inversa de la base $\mathbf{B}^{-1}$ y el vector $\mathbf{b}$. Reorganizamos la ecuación para resolver $\mathbf{x}_{BV}$ en términos de $\mathbf{x}_{NBV}$.

$$
\mathbf{x}_{BV} = \mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV}
$$

La solución $\mathbf{x}_{BV}$ es factible si $\mathbf{b}' \geq 0$, donde $\mathbf{b}' = \mathbf{B}^{-1} \mathbf{b}$.
   
$$\mathbf{B} \mathbf{x}_{BV} = \mathbf{b}' - \mathbf{N}' \mathbf{x}_{NBV}$$

Si $\mathbf{b}' \geq 0$, la solución es una BFS.

**Determinando la Fila 0 del Tableau Óptimo en Términos del PL Inicial**

Para comenzar, multiplicamos las restricciones (expresadas en la forma $\mathbf{B}\mathbf{x}_{BV} + \mathbf{N}\mathbf{x}_{NBV} = \mathbf{b}$) por el vector $\mathbf{c}_{BV}\mathbf{B}^{-1}$:

$$
\begin{aligned}
\mathbf{B}\mathbf{x}_{BV} + \mathbf{N}\mathbf{x}_{NBV} &= \mathbf{b}\\
\mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{B}\mathbf{x}_{BV} + \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} &= \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b}\\
\mathbf{c}_{BV}\mathbf{x}_{BV} + \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} &= \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b} \\
\mathbf{c}_{BV}\mathbf{x}_{BV} + \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} - \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b} &= 0 
\end{aligned}

$$

y reescribimos la función objetivo original, $z = \mathbf{c}_{BV}\mathbf{x}_{BV}$, sustituyendo $\mathbf{x}_{BV} = \mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV}$, como

$$
\begin{aligned}
z &= \mathbf{c}_{BV}\mathbf{x}_{BV} \\
z &= \mathbf{c}_{BV}(\mathbf{B}^{-1}\mathbf{b} - \mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV}) \\
z &= \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b} - \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} = 0 \\

z - \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b} + \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} &= 0
\end{aligned}
$$

podemos eliminar las variables básicas del tableau óptimo y obtener su fila 0:

$$
\begin{aligned}

z &=\mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b} - \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} + \mathbf{c}_{NBV}\mathbf{x}_{NBV}
\\
z + \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N}\mathbf{x}_{NBV} - \mathbf{c}_{NBV}\mathbf{x}_{NBV} &= \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b}
\\
z + (\mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{N} - \mathbf{c}_{NBV})\mathbf{x}_{NBV} &= \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b}
\end{aligned}
$$

el coeficiente de $x_j$ en la fila 0 es

$$\mathbf{c}_{BV}\mathbf{B}^{-1} (\text{columna de } \mathbf{N} \text{ para } x_j) - (\text{coeficiente de } x_j \text{ en } \mathbf{c}_{NBV}) = \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{a}_j - c_j$$

y el lado derecho de la fila 0 es $\mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b}$.

Para ayudar a resumir la discusión anterior, dejemos que $\tilde{c}_j$ sea el coeficiente de $x_j$ en la fila 0 del tableau óptimo. Entonces hemos mostrado que

$$\tilde{c}_j = \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{a}_j - c_j$$

y

$$\text{Lado derecho de la fila 0 del tableau óptimo} = \mathbf{c}_{BV}\mathbf{B}^{-1}\mathbf{b}$$

### Multiplicador Simplex $\Pi$, Precio Sombra de la i-ésima restricción o Valor Dual
Valor que indica cuánto cambiaría la función objetivo por una unidad adicional del RHS de una restricción. 

> El **precio sombra** de la i-ésima restricción es la cantidad en la que el valor óptimo de $z$ mejora (aumenta en un problema de maximización y disminuye en un problema de minimización) si incrementamos $b_i$ en 1 (de $b_i$ a $b_i + 1$).

**Ejemplo**: Si el precio sombra de una restricción es 2, agregar una unidad al RHS de esa restricción incrementará la función objetivo en 2 unidades.

**¿Cuál es el costo para la base $\mathbf{B}$?**

$$
\begin{aligned}
z = \mathbf{c}\mathbf{x} &= \quad \mathbf{c}_{BV} \mathbf{x}_{BV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \left(\mathbf{B}^{-1} \mathbf{b} - \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} \right) + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N} \mathbf{x}_{NBV} + \mathbf{c}_{NBV} \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c}_{NBV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{N}\right) \mathbf{x}_{NBV} + \left(\mathbf{c}_{BV} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{B}\right) \mathbf{x}_{BV} \\
\quad &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{A}\right) \mathbf{x}
\end{aligned}
$$

Define $\Pi = \mathbf{c}_{BV} \mathbf{B}^{-1}$ como los multiplicadores del método **simplex**

Probar que una base es óptima, es verificar que
$$
\begin{aligned}
z = \mathbf{c}\mathbf{x} &= \quad \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{b} + \left(\mathbf{c} - \mathbf{c}_{BV} \mathbf{B}^{-1} \mathbf{A}\right) \mathbf{x} \\
z = \mathbf{c}\mathbf{x} &= \quad \Pi \mathbf{b} + \left(\mathbf{c} - \Pi \mathbf{A}\right) \mathbf{x}
\end{aligned}
$$

### Dualidad
Dado un primal
$$
\begin{aligned}
&\text{max} \quad z = \mathbf{c}^T \mathbf{x} \\
&\text{s. a.} \\
&\mathbf{A}\mathbf{x} \leq \mathbf{b} \\
&\mathbf{x} \geq 0
\end{aligned}
$$

Donde
* $\mathbf{c}$ es un vector de costos de las variables de decisión de dimensión $n$.
* $\mathbf{x}$ es un vector de variables de decisión de dimensión $n$.
* $\bar{\mathbf{x}}$ es vector de variables de la BFS.
* $\mathbf{A}$ es una matriz de restricciones de dimensión $m \times n$.
* $\mathbf{b}$ es un vector de RHS de las restricciones de dimension $m$.

El dual es
$$
\begin{aligned}
&\text{min} \quad w = \mathbf{b}^T \mathbf{y} \\
&\text{s. a.} \\
&\mathbf{A}^T\mathbf{y} \geq \mathbf{c} \\
&\mathbf{y} \geq 0
\end{aligned}
$$

Donde
* $\mathbf{y}$ es un vector de variables duales de dimensión $m$.
* $\bar{\mathbf{y}}$ es vector de variables de la BFS.
* $\mathbf{b}$ ahora es un vector de restricciones.
* $\mathbf{A}^T$ es la transpuesta de la matriz de restricciones.
* $\mathbf{c}$ es ahora el RHS de las restricciones de dimensión $n$.

**Propiedades de la dualidad**

### Costo marginal (Marginal Cost) de NBV
Cambio en la función objetivo por una unidad adicional de una variable de decisión. **Ejemplo**: Si el costo marginal de $x_1$ es 3, entonces incrementar $x_1$ en una unidad incrementará la función objetivo en 3.

### Costo Reducido (Reduced Cost) de NBV
Diferencia entre el costo marginal de una variable y su contribución a la función objetivo en una solución básica factible. 

Indica cuánto cambiaría la función objetivo si se incrementa una unidad de una variable no básica (NBV).

El costo reducido de una variable no básica (NBV) en una solución básica factible (BFS) es la cantidad en que el coeficiente de la variable en la función objetivo tendría que mejorar (aumentar en maximización o disminuir en minimización) antes de que esa variable entre en la **base**.

En términos más simples, el costo reducido indica cuánto afectaría el valor de la función objetivo si aumentamos una variable no básica desde cero.

- En problemas de **maximización**, un costo reducido positivo sugiere que aumentar esa variable aumentaría el valor de la función objetivo.
- En problemas de **minimización**, un costo reducido negativo sugiere que aumentar esa variable disminuiría el valor de la función objetivo.

$$
\bar{c}_j = \mathbf{c}_{BV} \mathbf{A_B}^{-1} \mathbf{a}_j - c_j
$$


### Holgura
Diferencia entre el lado izquierdo y derecho de una restricción cuando se evalúa en la solución óptima. **Ejemplo**: Si la restricción es $2x + 3y \leq 10$ y en la solución óptima $2x + 3y = 8$, la holgura es 2.

## Teoremas y Lemas Fundamentales en Programación Lineal

### Lema 1 Dualidad Débil (Weak Duality)

Sea

$$\mathbf{x} = \begin{bmatrix}  
x_1 \\  
x_2 \\  
\vdots \\  
x_n  
\end{bmatrix}$$

cualquier solución factible para el problema primal y

$$\mathbf{y} = [y_1 \; y_2 \; \cdots \; y_m]$$

cualquier solución factible para el problema dual. Entonces (valor z para $\mathbf{x}$) $\leq$ (valor w para $\mathbf{y}$).

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 305.

### Lema 2

Sea

$$\bar{\mathbf{x}} = \begin{bmatrix}  
\bar{x}_1 \\  
\bar{x}_2 \\  
\vdots \\  
\bar{x}_n  
\end{bmatrix}$$

cualquier solución factible para el problema primal y

$$\mathbf{y} = [y_1 \; y_2 \; \cdots \; y_m]$$

cualquier solución factible para el problema dual. Si $\mathbf{c} \bar{\mathbf{x}} = \mathbf{y} \mathbf{b}$, entonces $\bar{\mathbf{x}}$ es óptima para el problema primal y $\mathbf{y}$ es óptima para el problema dual.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Lema 3

> Si el primal es ilimitado, entonces el problema dual es infactible.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Lema 4

> Si el dual es ilimitado, entonces el primal es infactible.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Lemma 5

Si el problema primal tiene una solución óptima finita, entonces el problema dual también tiene una solución óptima finita, y sus valores óptimos son iguales.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### Lemma 6

Si el problema dual tiene una solución óptima finita, entonces el problema primal también tiene una solución óptima finita, y sus valores óptimos son iguales.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### Teorema de la Dualidad
> Supongamos que $BV$ es una base óptima para el primal. Entonces $\mathbf{c}_{BV} \mathbf{B}^{-1}$ es una solución óptima para el dual. Además, $\bar{z} = \bar{w}$.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 308.

Donde,
* **$\mathbf{c}_{BV}$**: Es el vector de costos asociado con las variables básicas (BV) en el problema primal.
* **$\mathbf{B}^{-1}$**: Es la inversa de la matriz de restricciones asociada con las variables básicas en el problema primal.
* **$\bar{z}$**: Es el valor óptimo de la función objetivo del problema primal.
* **$\bar{w}$**: Es el valor óptimo de la función objetivo del problema dual.


El teorema de la dualidad establece que si $\mathbf{c}_{BV}$ es el vector de costos asociado con las variables básicas en el problema primal y $\mathbf{B}$ es la matriz de restricciones asociada con las variables básicas en el problema primal, entonces $\mathbf{c}_{BV} \mathbf{B}^{-1}$ proporciona una solución óptima para el problema dual. Esto implica que los costos de las variables básicas en el primal se pueden transformar a través de la inversa de la matriz de restricciones para encontrar los valores duales correspondientes.

**Resumen**: Si un problema de programación lineal (primal) tiene una solución óptima, entonces el problema dual también tiene una solución óptima, y los valores óptimos de ambos problemas son iguales.
    
**Implicación**: Permite verificar la optimalidad y proporciona información sobre los precios sombra.

### Teorema de Holgura Complementaria

> $$y_i (b_i - \mathbf{a}_i \mathbf{x}) = 0 \quad \text{y} \quad x_j (c_j - \mathbf{a}_j^T \mathbf{y}) = 0$$
> Para cada par de variables duales y primales asociadas, al menos una de ellas debe ser cero en la solución óptima.
   
**Implicación**: Si una restricción tiene holgura en la solución óptima, entonces su precio sombra es cero, y viceversa.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 301.

El **Teorema de Complementariedad** establece que, para cada par de problemas primal y dual, si $\mathbf{x}^*$ es una solución óptima para el primal y $\mathbf{y}^*$ es una solución óptima para el dual, entonces:

$$y_j^* (\mathbf{a}_j^T \mathbf{x}^* - b_j) = 0 \quad \text{para cada } j \text{ en el dual}$$

y

$$x_i^* (c_i - \mathbf{a}_i^T \mathbf{y}^*) = 0 \quad \text{para cada } i \text{ en el primal}$$

Este teorema nos dice que para cada restricción en el problema primal, el valor dual correspondiente será cero a menos que la restricción sea activa (es decir, que se cumpla con igualdad). Similarmente, para cada variable primal, el valor de la variable será cero a menos que la desigualdad correspondiente en el dual sea activa.

**Memotecnia**: $y_j^* del dual será 0 si la restricción $j$ del primal no es activa (no se cumple en igualdad).

### Teorema de la Dualidad Fuerte

$$Z_{\text{primal}} = W_{\text{dual}}$$

Si el problema primal tiene una solución óptima finita, entonces el problema dual también tiene una solución óptima finita, y sus valores óptimos son iguales.
    
**Implicación**: Refuerza la validez del Teorema Fundamental de la Dualidad.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### Teorema de la Dualidad Débil

$$W_{\text{dual}} \leq Z_{\text{primal}}$$

Si $\mathbf{x}$ es una solución factible para el problema primal y $\mathbf{y}$ es una solución factible para el problema dual, entonces el valor de la función objetivo del dual es siempre menor o igual al valor de la función objetivo del primal.
    
**Implicación**: Establece una cota inferior para el valor óptimo del problema primal y una cota superior para el valor óptimo del problema dual.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### Teorema de Factibilidad Primal

Si existe una solución factible para el problema primal, entonces existe una solución factible para el problema dual.

**Implicación**: Garantiza que la búsqueda de soluciones en el problema dual es válida siempre que haya soluciones en el problema primal.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Teorema de Factibilidad Dual

Si existe una solución factible para el problema dual, entonces existe una solución factible para el problema primal.

**Implicación**: Similar al teorema anterior, pero en el sentido inverso.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Teorema de la Optimalidad del Simplex

$$\bar{c}_j \geq 0 \quad \forall j \quad \text{(para maximización)}$$ 
$$\bar{c}_j \leq 0 \quad \forall j \quad \text{(para minimización)}$$

Una solución básica factible es óptima si y solo si todos los costos reducidos son no negativos en un problema de maximización (o no positivos en un problema de minimización).

**Implicación**: Permite verificar la optimalidad de una solución básica factible en el método Simplex.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 146.

### Teorema de la Degeneración

Si una solución básica factible tiene más de una variable básica igual a cero, se dice que la solución es degenerada.

**Implicación**: La degeneración puede causar ciclos en el método Simplex, afectando la eficiencia del algoritmo.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 168.

## Preguntas y Respuestas Clave en Programación Lineal

### Qué pasa con el dual si el costo sombra de una variable es 0?
Si el costo sombra de una variable en el primal es 0, esto significa que la restricción correspondiente en el dual no tiene holgura y no contribuye al valor de la función objetivo del dual. Esto puede implicar que la restricción es redundante en el contexto del problema dual.

### ¿Qué pasa si el primal y el dual tienen el mismo valor óptimo?
Según el Teorema de Dualidad Fuerte, si ambos, el primal y el dual tienen soluciones óptimas, sus valores óptimos son iguales. Esto implica que las soluciones son viables y que se ha alcanzado la óptima eficiencia de recursos.

### ¿Cómo se hace para saber si un problema tiene múltiples soluciones?
Un problema de programación lineal tiene múltiples soluciones óptimas si en la última iteración del método simplex, una variable no básica tiene un costo reducido de cero. Esto indica que hay una dirección en la que se puede mover sin cambiar el valor de la función objetivo, lo que resulta en múltiples soluciones óptimas.

### ¿Qué pasa con el dual si el costo sombra de una variable es 0?
Si el costo sombra (precio dual) de una variable en el primal es 0, esto significa que la restricción correspondiente en el dual no tiene holgura (es decir, la restricción es exactamente una igualdad en la solución óptima). Esto implica que el recurso adicional no afecta el valor de la función objetivo del dual.

### ¿Qué significa el precio sombra de una restricción?
El precio sombra de una restricción indica cuánto cambiará el valor de la función objetivo si se incrementa el lado derecho de la restricción en una unidad, manteniendo todo lo demás constante. En otras palabras, mide la sensibilidad del valor óptimo a cambios en la disponibilidad del recurso correspondiente.

### ¿Cómo afectan los cambios en los valores del RHS a la solución óptima?
Los cambios en los valores del RHS afectan la solución óptima dentro de ciertos rangos. Si el cambio está dentro del rango permisible del RHS, la base óptima no cambiará. Si el cambio está fuera de este rango, será necesario resolver nuevamente el problema para encontrar la nueva solución óptima.

### ¿Qué indican los rangos permisibles de los coeficientes de la función objetivo?
Los rangos permisibles de los coeficientes de la función objetivo indican cuánto pueden variar los coeficientes de las variables en la función objetivo antes de que la base óptima cambie. Dentro de estos rangos, la solución óptima permanece la misma, aunque el valor de la función objetivo puede cambiar.

### ¿Qué implica la factibilidad del dual para la solución del primal?
Si el problema primal tiene una solución factible y acotada, el dual también tendrá una solución factible y acotada, y viceversa. Si uno de los problemas es no acotado o no tiene solución factible, el otro tampoco la tendrá.

### ¿Qué implica la holgura complementaria en soluciones óptimas?
La holgura complementaria establece que en las soluciones óptimas del primal y el dual, el producto de cada variable primal y su correspondiente restricción dual debe ser cero. Esto significa que si una variable primal es positiva, la restricción dual correspondiente es una igualdad, y si una restricción primal tiene holgura, la variable dual correspondiente es cero.

### ¿Qué condiciones deben cumplir las soluciones óptimas del primal y el dual según las condiciones de optimalidad KKT?
Las condiciones KKT establecen que una solución \(x^*\) del primal y \(y^*\) del dual son óptimas si cumplen:
1. **Viabilidad Primal**: \(x^*\) cumple todas las restricciones del primal.
2. **Viabilidad Dual**: \(y^*\) cumple todas las restricciones del dual.
3. **Holgura Complementaria**: \(x_i^* \cdot (Ax - b)_i = 0\) para todas las \(i\).
4. **No Negatividad**: Todas las variables son no negativas en sus respectivos dominios.

### ¿Cómo se determina si se debe introducir una nueva variable (producto) en el modelo?
Para determinar si se debe introducir una nueva variable, se calcula su costo reducido (\(\bar{c}_j\)). Si el costo reducido es negativo en un problema de maximización, o positivo en un problema de minimización, entonces la introducción de esta variable mejorará el valor de la función objetivo y debe ser incluida en la solución.

### ¿Para convertir a la forma estándar, el tipo de variabla de holgura (exceso o holgura) depende del tipo de restricción y de si es minimización o maximización?
No, el tipo de variable de holgura (exceso o holgura) **no** depende de si el problema es de **minimización** o **maximización**. Depende únicamente del tipo de restricción que se esté tratando:

- **\(\leq\) ** → **Variable de holgura \(s\)** (se suma para convertir la desigualdad en igualdad).
- **\(\geq\) ** → **Variable de exceso \(e\)** (se resta para convertir la desigualdad en igualdad).
- **\(=\)** → No requiere variables adicionales para convertir a la forma estándar. 

Por lo tanto, la selección de una variable de holgura o de exceso es independiente del objetivo del problema (ya sea minimización o maximización) y está únicamente determinada por el tipo de desigualdad en las restricciones.


