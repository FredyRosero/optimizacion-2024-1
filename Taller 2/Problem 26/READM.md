Voy a asegurarme de que todas las ecuaciones estén correctamente formateadas utilizando \( \$ \) para las ecuaciones en línea y \( \$\$ \) para las ecuaciones en bloque. Aquí tienes la explicación corregida:

### Costo en Programación Lineal

1. **Costo en la Función Objetivo**

En un problema de programación lineal, la función objetivo puede representar un beneficio o un costo.

#### Ejemplo:

Para un problema de minimización:

$$ \text{Minimizar} \quad Z = 2x_1 + 3x_2 $$

Aquí, los coeficientes 2 y 3 representan los costos unitarios asociados con las variables \( x_1 \) y \( x_2 \), respectivamente. El objetivo es minimizar el costo total \( Z \).

2. **Costo Reducido (Reduced Cost)**

El costo reducido de una variable es la cantidad que la función objetivo cambiaría si se incrementara esa variable en una unidad, manteniendo las demás variables constantes.

- En problemas de **maximización**, un costo reducido positivo sugiere que aumentar esa variable aumentaría el valor de la función objetivo.
- En problemas de **minimización**, un costo reducido negativo sugiere que aumentar esa variable disminuiría el valor de la función objetivo.

3. **Costo Dual (Precio Sombra)**

El costo dual o precio sombra es el valor asociado con una restricción en el problema primal. Representa el cambio en el valor de la función objetivo por unidad de cambio en el lado derecho de la restricción.

#### Ejemplo:

Si una restricción indica que no se pueden utilizar más de 100 unidades de un recurso, el precio sombra de esa restricción podría indicar cuánto aumentaría el valor óptimo de la función objetivo por cada unidad adicional del recurso permitido.

### Costos en el Contexto de una Solución Básica Factible (BFS)

En una solución básica factible (BFS):

- **Costos Básicos (\( c_B \))**: Son los coeficientes de las variables básicas en la función objetivo.
- **Costos No Básicos (\( c_N \))**: Son los coeficientes de las variables no básicas en la función objetivo.

### Fórmula de Costos en una BFS

La fórmula de la diapositiva \( cx = c_B A_B^{-1} b + (c - c_B A_B^{-1} A)x \) se descompone en:

1. \( c_B A_B^{-1} b \):
   - Representa el costo de la solución asociada con las variables básicas.
   - \( c_B \) son los coeficientes de las variables básicas en la función objetivo.
   - \( A_B \) es la matriz de los coeficientes de las restricciones asociadas a las variables básicas.
   - \( b \) es el vector de los términos constantes en las restricciones.
   - \( A_B^{-1} \) es la inversa de la matriz \( A_B \).

2. \( (c - c_B A_B^{-1} A)x \):
   - Representa los costos reducidos de las variables no básicas.
   - \( c \) son los coeficientes de todas las variables en la función objetivo.
   - \( A \) es la matriz de coeficientes de todas las variables en las restricciones.
   - \( x \) es el vector de todas las variables (básicas y no básicas).

### Determinación de la Optimalidad de una Solución Básica

Para probar si una solución básica es óptima, se verifica si todos los costos reducidos son no negativos:

- La base es óptima si los costos reducidos \( (c - c_B A_B^{-1} A)x \) no son negativos.
- Si algún costo reducido es negativo, la solución no es óptima, y se puede mejorar moviendo una variable no básica con costo reducido negativo a la base.

### Multiplicadores del Simplex

- Los multiplicadores del simplex son valores duales o precios sombra asociados a las restricciones.
- Estos multiplicadores son soluciones al problema dual y proporcionan información adicional sobre las restricciones y la función objetivo.

### Resumen

- **Costo** en la función objetivo: Representa el valor que queremos optimizar (maximizar o minimizar).
- **Costo Reducido**: Indica el impacto en la función objetivo al cambiar el valor de una variable no básica.
- **Costo Dual (Precio Sombra)**: Mide el cambio en la función objetivo por unidad de cambio en una restricción.
- **Costos en una BFS**: Descomponen el costo en contribuciones de variables básicas y no básicas.

Si tienes más preguntas o necesitas más ejemplos, por favor házmelo saber.