## Teoremas y Lemas Fundamentales en Programación Lineal

### Lema Dualidad Débil (Weak Duality)

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

### Lema 

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

### Lema 

> Si el primal es ilimitado, entonces el problema dual es infactible.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### Lema 

> Si el dual es ilimitado, entonces el primal es infactible.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

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

### **Teorema de Holgura Complementaria**:

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

### **Teorema de la Dualidad Fuerte**:

$$Z_{\text{primal}} = W_{\text{dual}}$$

Si el problema primal tiene una solución óptima finita, entonces el problema dual también tiene una solución óptima finita, y sus valores óptimos son iguales.
    
**Implicación**: Refuerza la validez del Teorema Fundamental de la Dualidad.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### **Teorema de la Dualidad Débil**:

$$W_{\text{dual}} \leq Z_{\text{primal}}$$

Si $\mathbf{x}$ es una solución factible para el problema primal y $\mathbf{y}$ es una solución factible para el problema dual, entonces el valor de la función objetivo del dual es siempre menor o igual al valor de la función objetivo del primal.
    
**Implicación**: Establece una cota inferior para el valor óptimo del problema primal y una cota superior para el valor óptimo del problema dual.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### **Teorema de Factibilidad Primal**:

Si existe una solución factible para el problema primal, entonces existe una solución factible para el problema dual.

**Implicación**: Garantiza que la búsqueda de soluciones en el problema dual es válida siempre que haya soluciones en el problema primal.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### **Teorema de Factibilidad Dual**:

Si existe una solución factible para el problema dual, entonces existe una solución factible para el problema primal.

**Implicación**: Similar al teorema anterior, pero en el sentido inverso.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 307.

### **Teorema de la Optimalidad del Simplex**:

$$\bar{c}_j \geq 0 \quad \forall j \quad \text{(para maximización)}$$ 
$$\bar{c}_j \leq 0 \quad \forall j \quad \text{(para minimización)}$$

Una solución básica factible es óptima si y solo si todos los costos reducidos son no negativos en un problema de maximización (o no positivos en un problema de minimización).

**Implicación**: Permite verificar la optimalidad de una solución básica factible en el método Simplex.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 146.

### **Teorema de la Degeneración**:

Si una solución básica factible tiene más de una variable básica igual a cero, se dice que la solución es degenerada.

**Implicación**: La degeneración puede causar ciclos en el método Simplex, afectando la eficiencia del algoritmo.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 168.

## Lemas Fundamentales en Programación Lineal

### **Lemma 1**:

Si el problema primal tiene una solución óptima finita, entonces el problema dual también tiene una solución óptima finita, y sus valores óptimos son iguales.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.

### **Lemma 2**:

Si el problema dual tiene una solución óptima finita, entonces el problema primal también tiene una solución óptima finita, y sus valores óptimos son iguales.

**Referencia**: Winston, Operations Research: Applications and Algorithms, 4th ed., p. 299.


