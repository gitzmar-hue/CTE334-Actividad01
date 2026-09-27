"""
CTE-334 - Desarrollo de Aplicaciones SIG
Actividad 01 - Distancia y direccion entre dos puntos geograficos
Autor: Gitzy Yissel Andrade Andrade
Numero de cuenta: 20161030363
"""

import math

RADIO_TIERRA_KM = 6371.0088


def validar_coordenadas(latitud, longitud):
    """Comprueba que la latitud y la longitud esten dentro de los rangos
    geograficos permitidos (-90 <= latitud <= 90, -180 <= longitud <= 180).

    Retorna True si ambos valores son validos, False en caso contrario.
    """
    return -90 <= latitud <= 90 and -180 <= longitud <= 180


def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia entre dos puntos geograficos aplicando la
    formula de Haversine. Recibe las coordenadas en grados decimales y
    retorna la distancia resultante en kilometros.
    """
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) ** 2
         + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)

    distancia = 2 * RADIO_TIERRA_KM * math.asin(math.sqrt(a))
    return distancia


def determinar_direccion(lat1, lon1, lat2, lon2):
    """Compara las latitudes y longitudes del Punto A y el Punto B para
    establecer la ubicacion general de B respecto a A. Retorna uno de los
    nueve resultados definidos en la guia de la actividad.
    """
    if lat2 > lat1 and lon2 == lon1:
        return "Norte"
    elif lat2 < lat1 and lon2 == lon1:
        return "Sur"
    elif lat2 == lat1 and lon2 > lon1:
        return "Este"
    elif lat2 == lat1 and lon2 < lon1:
        return "Oeste"
    elif lat2 > lat1 and lon2 > lon1:
        return "Noreste"
    elif lat2 > lat1 and lon2 < lon1:
        return "Noroeste"
    elif lat2 < lat1 and lon2 > lon1:
        return "Sureste"
    elif lat2 < lat1 and lon2 < lon1:
        return "Suroeste"
    else:
        return "Misma ubicación"


def clasificar_distancia(distancia):
    """Clasifica la distancia (en km) segun los intervalos establecidos
    en la guia de la actividad, respetando los valores frontera.
    """
    if distancia < 1:
        return "Muy cercano"
    elif distancia < 10:
        return "Cercano"
    elif distancia < 50:
        return "Distancia media"
    else:
        return "Distante"


def main():
    print("CTE-334 - Análisis básico entre dos puntos geográficos")
    print()
    print("Ingrese las coordenadas del Punto A")
    lat_a = float(input("Latitud: "))
    lon_a = float(input("Longitud: "))
    print()
    print("Ingrese las coordenadas del Punto B")
    lat_b = float(input("Latitud: "))
    lon_b = float(input("Longitud: "))

    if not (validar_coordenadas(lat_a, lon_a) and validar_coordenadas(lat_b, lon_b)):
        print()
        print("ERROR: coordenada fuera del rango geográfico permitido.")
        return

    distancia = calcular_distancia(lat_a, lon_a, lat_b, lon_b)
    direccion = determinar_direccion(lat_a, lon_a, lat_b, lon_b)
    clasificacion = clasificar_distancia(distancia)

    print()
    print("-" * 40)
    print("RESULTADO DEL ANÁLISIS")
    print("-" * 40)
    print(f"Distancia: {distancia:.3f} km")
    print(f"Dirección: {direccion}")
    print(f"Clasificación: {clasificacion}")
    print("-" * 40)


if __name__ == "__main__":
    main()
