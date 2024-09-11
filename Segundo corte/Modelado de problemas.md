### Técnica para Modelar Problemas de Transporte con Programación Lineal

1. **Definir las Variables de Decisión:**
    
    * Representa la cantidad de bienes (por ejemplo, electricidad, productos, recursos) transportados desde cada fuente (planta, almacén, etc.) a cada destino (ciudad, cliente, etc.) con variables de decisión.
    * Denotamos las variables como $x_{ij}$, donde:
        * $i$ indica la fuente (por ejemplo, planta).
        * $j$ indica el destino (por ejemplo, ciudad).
    * Ejemplo: $x_{ij}$ es la cantidad de bienes transportados desde la fuente $i$ al destino $j$.
2. **Definir la Función Objetivo:**
    
    * La función objetivo de un problema de transporte suele ser **minimizar el costo total** de transportar bienes desde todas las fuentes a todos los destinos.
    * Se expresa como la suma del costo unitario de transporte multiplicado por la cantidad transportada para cada par de fuente-destino:
    
    $$\text{Minimizar } Z = \sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} \cdot x_{ij}$$
    
    donde:
    
    * $c_{ij}$ es el costo de enviar una unidad de bien desde la fuente $i$ al destino $j$.
    * $x_{ij}$ es la cantidad de bienes transportados desde la fuente $i$ al destino $j$.
3. **Establecer las Restricciones:**
    
    a) **Restricciones de Oferta (Capacidad de las Fuentes):**
    
    * Cada fuente tiene una cantidad máxima disponible que puede suministrar:
    
    $$\sum_{j=1}^{n} x_{ij} \leq S_i, \quad \forall i = 1, 2, \ldots, m$$
    
    donde:
    
    * $S_i$ es la capacidad o suministro total de la fuente $i$.
    
    b) **Restricciones de Demanda (Requerimientos de los Destinos):**
    
    * Cada destino tiene una cantidad fija de demanda que debe ser satisfecha:
    
    $$\sum_{i=1}^{m} x_{ij} = D_j, \quad \forall j = 1, 2, \ldots, n$$
    
    donde:
    
    * $D_j$ es la demanda total del destino $j$.
    
    c) **Restricciones de No Negatividad:**
    
    * No se pueden enviar cantidades negativas de bienes:
    
    $$x_{ij} \geq 0, \quad \forall i, j$$
4. **Resolver el Modelo Usando Métodos de Optimización:**
    
    * Utiliza un software de optimización (como LINGO, Gurobi, o Excel Solver) o un método manual (como el Método Simplex de Transporte) para encontrar la solución óptima.
    * Verifica que la solución respete todas las restricciones y minimice el costo total de transporte.