## Definición de Función Lineal

Una **función lineal** $f(x_1, x_2, \ldots, x_n)$ de las variables $x_1, x_2, \ldots, x_n$ es una función que se puede expresar en la forma:

$$f(x_1, x_2, \ldots, x_n) = c_1 x_1 + c_2 x_2 + \cdots + c_n x_n$$

donde $c_1, c_2, \ldots, c_n$ son constantes.

En otras palabras, una función lineal es una combinación lineal de sus variables, es decir, cada variable está multiplicada por una constante y estas constantes se suman.

**Ejemplo de función lineal:** $f(x_1, x_2) = 2x_1 + x_2$ Aquí, $c_1 = 2$ y $c_2 = 1$. La función es una combinación lineal de $x_1$ y $x_2$.

**Ejemplo de función no lineal:** $f(x_1, x_2) = x_1^2 x_2$ Esta función no es lineal porque involucra el producto y el cuadrado de las variables $x_1$ y $x_2$.

## Definición de Desigualdades Lineales

Para cualquier función lineal $f(x_1, x_2, \ldots, x_n)$ y cualquier número $b$, las desigualdades:

$$f(x_1, x_2, \ldots, x_n) \leq b \quad \text{y} \quad f(x_1, x_2, \ldots, x_n) \geq b$$

se llaman **desigualdades lineales**.

Esto significa que si tienes una función lineal y estableces una desigualdad en relación con un número $b$, esa desigualdad es una desigualdad lineal.

**Ejemplos de desigualdades lineales:** $2x_1 + 3x_2 \leq 3$ $2x_1 + x_2 \geq 3$

Ambas son desigualdades lineales porque la función en cada caso es lineal.

**Ejemplo de desigualdad no lineal:** $x_1^2 x_2 \geq 3$

Esta no es una desigualdad lineal porque la función involucra productos y potencias de las variables.

En resumen, una función es lineal si es una suma ponderada de sus variables, y una desigualdad es lineal si esa función lineal se compara con un número mediante una desigualdad.

## Definición de Problema de Programación Lineal (LP)

Un **problema de programación lineal (LP)** es un problema de optimización en el que se realizan las siguientes acciones:

1. **Maximizar o minimizar una función lineal de las variables de decisión:**
    
    * La función que se intenta maximizar o minimizar se llama **función objetivo**.
    * Una función lineal de las variables de decisión significa que cada variable está multiplicada por una constante y estas constantes se suman.
2. **Las variables de decisión deben satisfacer un conjunto de restricciones:**
    
    * Los valores de las variables de decisión están sujetos a un conjunto de **restricciones**.
    * Cada restricción debe ser una **ecuación lineal** o una **desigualdad lineal**.
3. **Una restricción de signo está asociada a cada variable:**
    
    * Para cualquier variable $x_i$, la restricción de signo especifica que $x_i$ debe ser **no negativa** ($x_i \geq 0$) o **sin restricción de signo** (urs, del inglés "unrestricted in sign").

### Desglose de los Componentes

* **Función Objetivo:** Es la función lineal que se quiere maximizar o minimizar. Ejemplo: $\text{Maximizar } Z = c_1 x_1 + c_2 x_2 + \cdots + c_n x_n$
    
* **Restricciones:** Son las condiciones que las variables de decisión deben cumplir, y pueden ser igualdades o desigualdades lineales. Ejemplo: $a_1 x_1 + a_2 x_2 \leq b$
    
* **Restricción de Signo:** Especifica que las variables de decisión deben ser no negativas o pueden ser sin restricción de signo. Ejemplo: $x_i \geq 0$
    

### Ejemplo de un Problema de Programación Lineal

Supongamos que queremos maximizar el beneficio ($Z$) de producir dos productos $x_1$ y $x_2$, dados ciertos recursos limitados:

* **Función Objetivo:** Maximizar el beneficio: $Z = 3x_1 + 2x_2$
    
* **Restricciones:** $x_1 + 2x_2 \leq 100 \quad (\text{restricción de recursos})$ $2x_1 + x_2 \leq 80 \quad (\text{otra restricción de recursos})$
    
* **Restricción de Signo:** $x_1, x_2 \geq 0$
    

En este ejemplo, buscamos los valores de $x_1$ y $x_2$ que maximizan el beneficio $Z$, cumpliendo con las restricciones de recursos y la restricción de signo.

Esta definición y estructura permiten formular y resolver problemas de programación lineal de manera sistemática y eficiente usando métodos como el Simplex.****