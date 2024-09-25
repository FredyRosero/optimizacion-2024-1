import gurobipy as gp
from gurobipy import GRB
import math
import re

print("""
# Primer Punto (40 Puntos)

(Remplazo de XXX por 270 y YYY por 114)

Una compañía produce cierto tipo de accesorios. Estos accesorios se producen en una de las **instalaciones de producción* (fábricas), luego se envían a uno de los **centros de distribución** (bodegas) y finalmente se despachan a los **vendedores al detal** (tiendas). Cada vendedor al detal tiene un pronóstico de demanda, cada instalación de producción tiene una cantidad mínima y máxima de accesorios que puede fabricar durante este período y cada centro de distribución tiene una capacidad máxima de accesorios que puede distribuir. El costo de transporte por unidad sólo es válido si se transporta un número mínimo de unidades del accesorio ya sea desde las fábricas a los centros de distribución o desde estos últimos hacia los vendedores al detal, lo que significa que cualquier envío desde las instalaciones de producción a los centros de distribución debe ser mayor a N unidades y cualquier envío desde los centros de distribución a los vendedores al detal debe ser mayor a M unidades.

Como complemento del punto uno debe asegurarse que cada una de las fábricas produzca al menos el 80% de su capacidad máxima de suministro y la cantidad mínima a transportar entre cualquier dos nodos debe ser mayor al valor de mínimo demanda total de un centro de demanda (ciudad).

Para los puntos de ubicación de la demanda en cada zona de demanda usar el promedio. El costo por kilogramo por kilometro es 1XXX (1270) pesos por kilogramo y cada unidad pesa 2.YYY (2.114) kilogramos. El costo de distribuir una unidad al interior de las ciudades considerarlo igual a 2XXX (2270) pesos
"""
)

model = gp.Model('Optimización_Transporte')

# # Parámetros

# Conjunto de fábricas (instalaciones de producción) y sus capacidades:
FABRICAS = ['Bogotá', 'Medellín', 'Pereira', 'Cali', 'Barranquilla', 'Bucaramanga']
Capacidad = {
    'Bogotá': 5502,
    'Medellín': 5909,
    'Pereira': 1497,
    'Cali': 5862,
    'Barranquilla': 5161,
    'Bucaramanga': 1254
}
print(f'Fábricas: {FABRICAS}')
#print(f'Capacidades: {Capacidad}')

# Los sitios de las bodegas (centros de distribución) son...
# Bogotá, Medellín, Pereira, Cali, Barranquilla, Bucaramanga, Tenjo, Itagüí, Palmira, Manizales, Santa Marta, Popayan, Montería
BODEGAS = ['Bogotá', 'Medellín', 'Pereira', 'Cali', 'Barranquilla', 'Bucaramanga',
     'Tenjo', 'Itagüí', 'Palmira', 'Manizales', 'Santa Marta', 'Popayan', 'Montería']
print(f'Centros de distribución (Bodegas): {BODEGAS}')
# Coordenadas de las ciudades de las bodegas
CoordenaddasCiudad = {
    'Bogotá': (4.60971,-74.08175), 
    'Medellín': (6.257454, -75.574068),
    'Pereira': (4.807141, -75.718139),
    'Cali': (3.482512, -76.498949),
    'Barranquilla': (10.979068, -74.787939),
    'Bucaramanga': (7.116105, -73.114759),
    'Tenjo': (4.869722, -74.143889), # No tiene para centroide -> https://es.wikipedia.org/wiki/Tenjo:	4.869722°, -74.143889°
    'Itagüí': (6.1726, -75.6096), # No tiene para centroide -> https://es.wikipedia.org/wiki/Itag%C3%BC%C3%AD: 6.1726°, -75.6096°
    'Palmira': (3.537581, -76.296857),
    'Manizales': (5.065467, -75.503273),
    'Santa Marta': (11.220445, -74.184496),
    'Popayan': (2.444268, -76.615440),
    'Montería': (8.736465, -75.855345)
}

# Ubicaciones y demandas de los vendedores al detal (tiendas):
TIENDAS = []
DemandasTiendas = {}
CoordenadasTiendas = {}
ciudadDeTiendaDict = {}
ciudadesTiendas = []
DemandaTotalTiendasCiudad = {}
ubicacionesDemandasInput = """
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
"""
def parse_input(input_str):
    city_data = {}
    # Ciudades como "Santa Marta"
    city_pattern = re.compile(r"City: (.+)$")
    total_demand_pattern = re.compile(r"Total Demand (\d+)$")
    point_pattern = re.compile(r"Point \d+: Coordinates: \(([^)]+)\), Demand: (\d+) units")    
    current_city = None
    for line in input_str.strip().split("\n"):
        city_match = city_pattern.match(line)
        total_demand_match = total_demand_pattern.match(line)
        if city_match:
            current_city = city_match.group(1)
            city_data[current_city] = {'Points': []}
        elif total_demand_match:
            total_demand = int(total_demand_match.group(1))
            city_data[current_city]['TotalDemand'] = total_demand
        elif current_city:
            point_match = point_pattern.match(line)
            if point_match:
                coords = tuple(map(float, point_match.group(1).split(", ")))
                demand = int(point_match.group(2))
                point_id = f"{current_city}_{len(city_data[current_city]['Points']) + 1}"
                city_data[current_city]['Points'].append({'ID': point_id, 'Coords': coords, 'Demanda': demand})
    return city_data
demandaDatosTiendasCiudades = parse_input(ubicacionesDemandasInput)

# Promedio geográfico de ciudad
def calcular_promedio_geografico(datos_ciudad):
    latitudes = [punto['Coords'][0] for punto in datos_ciudad['Points']]
    longitudes = [punto['Coords'][1] for punto in datos_ciudad['Points']]
    promedio_latitud = sum(latitudes) / len(latitudes)
    promedio_longitud = sum(longitudes) / len(longitudes)
    return promedio_latitud, promedio_longitud

# Poblar K, DemandasPuntos y CoordenadasPuntos
for ciudad, datos in demandaDatosTiendasCiudades.items():
    CoordenaddasCiudad[ciudad] = calcular_promedio_geografico(datos)
    DemandaTotalTiendasCiudad[ciudad] = datos['TotalDemand']
    ciudadesTiendas.append(ciudad)
    for punto in datos['Points']:
        punto_id = punto['ID']
        TIENDAS.append(punto_id)
        DemandasTiendas[punto_id] = punto['Demanda']
        CoordenadasTiendas[punto_id] = punto['Coords']
        ciudadDeTiendaDict[punto_id] = ciudad
  
print(f'Ciuades de tiendas: {ciudadesTiendas}')
#print(f'Tiendas: {TIENDAS}')
print(f'Coordenadas de las ciudades (actualizado por centroides): {CoordenaddasCiudad}')
print(f'Demanda total por ciudad: {DemandaTotalTiendasCiudad}')

# Ejemplo de coordenada y demanda total de una Fábrica:
print(f'Coordenadas de la fábrica en Bogotá: {CoordenaddasCiudad["Bogotá"]}')
print(f'Demanda total de Bogotá: {DemandaTotalTiendasCiudad["Bogotá"]}')

# Función para calcular la distancia utilizando la fórmula de Haversine
def calcular_distancia(coord1, coord2):
    # Radio de la Tierra en km
    R = 6371.0
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    # Convertir grados a radianes
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    # Fórmula de Haversine
    a = math.sin(delta_phi / 2.0)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c  # Distancia en km
    return distancia

# Calcular Dist_ij: Distancia de fábricas a centros de distribución (bodegas)
Dist_fb = {}
for f in FABRICAS:
    coord_i = CoordenaddasCiudad[f]
    for b in BODEGAS:
        coord_j = CoordenaddasCiudad[b]
        distancia = calcular_distancia(coord_i, coord_j)
        Dist_fb[f,b] = distancia

# Calcular Dist_jk: Distancia de centros de distribución a tiendas
Dist_bt = {}
for b in BODEGAS:
    coord_j = CoordenaddasCiudad[b]
    for t in TIENDAS:
        coord_k = CoordenadasTiendas[t]
        distancia = calcular_distancia(coord_j, coord_k)
        Dist_bt[b,t] = distancia

# Otros parámetros (asegúrate de definirlos si aún no lo has hecho)
PesoUnidad = 2.114  # kg
CostoInterCiudad = 1270  # pesos por kg-km: El costo por kilogramo por kilometro es 1XXX (1270) pesos por kilogramo y cada unidad pesa 2.YYY (2.114) kilogramos.
CostoIntraCiudad = 2270  # pesos por unidad: El costo de distribuir una unidad al interior de las ciudades considerarlo igual a 2XXX (2270) pesos

N = 210 # Envíos desde fábricas a centros de distribución deben ser mayores a N unidades. El valor de M debe ser mayor o igual a la demanda más baja, que en este caso es 210 unidades (demandadas por Tunja).

M = 4 # Envíos desde centros de distribución a los vendedores al detal (ciudades) deben ser mayores a M unidades. 


# Variables continuas:
# X es la cantidad de unidades enviadas desde la fábrica f a la bodega b
X = model.addVars(FABRICAS, BODEGAS, vtype=GRB.INTEGER, name='X')
# Y es la cantidad de unidades enviadas desde la bodega b a la tienda t
Y = model.addVars(BODEGAS, TIENDAS, vtype=GRB.INTEGER, name='Y')

# Variables binarias
# Z es una variable binaria que indica si se envían unidades desde la fábrica f a la bodega b
Z = model.addVars(FABRICAS, BODEGAS, vtype=GRB.BINARY, name='Z')
# W es una variable binaria que indica si se envían unidades desde la bodega b a la tienda t
W = model.addVars(BODEGAS, TIENDAS, vtype=GRB.BINARY, name='W')

# # Función Objetivo

# Costo desde ciudad de fábricas a ciudad de centros de distribución en la misma ciudad
costoTransporteFabricaBodegasIntraCiudad = gp.quicksum(
    X[f,b] * Dist_fb[f,b] * CostoIntraCiudad
    for f in FABRICAS for b in BODEGAS if b == f
)

# Costo desde ciudad de fábricas a ciudad de centros de distribución en distinta ciudad
costoTransporteFabricaBodegasInterCiudad = gp.quicksum(
    X[f,b] * Dist_fb[f,b] * PesoUnidad * CostoInterCiudad
    for f in FABRICAS for b in BODEGAS if b != f
)

costoTransporteFabricaBodegas = costoTransporteFabricaBodegasIntraCiudad + costoTransporteFabricaBodegasInterCiudad

# Costo desde ciudad de centro de distribución a ciudad de tienda en la misma ciudad
costoTransporteBodegasTiendasIntraCiudad = gp.quicksum(
    Y[b,t] * Dist_bt[b,t] * CostoIntraCiudad
    for b in BODEGAS for t in TIENDAS if b == ciudadDeTiendaDict[t]
)

# Costo desde ciudad de centro de distribución a ciudad de tienda en distinta ciudad
costoTransporteBodegasTiendasInterCiudad = gp.quicksum(
    Y[b,t] * Dist_bt[b,t] * PesoUnidad * CostoInterCiudad
    for b in BODEGAS for t in TIENDAS if b != ciudadDeTiendaDict[t]
)

costoTransporteBodegasTiendas = costoTransporteBodegasTiendasIntraCiudad + costoTransporteBodegasTiendasInterCiudad

# Establecer la función objetivo
model.setObjective(costoTransporteFabricaBodegas + costoTransporteBodegasTiendas, GRB.MINIMIZE)

# # Restricciones

# Restricción de Capacidad de Producción de las Fábricas:
for f in FABRICAS:    
    # "Como complemento del punto uno debe asegurarse que cada una de las fábricas produzca al menos el 80% de su capacidad máxima de suministro y la cantidad mínima a transportar entre cualquier dos nodos debe ser mayor al valor de mínimo demanda total de un centro de demanda (ciudad)."
    model.addConstr(
        gp.quicksum(X[f,b] for b in BODEGAS) >= 0.8 * Capacidad[f],
        name=f'ProdMin_{f}'
    )    
    # No exceder la capacidad de producción
    model.addConstr(
        gp.quicksum(X[f,b] for b in BODEGAS) <= Capacidad[f],
        name=f'ProdMax_{f}'
    )

# Restricción de Balance en los Centros de Distribución:
# la cantidad de unidades enviadas desde las fábricas a los centros de distribución debe ser igual a la cantidad de unidades enviadas desde los centros de distribución a los vendedores al detal
for b in BODEGAS:
    model.addConstr(
        gp.quicksum(X[f,b] for f in FABRICAS) >= gp.quicksum(Y[b,t] for t in TIENDAS),
        name=f'BalanceCD_{b}'
    )

# Satisfacción de la Demanda:
# La cantidad enviada a una tienda debe ser igual a la demanda de esa tienda
for t in TIENDAS:
    model.addConstr(
        gp.quicksum(Y[b,t] for b in BODEGAS) == DemandasTiendas[t],
        name=f'Demanda_{t}'
    )

# Envíos Mínimos y Variables Binarias:
# Envíos desde fábricas a centros de distribución deben ser mayores a N unidades y menores o iguales a la capacidad de producción de la fábrica
for f in FABRICAS:
    for b in BODEGAS:
        # Si se envían unidades desde la fábrica f a la bodega b, entonces Z[f,b] = 1
        # Si Z[f,b] = 1, entonces X[f,b] >= N, exite una cota inferior
        # Si Z[f,b] = 0, entonces X[f,b] >= 0, quita la cota inferior
        model.addConstr(
            X[f,b] >= N * Z[f,b],
            name=f'MinEnvioFabrica_{f}_{b}'
        )
        # Si se envían unidades desde la fábrica f a la bodega b, entonces Z[f,b] = 1
        # Si Z[f,b] = 1, entonces X[f,b] <= Capacidad[f], exite una cota superior
        # Si Z[f,b] = 0, entonces X[f,b] <= 0, quita la cota superior
        model.addConstr(
            X[f,b] <= Capacidad[f] * Z[f,b],
            name=f'MaxEnvioFabrica_{f}_{b}'
        )

# Envíos desde centros de distribución a los vendedores al detal (ciudades) deben ser mayores a M unidades o menores o iguales a la demanda de la tienda
for b in BODEGAS:
    for t in TIENDAS:
        # Si se envían unidades desde la bodega b a la tienda t, entonces W[b,t] = 1
        # Si W[b,t] = 1, entonces Y[b,t] >= M, exite una cota inferior
        # Si W[b,t] = 0, entonces Y[b,t] >= 0, quita la cota inferior
        model.addConstr(
            Y[b,t] >= M * W[b,t],
            name=f'MinEnvioCD_{b}_{t}'
        )
        # Si se envían unidades desde la bodega b a la tienda t, entonces W[b,t] = 1
        # Si W[b,t] = 1, entonces Y[b,t] <= DemandasTiendas[t], exite una cota superior
        # Si W[b,t] = 0, entonces Y[b,t] <= 0, quita la cota superior
        model.addConstr(
            Y[b,t] <= DemandasTiendas[t] * W[b,t],
            name=f'MaxEnvioCD_{b}_{t}'
        )

# # Optimizar el modelo
model.update()
model.optimize()

# # Resultados
# Imprimir la solución
if model.status == GRB.OPTIMAL:
    print()
    for f in FABRICAS:
        for b in BODEGAS:
            if X[f,b].x > 0.5:
                print(f'Se envían {X[f,b].x:.0f} unidades desde la fábrica {f} a la bodega {b}')
    print()
    for b in BODEGAS:
        for t in TIENDAS:
            if Y[b,t].x > 0.5:
                print(f'Se envían {Y[b,t].x:.0f} unidades desde la bodega {b} a la tienda {t}')
    print()
    print(f'Costo Total: ${model.objVal:,.2f}')