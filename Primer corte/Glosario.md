## Glosario de Programación Lineal (Primer Corte)

1. **Programación Lineal (PL)**:
    
    * Método de optimización para maximizar o minimizar una función lineal sujeta a restricciones lineales.

2. **Función Objetivo**:
    
    * La función que se desea maximizar o minimizar en un problema de programación lineal. Ejemplo: $Z = 3x_1 + 5x_2$.

3. **Variables de Decisión**:
    
    * Las variables que representan las decisiones que se deben tomar en el problema de programación lineal. Ejemplo: $x_1$ y $x_2$.

4. **Restricciones**:
    
    * Limitaciones o condiciones que deben cumplirse en el problema de programación lineal. Ejemplo: $x_1 + x_2 \leq 10$.

5. **No Negatividad**:
    
    * Condición que establece que las variables de decisión no pueden ser negativas. Ejemplo: $x_1 \geq 0$.

6. **Solución Factible**:
    
    * Conjunto de valores para las variables de decisión que satisface todas las restricciones del problema.

7. **Solución Óptima**:
    
    * Solución factible que maximiza o minimiza la función objetivo.

8. **Método Simplex**:
    
    * Algoritmo iterativo utilizado para resolver problemas de programación lineal.

9. **Tabla Simplex**:
    
    * Herramienta utilizada en el método Simplex para realizar cálculos iterativos y encontrar la solución óptima.

10. **Solución Básica Factible (SBF)**:
    
    * Solución en la que las variables básicas son iguales a los valores del lado derecho (RHS) y las variables no básicas son iguales a cero.
11. **Variable Básica (VB)**:
    
    * Variable que se incluye en la base de la solución básica factible.

12. **Variable No Básica (VNB)**:
    
    * Variable que no se incluye en la base de la solución básica factible y se fija en cero.

13. **Costo Reducido**:
    
    * Diferencia entre el coeficiente de la función objetivo y la combinación lineal de los precios sombra correspondientes. Indica cuánto cambiaría la función objetivo si se incrementara una unidad de una variable no básica.

14. **Precio Sombra (Dual Price)**:
    
    * Tasa de cambio del valor óptimo de la función objetivo por unidad adicional de recurso disponible en una restricción activa.

15. **Análisis de Sensibilidad**:
    
    * Estudio de cómo cambian las soluciones óptimas cuando se modifican los coeficientes de la función objetivo o las restricciones.

16. **Rango de Coeficientes de la Función Objetivo**:
    
    * Intervalo en el cual los coeficientes de las variables en la función objetivo pueden variar sin cambiar la base óptima.

17. **Rango de Lados Derechos (RHS)**:
    
    * Intervalo en el cual los valores de las restricciones pueden variar sin cambiar la base óptima.

18. **Dualidad**:
    
    * Relación entre un problema de maximización (primal) y su correspondiente problema de minimización (dual).

19. **Problema Primal**:
    
    * El problema original de maximización o minimización en programación lineal.

20. **Problema Dual**:
    
    * Problema asociado con el problema primal, donde las restricciones del primal se convierten en la función objetivo del dual y viceversa.

21. **Holgura Complementaria**:
    
    * Condición que establece que para cada restricción en el problema primal y dual, al menos una de las dos (holgura o precio sombra) debe ser cero.

22. **Teorema Fundamental de la Dualidad**:
    
    * Teorema que establece que si el problema primal tiene una solución óptima, entonces el problema dual también tiene una solución óptima, y sus valores óptimos son iguales.

23. **Coeficiente**:
    
    * Constante multiplicativa de una variable en la función objetivo o en una restricción.

24. **Intervalo de Confianza**:
    
    * Rango en el que pueden variar los coeficientes o valores del RHS sin afectar la solución óptima.

## Conceptos y Definiciones Clave

1. **Proporcionalidad**:
    
    * Suposición de que las contribuciones de cada variable a la función objetivo y las restricciones son proporcionales a los niveles de las variables.

2. **Aditividad**:
    
    * Suposición de que las contribuciones de las variables a la función objetivo y las restricciones se suman linealmente.

3. **Factibilidad**:
    
    * Propiedad de una solución que cumple con todas las restricciones del problema.

4. **Optimalidad**:
    
    * Propiedad de una solución que maximiza o minimiza la función objetivo.

5. **Variable Holgura**:
    
    * Variable añadida a una restricción de desigualdad para convertirla en una ecuación de igualdad.

6. **Variable Artificial**:
    
    * Variable añadida para iniciar el método Simplex en problemas con restricciones de igualdad o de mayor o igual.

## Pasos para Resolver un Problema de Programación Lineal

1. **Definir Variables de Decisión**.
2. **Formular la Función Objetivo**.
3. **Formular las Restricciones**.
4. **Aplicar el Método Simplex o Algoritmo de Solución**.
5. **Interpretar los Resultados**.
6. **Realizar Análisis de Sensibilidad**.