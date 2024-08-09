## Preguntas y Respuestas Clave en Programación Lineal

### Qué pasa con el dual si el costo sombra de una variable es 0?
Si el costo sombra de una variable en el primal es 0, esto significa que la restricción correspondiente en el dual no tiene holgura y no contribuye al valor de la función objetivo del dual. Esto puede implicar que la restricción es redundante en el contexto del problema dual.

### ¿Qué pasa si el primal y el dual tienen el mismo valor óptimo?
Según el Teorema de Dualidad Fuerte, si ambos, el primal y el dual tienen soluciones óptimas, sus valores óptimos son iguales. Esto implica que las soluciones son viables y que se ha alcanzado la óptima eficiencia de recursos.

### ¿Cómo se hace para saber si un problema tiene múltiples soluciones?
Un problema de programación lineal tiene múltiples soluciones óptimas si en la última iteración del método simplex, una variable no básica tiene un costo reducido de cero. Esto indica que hay una dirección en la que se puede mover sin cambiar el valor de la función objetivo, lo que resulta en múltiples soluciones óptimas.

### ¿Qué pasa con el dual si el costo sombra de una variable es 0?
Si el costo sombra (precio dual) de una variable en el primal es 0, esto significa que la restricción correspondiente en el dual no tiene holgura (es decir, la restricción es exactamente una igualdad en la solución óptima). Esto implica que el recurso adicional no afecta el valor de la función objetivo del dual.

### ¿Qué pasa si el primal y el dual tienen el mismo valor óptimo?
Si el primal y el dual tienen el mismo valor óptimo, esto confirma el Teorema de Dualidad Fuerte, que establece que si ambos problemas tienen soluciones óptimas, los valores de sus funciones objetivo son iguales. Esto indica que ambos problemas alcanzaron la máxima eficiencia de recursos.

### ¿Cómo se hace para saber si un problema tiene múltiples soluciones?
Un problema tiene múltiples soluciones óptimas si, en la última iteración del método simplex, una variable no básica tiene un costo reducido de cero. Esto significa que hay una dirección en la que se puede mover sin cambiar el valor de la función objetivo, resultando en múltiples soluciones óptimas.

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