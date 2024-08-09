## Reglas y Principios Clave en Programación Lineal

### Regla de la Correspondencia Primal-Dual
    
Cada restricción en el problema primal corresponde a una variable en el problema dual, y cada variable en el problema primal corresponde a una restricción en el problema dual.

> **Implicación**: Si una variable en el primal tiene un costo reducido de 0, la correspondiente restricción en el dual será activa (es decir, la igualdad se mantiene).

### Teorema de Dualidad Fuerte
    
Si ambos, el problema primal y el dual tienen soluciones óptimas, entonces los valores óptimos de las funciones objetivo son iguales.

> **Implicación**: Si el primal tiene un valor óptimo $Z^*$ y el dual tiene un valor óptimo $W^*$, entonces $Z^* = W^*$.
 
### Condiciones de Optimalidad de Karush-Kuhn-Tucker (KKT)
    
Una solución $x^*$ es óptima para el problema primal y $y^*$ es óptima para el problema dual si y solo si satisfacen las condiciones KKT, que incluyen la viabilidad primal, viabilidad dual, holgura complementaria y no negatividad.

**Implicación**: Estas condiciones ayudan a verificar si las soluciones dadas son óptimas para ambos problemas.

### Regla de la Holgura Complementaria:
    
En las soluciones óptimas, el producto de cada variable primal y su correspondiente restricción dual debe ser cero. Es decir, si $x_i$ es una variable en el primal y $y_j$ es su correspondiente variable dual, entonces $x_i \cdot y_j = 0$.

**Implicación**: Si una variable primal es positiva, la restricción correspondiente en el dual no tiene holgura (es una igualdad). Si una restricción primal tiene holgura, la variable correspondiente en el dual es cero.

### Multiplicidad de Soluciones
    
Un problema de programación lineal tiene múltiples soluciones óptimas si hay más de una solución básica factible que da el mismo valor óptimo de la función objetivo.

**Implicación**: Si en la última tabla del método simplex, una variable no básica tiene un costo reducido de cero, el problema tiene soluciones óptimas múltiples. Esto indica que hay una dirección en la que se puede mover sin cambiar el valor de la función objetivo.

### Regla de la Factibilidad del Dual
    
Si el problema primal tiene una solución factible acotada, el dual también tiene una solución factible acotada y viceversa.

> **Implicación**: Si el primal o el dual no tiene una solución factible acotada, entonces el otro tampoco la tiene. Si el primal es no acotado, el dual no tiene solución factible.

### Impacto del Costo Sombra en el Dual
    
El costo sombra de una variable en el primal representa el valor del cambio en la función objetivo del dual por una unidad adicional de recurso correspondiente.

> **Implicación**: Si el costo sombra de una variable es 0 en el primal, esto significa que el recurso correspondiente en el dual no tiene ningún impacto en el valor de la función objetivo del dual. La restricción en el dual es una igualdad con cero contribución adicional.