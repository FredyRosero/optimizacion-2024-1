()    # Taller 4 Optimización
**Departamento de Ingeniería de Sistemas e Ingeniería Industrial**

**Universidad Nacional de Colombia**


XXX = 270, YYY = 114
---

## Primer Punto (40 Puntos)

Una compañía produce cierto tipo de accesorios. Estos accesorios se producen en una de las instalaciones de producción, luego se envían a uno de los centros de distribución y finalmente se despachan a los vendedores al detal. 

Cada vendedor al detal tiene un pronóstico de demanda, cada instalación de producción tiene una cantidad mínima y máxima de accesorios que puede fabricar durante este período y cada centro de distribución tiene una capacidad máxima de accesorios que puede distribuir. 

El costo de transporte por unidad sólo es válido si se transporta un número mínimo de unidades del accesorio ya sea desde las fábricas a los centros de distribución o desde estos últimos hacia los vendedores al detal, lo que significa que cualquier envío desde las instalaciones de producción a los centros de distribución debe ser mayor a N unidades y cualquier envío desde los centros de distribución a los vendedores al detal debe ser mayor a M unidades.

Como complemento del punto uno debe asegurarse que cada una de las fábricas produzca al menos el 80% de su capacidad máxima de suministro y la cantidad mínima a transportar entre cualquier dos nodos debe ser mayor al valor de mínimo demanda total de un centro de demanda (ciudad).

### Datos primer punto

| Fábricas     | Capacidad |
| ------------ | --------- |
| Bogotá       | 5502      |
| Medellín     | 5909      |
| Pereira      | 1497      |
| Cali         | 5862      |
| Barranquilla | 5161      |
| Bucaramanga  | 1254      |

Los sitios de las bodegas son:
Bogotá, Medellín, Pereira, Cali, Barranquilla, Bucaramanga, Tenjo, Itagüí, Palmira, Manizales, Santa Marta, Popayan, Montería

#### Ubicación y demanda de cada punto...

City: Bogotá
Point 1: Coordinates: (4.568565647912089, -74.00270535750907), Demand: 333 units
Point 2: Coordinates: (4.699675267272541, -74.07013834007228), Demand: 275 units
Point 3: Coordinates: (4.605959459359155, -73.90746369562126), Demand: 234 units
Point 4: Coordinates: (4.659937063543658, -74.19389215200056), Demand: 184 units
Point 5: Coordinates: (4.738392236201863, -73.96694806082473), Demand: 824 units
Point 6: Coordinates: (4.745245132662214, -74.05316646428159), Demand: 385 units
Point 7: Coordinates: (4.641713414509857, -74.12465194138828), Demand: 252 units
Point 8: Coordinates: (4.570809571300359, -73.92035359354273), Demand: 569 units
Point 9: Coordinates: (4.552916274446604, -74.10994941504137), Demand: 437 units
Point 10: Coordinates: (4.62600534010459, -74.05028318114154), Demand: 830 units
Point 11: Coordinates: (4.618542022125971, -74.13280565976245), Demand: 560 units
Point 12: Coordinates: (4.612961297506587, -74.05915339775301), Demand: 354 units
Point 13: Coordinates: (4.668352608761532, -73.90056673165957), Demand: 316 units
Point 14: Coordinates: (4.79212846131582, -74.19311557774746), Demand: 695 units
Point 15: Coordinates: (4.768387148819588, -73.91357516563635), Demand: 273 units
Point 16: Coordinates: (4.676193393539264, -74.03070168231001), Demand: 524 units
Point 17: Coordinates: (4.613825560227022, -74.14791329582887), Demand: 306 units
Point 18: Coordinates: (4.620253419081813, -74.03801851849347), Demand: 211 units
Point 19: Coordinates: (4.631651143383878, -74.08450952246882), Demand: 349 units
Point 20: Coordinates: (4.584826182628852, -74.00492640453885), Demand: 94 units
Point 21: Coordinates: (4.847285437118325, -73.98975277454807), Demand: 347 units
Total Demand 8352

City: Medellín
Point 1: Coordinates: (6.24678283335728, -75.55975056917285), Demand: 76 units
Point 2: Coordinates: (6.39187735180898, -75.45636631092621), Demand: 132 units
Point 3: Coordinates: (6.215345892814951, -75.54014752379258), Demand: 267 units
Point 4: Coordinates: (6.2082762746581635, -75.59391980515261), Demand: 121 units
Point 5: Coordinates: (6.323480241300139, -75.56604887115931), Demand: 260 units
Point 6: Coordinates: (6.279431539183332, -75.51004934195527), Demand: 66 units
Point 7: Coordinates: (6.326962078155686, -75.69827778274481), Demand: 146 units
Point 8: Coordinates: (6.26915784596375, -75.49658169166341), Demand: 121 units
Point 9: Coordinates: (6.34696603880599, -75.71013274300316), Demand: 164 units
Point 10: Coordinates: (6.318588603337838, -75.65628011272405), Demand: 245 units
Point 11: Coordinates: (6.185193555627089, -75.56754876195153), Demand: 265 units
Point 12: Coordinates: (6.423252482834666, -75.58331580790333), Demand: 114 units
Point 13: Coordinates: (6.330840277320823, -75.45125253796577), Demand: 121 units
Point 14: Coordinates: (6.340813281523848, -75.45970691471041), Demand: 124 units
Point 15: Coordinates: (6.180089045262404, -75.72198766559482), Demand: 152 units
Point 16: Coordinates: (6.442411401933392, -75.49338460849934), Demand: 198 units
Total Demand 2572

City: Pereira
Point 1: Coordinates: (4.934159216116012, -75.71159408465378), Demand: 50 units
Point 2: Coordinates: (4.888683460412503, -75.74212851365125), Demand: 54 units
Point 3: Coordinates: (4.818079296564807, -75.79892751507316), Demand: 80 units
Point 4: Coordinates: (4.856415305727871, -75.66832205637897), Demand: 58 units
Point 5: Coordinates: (4.906458817777211, -75.76549168270424), Demand: 53 units
Point 6: Coordinates: (4.88463509254025, -75.83919424577893), Demand: 72 units
Point 7: Coordinates: (4.810177229025141, -75.73860332737266), Demand: 72 units
Point 8: Coordinates: (4.753602195409531, -75.68040618936003), Demand: 41 units
Total Demand 480

City: Cali
Point 1: Coordinates: (3.4988178385383626, -76.53906625393655), Demand: 154 units
Point 2: Coordinates: (3.5319520676627203, -76.48352135867346), Demand: 92 units
Point 3: Coordinates: (3.518102645223277, -76.56859062219138), Demand: 234 units
Point 4: Coordinates: (3.435112143871753, -76.5485411295532), Demand: 265 units
Point 5: Coordinates: (3.5421168393062934, -76.47519594758568), Demand: 86 units
Point 6: Coordinates: (3.421216861250469, -76.64242127742459), Demand: 101 units
Point 7: Coordinates: (3.4141443605594444, -76.49272651226782), Demand: 224 units
Point 8: Coordinates: (3.3768732888942368, -76.47073692971365), Demand: 153 units
Point 9: Coordinates: (3.485087930296774, -76.64043206190112), Demand: 169 units
Point 10: Coordinates: (3.3876066466311925, -76.61253774277654), Demand: 63 units
Point 11: Coordinates: (3.3563209385071775, -76.56290852348708), Demand: 132 units
Point 12: Coordinates: (3.501460440152619, -76.56051785491243), Demand: 159 units
Point 13: Coordinates: (3.532424235443296, -76.53406716411841), Demand: 243 units
Point 14: Coordinates: (3.435739509617801, -76.48228152032999), Demand: 121 units
Point 15: Coordinates: (3.419761006983692, -76.5897984537001), Demand: 4 units
Total Demand 2200

City: Barranquilla
Point 1: Coordinates: (10.918961299792898, -74.85311969546414), Demand: 59 units
Point 2: Coordinates: (11.02000512577378, -74.92323149271067), Demand: 102 units
Point 3: Coordinates: (11.017740314351926, -74.89182351470355), Demand: 140 units
Point 4: Coordinates: (10.905922582083427, -74.8395095538373), Demand: 74 units
Point 5: Coordinates: (11.023056461716886, -74.8042446002198), Demand: 125 units
Point 6: Coordinates: (11.045931468458035, -74.84107249350501), Demand: 58 units
Point 7: Coordinates: (11.026368363636914, -74.85612353940938), Demand: 133 units
Point 8: Coordinates: (11.090591093335517, -74.90616360272757), Demand: 53 units
Point 9: Coordinates: (10.911651573465871, -74.91256232905822), Demand: 65 units
Point 10: Coordinates: (10.986688807659831, -74.96035535057425), Demand: 159 units
Point 11: Coordinates: (11.03202695434874, -74.81822752553282), Demand: 149 units
Point 12: Coordinates: (11.039378716773514, -74.80226172261354), Demand: 74 units
Point 13: Coordinates: (11.077566551549276, -74.87477118766326), Demand: 91 units
Point 14: Coordinates: (11.086983962783636, -74.84027381757024), Demand: 84 units
Point 15: Coordinates: (11.022008597178726, -74.90588200231136), Demand: 14 units
Total Demand 1380

City: Bucaramanga
Point 1: Coordinates: (7.03101588281971, -73.1385508171867), Demand: 50 units
Point 2: Coordinates: (7.0314552737773885, -73.00098735923719), Demand: 60 units
Point 3: Coordinates: (7.075489608474301, -73.14574348419278), Demand: 77 units
Point 4: Coordinates: (7.117533830410376, -73.19989982414273), Demand: 61 units
Point 5: Coordinates: (7.083597662020387, -73.15929424826093), Demand: 75 units
Point 6: Coordinates: (7.076781188709875, -73.04292911983586), Demand: 57 units
Point 7: Coordinates: (7.166155765347051, -73.05342808629565), Demand: 61 units
Point 8: Coordinates: (7.130199171733082, -73.11591141400521), Demand: 58 units
Point 9: Coordinates: (7.088465559298013, -73.19531822127395), Demand: 31 units
Total Demand 530

City: Manizales
Point 1: Coordinates: (5.067523932886786, -75.57062874019675), Demand: 66 units
Point 2: Coordinates: (5.160858736395765, -75.63537120409545), Demand: 52 units
Point 3: Coordinates: (5.064813206035943, -75.5041614711201), Demand: 66 units
Point 4: Coordinates: (5.149086609760744, -75.51117602733045), Demand: 51 units
Point 5: Coordinates: (5.005808749827277, -75.52643249847375), Demand: 77 units
Point 6: Coordinates: (5.110664667617254, -75.46561559237615), Demand: 89 units
Total Demand 401

City: Santa Marta
Point 1: Coordinates: (11.268139753594316, -74.08372835153806), Demand: 63 units
Point 2: Coordinates: (11.241454209991542, -74.13962035350612), Demand: 87 units
Point 3: Coordinates: (11.298610514516472, -74.22908869624831), Demand: 51 units
Point 4: Coordinates: (11.24090960658347, -74.14744877799725), Demand: 74 units
Point 5: Coordinates: (11.261359997239959, -74.09729226489115), Demand: 60 units
Point 6: Coordinates: (11.27244340317256, -74.11532069083937), Demand: 68 units
Point 7: Coordinates: (11.132332770059358, -74.24413041998471), Demand: 52 units
Point 8: Coordinates: (11.165722280826017, -74.09331756204145), Demand: 45 units
Total Demand 500

City: Popayán
Point 1: Coordinates: (2.447583549826251, -76.63625408654563), Demand: 60 units
Point 2: Coordinates: (2.4811300986664984, -76.62597937594788), Demand: 65 units
Point 3: Coordinates: (2.4923105158964214, -76.64075942825328), Demand: 59 units
Point 4: Coordinates: (2.4631740073872597, -76.63766796464262), Demand: 62 units
Point 5: Coordinates: (2.5544313919881647, -76.5800444835752), Demand: 34 units
Total Demand 280

City: Montería
Point 1: Coordinates: (8.708136917860106, -75.82228643506112), Demand: 64 units
Point 2: Coordinates: (8.801995245843175, -75.82935328858713), Demand: 70 units
Point 3: Coordinates: (8.886607470772898, -75.93416983347318), Demand: 72 units
Point 4: Coordinates: (8.79056483189564, -75.87296315800162), Demand: 55 units
Point 5: Coordinates: (8.82716975168954, -75.82123790783693), Demand: 59 units
Point 6: Coordinates: (8.710407678960928, -75.86502019564988), Demand: 53 units
Point 7: Coordinates: (8.724098748741751, -75.93971058373721), Demand: 69 units
Point 8: Coordinates: (8.816028148947925, -75.87857258515331), Demand: 18 units
Total Demand 460

City: Cartagena
Point 1: Coordinates: (10.382330259710246, -75.50962929424196), Demand: 103 units
Point 2: Coordinates: (10.39809731930941, -75.40558135044982), Demand: 59 units
Point 3: Coordinates: (10.384228304751158, -75.46257477763645), Demand: 94 units
Point 4: Coordinates: (10.483290750855364, -75.55647396199137), Demand: 85 units
Point 5: Coordinates: (10.432551145566416, -75.52774364697767), Demand: 89 units
Point 6: Coordinates: (10.411820723338215, -75.5125475918667), Demand: 62 units
Point 7: Coordinates: (10.36420012848041, -75.57288633043346), Demand: 125 units
Point 8: Coordinates: (10.374775244444212, -75.40488201050633), Demand: 125 units
Point 9: Coordinates: (10.451368515655714, -75.45563108194403), Demand: 66 units
Point 10: Coordinates: (10.340486718075276, -75.45528932452014), Demand: 51 units
Point 11: Coordinates: (10.39257919820145, -75.53886036382914), Demand: 53 units
Point 12: Coordinates: (10.484091290093463, -75.42394809922824), Demand: 28 units
Total Demand 940

City: Cúcuta
Point 1: Coordinates: (7.922709650919586, -72.57212767968609), Demand: 107 units
Point 2: Coordinates: (7.968884205766315, -72.43664206936042), Demand: 95 units
Point 3: Coordinates: (7.8115796663872885, -72.5916540581052), Demand: 93 units
Point 4: Coordinates: (7.878929483561572, -72.57735231118328), Demand: 60 units
Point 5: Coordinates: (7.889794864778388, -72.53239943375449), Demand: 97 units
Point 6: Coordinates: (7.937888298010477, -72.5600536287404), Demand: 103 units
Point 7: Coordinates: (7.913572482511313, -72.53713714825639), Demand: 55 units
Point 8: Coordinates: (7.960786162538586, -72.40199867582604), Demand: 112 units
Point 9: Coordinates: (7.827362882549887, -72.42345802672635), Demand: 81 units
Point 10: Coordinates: (7.996685016553495, -72.45157359221406), Demand: 37 units
Total Demand 840

City: Villavicencio
Point 1: Coordinates: (4.217429769459895, -73.60575927766328), Demand: 68 units
Point 2: Coordinates: (4.251820672957551, -73.54432623086454), Demand: 53 units
Point 3: Coordinates: (4.2751417936385385, -73.62115120388508), Demand: 71 units
Point 4: Coordinates: (4.161673941847539, -73.63047687003525), Demand: 77 units
Point 5: Coordinates: (4.223813829059786, -73.65259418262617), Demand: 68 units
Point 6: Coordinates: (4.1759152691104555, -73.59868886001021), Demand: 57 units
Point 7: Coordinates: (4.239313994689246, -73.5632525426589), Demand: 77 units
Point 8: Coordinates: (4.275649705907236, -73.52031539826552), Demand: 57 units
Point 9: Coordinates: (4.161079765059042, -73.63085089467232), Demand: 22 units
Total Demand 550

City: Tunja
Point 1: Coordinates: (5.578288272562176, -73.3187064858441), Demand: 62 units
Point 2: Coordinates: (5.643071028986838, -73.3631952620379), Demand: 58 units
Point 3: Coordinates: (5.590048913119787, -73.2613348392755), Demand: 62 units
Point 4: Coordinates: (5.641531032938612, -73.3067738084488), Demand: 28 units
Total Demand 210

Para los puntos de ubicación de la demanda en cada zona de demanda usar el promedio. El costo por kilogramo por kilometro es 1270 pesos por kilogramo y cada unidad pesa 2.114 kilogramos. El costo de distribuir una unidad al interior de las ciudades considerarlo igual a 2270 pesos

### a) (25 puntos)
Formular el modelo de Programación Lineal Entera Mixta (PLEM) que minimice el costo total de transporte.

### b) (15 puntos)
Encuentre la solución al modelo anterior con los datos provistos en el correo usando Gurobi.

### Solution

### **a) Formulación del Modelo de Programación Lineal Entera Mixta (PLEM)**

#### Parámetros

- **FABRICAS** ($ f $): Conjunto de fábricas que producen accesorios.
- **BODEGAS** ($ b $): Conjunto de centros de distribución a los que se envían los accesorios desde las fábricas.
- **TIENDAS** ($ t $): Conjunto de tiendas que representan los puntos de demanda de los productos.

- $ \text{Capacidad}_f $: Capacidad máxima de producción de la fábrica $ f $.
- $ \text{Demanda}_t $: Demanda total de la tienda $ t $.
- $ \text{PesoUnidad} $: Peso de cada unidad producida, 2.114 kg.
- $ \text{CostoInterCiudad} $: Costo por kilogramo por kilómetro entre ciudades, 1270 pesos/kg-km.
- $ \text{CostoIntraCiudad} $: Costo de distribución dentro de la misma ciudad, 2270 pesos por unidad.
- $ \text{Dist}_{fb} $: Distancia entre la fábrica $ f $ y el centro de distribución $ b $.
- $ \text{Dist}_{bt} $: Distancia entre el centro de distribución $ b $ y la tienda $ t $.
- $ N $: Mínimo de unidades a enviar entre fábricas y bodegas, establecido en 210 unidades.
- $ M $: Mínimo de unidades a enviar entre bodegas y tiendas, establecido en 4 unidades.
- $ \alpha $: Porcentaje mínimo de utilización de la capacidad de las fábricas (80%, es decir, $ \alpha = 0.8 $).

#### Variables de Decisión

- $ X_{fb} $: Cantidad de unidades enviadas desde la fábrica $ f $ al centro de distribución $ b $.
- $ Y_{bt} $: Cantidad de unidades enviadas desde el centro de distribución $ b $ a la tienda $ t $.
- $ Z_{fb} $: Variable binaria que indica si se realiza envío desde la fábrica $ f $ al centro de distribución $ b $.
- $ W_{bt} $: Variable binaria que indica si se realiza envío desde el centro de distribución $ b $ a la tienda $ t $.

#### Función Objetivo

Minimizar el costo total de transporte, que se compone de dos partes:

##### 1. Transporte entre Fábricas y Bodegas

- **Intra-ciudad**: Cuando la fábrica y la bodega están en la misma ciudad, el costo por unidad es $ \text{CostoIntraCiudad} $.
  $$
  \sum_{f \in F} \sum_{b \in B} X_{fb} \times \text{Dist}_{fb} \times \text{CostoIntraCiudad}
  $$
  
- **Inter-ciudad**: Cuando la fábrica y la bodega están en diferentes ciudades, el costo depende del peso de las unidades transportadas y la distancia.
  $$
  \sum_{f \in F} \sum_{b \in B} X_{fb} \times \text{Dist}_{fb} \times \text{PesoUnidad} \times \text{CostoInterCiudad}
  $$

##### 2. Transporte entre Bodegas y Tiendas

- **Intra-ciudad**: Transporte dentro de la misma ciudad entre la bodega y la tienda.
  $$
  \sum_{b \in B} \sum_{t \in T} Y_{bt} \times \text{Dist}_{bt} \times \text{CostoIntraCiudad}
  $$

- **Inter-ciudad**: Transporte entre diferentes ciudades desde la bodega hacia la tienda.
  $$
  \sum_{b \in B} \sum_{t \in T} Y_{bt} \times \text{Dist}_{bt} \times \text{PesoUnidad} \times \text{CostoInterCiudad}
  $$

La función objetivo final es la suma de los costos anteriores:

$$
\text{Minimizar} \quad CostoTotal = \text{CostoFábricaBodega} + \text{CostoBodegaTienda}
$$

#### Restricciones

##### 1. Capacidad de Producción de las Fábricas

Cada fábrica debe producir al menos el 80% de su capacidad y no exceder su límite de producción:

$$
\alpha \times \text{Capacidad}_f \leq \sum_{b \in B} X_{fb} \leq \text{Capacidad}_f, \quad \forall f \in F
$$

##### 2. Balance en los Centros de Distribución

La cantidad de unidades que llega a cada centro de distribución debe ser igual o mayor a la cantidad de unidades que se distribuyen a las tiendas:

$$
\sum_{f \in F} X_{fb} \geq \sum_{t \in T} Y_{bt}, \quad \forall b \in B
$$

##### 3. Satisfacción de la Demanda

La demanda de cada tienda debe ser satisfecha exactamente:

$$
\sum_{b \in B} Y_{bt} = \text{Demanda}_t, \quad \forall t \in T
$$

##### 4. Envíos Mínimos y Variables Binarias (Fábricas a Bodegas)

Si se realiza un envío desde la fábrica $ f $ al centro de distribución $ b $, el envío debe cumplir con un mínimo de $ N $ unidades y no exceder la capacidad de la fábrica:

$$
\begin{align*}
X_{fb} \geq N \times Z_{fb}, \quad \forall f \in F, \forall b \in B \\
X_{fb} \leq \text{Capacidad}_f \times Z_{fb}, \quad \forall f \in F, \forall b \in B
\end{align*}
$$

##### 5. Envíos Mínimos y Variables Binarias (Bodegas a Tiendas)

Si se realiza un envío desde el centro de distribución $ b $ a la tienda $ t $, el envío debe cumplir con un mínimo de $ M $ unidades y no exceder la demanda de la tienda:

$$
\begin{align*}
Y_{bt} \geq M \times W_{bt}, \quad \forall b \in B, \forall t \in T \\
Y_{bt} \leq \text{Demanda}_t \times W_{bt}, \quad \forall b \in B, \forall t \in T
\end{align*}
$$

##### 6. Restricciones de Dominio

- $ X_{fb} \geq 0 $, entero, $ \forall f \in F, \forall b \in B $
- $ Y_{bt} \geq 0 $, entero, $ \forall b \in B, \forall t \in T $
- $ Z_{fb} \in \{0, 1\} $, binario, $ \forall f \in F, \forall b \in B $
- $ W_{bt} \in \{0, 1\} $, binario, $ \forall b \in B, \forall t \in T $

#### Modelo de Programación Lineal Entera Mixta (PLEM)
$$\begin{align*}  
\text{min} \quad & z =  
\sum_{f \in F} \sum_{b \in B} X_{fb} \times \text{Dist}_{fb} \times \text{CostoIntraCiudad} \\  
& + \sum_{f \in F} \sum_{b \in B} X_{fb} \times \text{Dist}_{fb} \times \text{PesoUnidad} \times \text{CostoInterCiudad} \\  
& + \sum_{b \in B} \sum_{t \in T} Y_{bt} \times \text{Dist}_{bt} \times \text{CostoIntraCiudad} \\  
& + \sum_{b \in B} \sum_{t \in T} Y_{bt} \times \text{Dist}_{bt} \times \text{PesoUnidad} \times \text{CostoInterCiudad}  
\\
\text{s.a.} \\
& \alpha \times \text{Capacidad}_f \leq \sum_{b \in B} X_{fb} \leq \text{Capacidad}_f \quad \forall f \in F\\
& \sum_{f \in F} X_{fb} \geq \sum_{t \in T} Y_{bt} \quad \forall b \in B \\
& \sum_{b \in B} Y_{bt} = \text{Demanda}_t \quad \forall t \in T \\
& X_{fb} \geq N \times Z_{fb} \quad \forall f \in F, \forall b \in B \\
& X_{fb} \leq \text{Capacidad}_f \times Z_{fb} \quad \forall f \in F, \forall b \in B \\
& Y_{bt} \geq M \times W_{bt} \quad \forall b \in B, \forall t \in T \\
& Y_{bt} \leq \text{Demanda}_t \times W_{bt} \quad \forall b \in B, \forall t \in T \\
& X_{fb} \geq 0, \quad Y_{bt} \geq 0, \quad Z_{fb} \in \{0,1\}, \quad W_{bt} \in \{0,1\}
\end{align*}$$
---

## Segundo Punto (40 Puntos)

Dado un inventario de rollos de ancho W metros, determine cuánto de estos rollos cortar de tal manera que $b_i$, $i = 1, ..., m$ unidades de ancho $w_i$ sean producidas, minimizando el total en centímetros cuadrados de desperdicio de rollos. Deben satisfacerse los requerimientos presentados en los datos para los m diferentes tamaños dados.

### Datos del segundo punto
El tamaño del rollo maestro es 2500 y se consideran desperdicios los rollos cortados y no vendidos. Las longitudes y demandas de los rollos a cortar son:

Piece Length: 701, Demand: 27

| Pieza | Longitud (mm) | Demanda (unidades) |
| ----- | ------------- | ------------------ |
| 1     | 692           | 14                 |
| 2     | 627           | 25                 |
| 3     | 491           | 50                 |
| 4     | 253           | 38                 |
| 5     | 271           | 19                 |
| 6     | 628           | 32                 |
| 7     | 533           | 50                 |
| 8     | 708           | 18                 |
| 9     | 520           | 12                 |
| 10    | 580           | 16                 |
| 11    | 630           | 39                 |
| 12    | 406           | 39                 |
| 13    | 587           | 36                 |
| 14    | 346           | 40                 |
| 15    | 632           | 45                 |
| 16    | 310           | 49                 |
| 17    | 617           | 30                 |
| 18    | 729           | 11                 |
| 19    | 723           | 27                 |
| 20    | 701           | 27                 |

### a) (15 puntos)
Formular el modelo de Programación Lineal Entera Mixta (PLEM) definiendo los patrones de cortes posibles.

### b) (25 puntos)
Encuentre la solución al modelo anterior con los datos provistos a través del algoritmo de Branch and Bound usando Gurobi. Presentar el árbol de decisión.

### Solución

* **Tamaño del rollo maestro**: 2500 unidades.

### **a) Formulación del modelo de Programación Lineal Entera Mixta (PLEM)**

### Modelo Matemático

#### Variables:

* $x_j$: Número de veces que se usa el patrón $j$ de corte.
* $s_i$: Cantidad de piezas $i$ cortadas en exceso (es decir, más de lo que se demanda).

#### Función Objetivo:

Minimizar el desperdicio total:

* **Desperdicio de material**: Es la cantidad de material sobrante de los rollos cortados.
* **Desperdicio de piezas**: Es la cantidad de piezas cortadas en exceso respecto a la demanda.

$$\text{Minimizar } Z = \sum_{j=1}^{n} (W - \sum_{i=1}^{m} L_i \times P_{ij}) \times x_j + \sum_{i=1}^{m} s_i$$

donde:

* $W$ es el ancho del rollo maestro.
* $L_i$ es la longitud de la pieza $i$.
* $P_{ij}$ es el número de piezas $i$ cortadas en el patrón $j$.

#### Restricciones:

* **Demanda mínima de piezas**: Asegurar que la cantidad total de piezas producidas cubra la demanda, permitiendo exceso en la variable $s_i$.

$$\sum_{j=1}^{n} P_{ij} \times x_j - s_i \geq D_i \quad \forall i = 1, \ldots, m$$

donde:

* $D_i$ es la demanda de la pieza $i$.
