# CTE-334 – Actividad 01: Distancia y dirección entre dos puntos geográficos

**Estudiante:** Gitzy Yissel Andrade Andrade
**Número de cuenta:** 20161030363

## Descripción

Programa de consola en Python que recibe las coordenadas (latitud y longitud en
grados decimales) de dos puntos geográficos, un Punto A (ubicación inicial) y un
Punto B (ubicación de destino), valida que dichas coordenadas estén dentro de los
rangos geográficos permitidos y, si son válidas, calcula:

- La **distancia** aproximada entre ambos puntos (fórmula de Haversine).
- La **dirección** general de B respecto a A.
- Una **clasificación** de esa distancia.

## Requisitos y forma de ejecución

- Python 3 (no requiere ninguna librería externa; solo se usa el módulo estándar `math`).

Desde la consola, ubicado en la carpeta del proyecto:

```bash
python3 actividad01.py
```

El programa solicitará en orden la latitud y longitud del Punto A y luego del
Punto B, y mostrará el resultado del análisis en pantalla.

## Funciones principales

| Función | Responsabilidad |
|---|---|
| `validar_coordenadas(latitud, longitud)` | Comprueba que la latitud esté entre -90 y 90, y la longitud entre -180 y 180. Retorna `True` o `False`. |
| `calcular_distancia(lat1, lon1, lat2, lon2)` | Aplica la fórmula de Haversine (convirtiendo previamente los grados a radianes) y retorna la distancia en kilómetros, usando R = 6371.0088 km. |
| `determinar_direccion(lat1, lon1, lat2, lon2)` | Compara las latitudes y longitudes de A y B y retorna una de las nueve ubicaciones generales posibles (Norte, Sur, Este, Oeste, Noreste, Noroeste, Sureste, Suroeste o Misma ubicación). |
| `clasificar_distancia(distancia)` | Clasifica la distancia obtenida en Muy cercano (<1 km), Cercano ([1,10) km), Distancia media ([10,50) km) o Distante (≥50 km). |

## Caso propio (dos sitios reales de Honduras)

```
Nombre del sitio A: Tegucigalpa, Parque Central
Coordenadas: 14.0995, -87.2063

Nombre del sitio B: La Ceiba, Parque Central
Coordenadas: 15.7597, -86.7822

Distancia obtenida: 190.146 km
Dirección obtenida: Noreste
Clasificación obtenida: Distante
```

## Decisiones de implementación

Para `determinar_direccion()` se optó por comparar explícitamente los nueve
casos posibles (combinaciones de mayor/menor/igual latitud con mayor/menor/igual
longitud) mediante una cadena de condicionales, en lugar de construir el
resultado concatenando cadenas como "Norte" + "Este". Esto se decidió porque
combinaciones como "Sur" + "Oeste" no producen directamente el texto correcto
("Suroeste") por simple concatenación, y una cadena explícita de condicionales
resulta más clara, más fácil de verificar contra la tabla de la guía y menos
propensa a errores silenciosos que una lógica basada en abreviaturas o
diccionarios de traducción.
