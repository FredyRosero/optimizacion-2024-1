# Suposiciones en Programación Lineal

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

## Suplemento: Ejemplo de Aplicación de Suposiciones

### Problema de Mezcla de Productos

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