## Preguntas y Respuestas Clave en Programación Lineal

### ¿Qué pasa con el dual si el costo sombra de una variable es 0?

Si el costo sombra (también conocido como precio sombra o valor dual) de una variable es 0, significa que un pequeño cambio en el lado derecho (RHS) de la restricción asociada no cambiará el valor óptimo de la función objetivo. En otras palabras, la restricción no está "activa" en el sentido de que no afecta directamente el valor óptimo en su punto actual.

### ¿Qué pasa si el primal y el dual tienen el mismo valor óptimo?

Cuando el primal y el dual tienen el mismo valor óptimo, se cumple el teorema de dualidad fuerte, que establece que si ambos problemas son factibles, sus valores óptimos son iguales. Esto también implica que la solución es óptima para ambos problemas y que se han satisfecho todas las condiciones de complementariedad.

### ¿Cómo se hace para saber si un problema tiene múltiples soluciones?

Un problema de programación lineal tiene múltiples soluciones óptimas si en el tableau final (o en la fila 0 del método Simplex) hay una o más variables no básicas con coeficiente cero. Esto indica que puede ajustarse una de estas variables sin afectar el valor de la función objetivo, lo que significa que existen múltiples combinaciones de variables que producen el mismo valor óptimo.

### ¿Qué significa el precio sombra de una restricción?

El precio sombra de una restricción representa la cantidad en que cambiaría el valor óptimo de la función objetivo por una unidad adicional de recurso disponible (es decir, un cambio marginal en el RHS de la restricción). Si el precio sombra es positivo, aumentar el RHS aumentará el valor óptimo en ese valor; si es negativo, lo disminuirá.

### ¿Cómo afectan los cambios en los valores del RHS a la solución óptima?

Los cambios en los valores del RHS (lado derecho de las restricciones) pueden afectar la solución óptima dependiendo del rango permisible de esos cambios. Si el cambio en el RHS está dentro del rango permisible, la solución óptima se ajustará sin cambiar la base de la solución. Si está fuera del rango, la solución base óptima cambiará y se requerirá una nueva optimización para encontrar la nueva solución.

### ¿Qué indican los rangos permisibles de los coeficientes de la función objetivo?

Los rangos permisibles de los coeficientes de la función objetivo indican cuánto pueden variar los coeficientes de las variables en la función objetivo antes de que la base óptima (conjunto de variables básicas y no básicas) cambie. Estos rangos ayudan a entender la sensibilidad de la solución óptima a cambios en los costos o beneficios de las variables.

### ¿Qué implica la factibilidad del dual para la solución del primal?

La factibilidad del dual implica que si el problema dual tiene una solución factible, entonces el problema primal también debe tener una solución factible, y viceversa. Esto es una consecuencia del teorema de dualidad fuerte. La factibilidad en ambos problemas es una condición necesaria para que se pueda alcanzar un valor óptimo común.

### ¿Qué implica la holgura complementaria en soluciones óptimas?

La holgura complementaria establece que para cada par de restricciones duales y primales, el producto de la variable dual y la holgura de la restricción primal debe ser cero en la solución óptima. Esto significa que si una restricción está activa (sin holgura), la variable dual asociada puede ser positiva; si una restricción no está activa (con holgura), la variable dual debe ser cero.

### ¿Cómo se determina si se debe introducir una nueva variable (producto) en el modelo?

Para determinar si se debe introducir una nueva variable o producto en el modelo, se evalúa el costo reducido de esa variable. Si el costo reducido es negativo en un problema de minimización (o positivo en uno de maximización), se justifica la introducción de esa variable, ya que podría mejorar el valor óptimo de la función objetivo.

### ¿Para convertir a la forma estándar, el tipo de variable de holgura (exceso o holgura) depende del tipo de restricción y de si es minimización o maximización?

El tipo de variable de holgura o exceso que se agrega depende del tipo de restricción:

* **Holgura:** Se agrega a las restricciones del tipo "menor o igual" ($\leq$) para convertirlas en igualdades.
* **Exceso:** Se resta en las restricciones del tipo "mayor o igual" ($\geq$) para convertirlas en igualdades.

El objetivo de la optimización (minimización o maximización) no afecta el tipo de variable de holgura o exceso que se debe agregar, ya que esto depende únicamente de la dirección de las restricciones.


### ¿Qué implica que un precio sombra o valor dual sea 0?

Un precio sombra o valor dual igual a 0 implica que un pequeño cambio en el RHS de la restricción asociada no afectará el valor óptimo de la función objetivo. En otras palabras, la restricción no es "crítica" en el punto óptimo; la cantidad de recurso asociado a esa restricción no limita el valor óptimo.

### ¿Qué implica tener una restricción activa?

Una restricción activa es una restricción que se cumple como una igualdad en la solución óptima, es decir, no tiene holgura (slack). Esto significa que en la solución óptima, la variable relacionada con esa restricción está en su límite y cualquier cambio en esta restricción afectaría el valor de la función objetivo.

### ¿Qué es el teorema de dualidad fuerte?

El teorema de dualidad fuerte establece que si un problema de programación lineal (el primal) tiene una solución óptima finita, entonces su problema dual también tiene una solución óptima finita, y los valores de la función objetivo de ambas soluciones son iguales. Este teorema garantiza la igualdad de los valores óptimos en ambos problemas cuando ambos son factibles.

### ¿Cómo se interpreta una solución degenerada?

Una solución degenerada en programación lineal ocurre cuando más restricciones de las necesarias son activas en la solución óptima. Esto significa que en la solución óptima, una o más variables básicas son iguales a cero. Aunque la solución es óptima, la degeneración puede llevar a múltiples iteraciones sin mejora en el valor de la función objetivo, lo que puede causar que el método Simplex se estanque.

### ¿Qué significa la complementariedad fuerte en programación lineal?

La complementariedad fuerte se refiere a la condición donde para cada restricción dual y primal en la solución óptima, si una variable dual es positiva, la restricción primal correspondiente es activa, y viceversa. Es una parte clave del teorema de dualidad fuerte, que asegura que la solución es óptima para ambos problemas primal y dual.

### ¿Cómo afecta la no negatividad de las variables al modelo?

La no negatividad de las variables asegura que las soluciones de programación lineal sean físicamente significativas en contextos donde las variables representan cantidades como producción, consumo o recursos. Esta condición garantiza que las soluciones del modelo sean factibles y aplicables a situaciones del mundo real.

### ¿Qué es una base factible y cómo se determina en el método Simplex?

Una base factible es un conjunto de variables básicas que satisface todas las restricciones del problema y donde todas las variables básicas son no negativas. En el método Simplex, la base factible inicial se determina eligiendo un conjunto de variables básicas que cumplan las restricciones, y a partir de ahí se busca una solución óptima a través de iteraciones sucesivas.

