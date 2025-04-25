import pandas as pd
import csv
import folium
from folium.plugins import HeatMap

mapa = folium.Map(location=[-23.4425, -58.4438], zoom_start=6)

def get_coordinates(nombre_archivo):

    coordenadas = []

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
                
            latitud = float(fila['latitude'])
            longitud = float(fila['longitude'])
            coordenadas.append([latitud, longitud])
                
    return coordenadas

# Ejemplo de uso con tu nombre de archivo:
nombre_del_archivo_csv = 'map_data.csv'
lista_de_coordenadas = get_coordinates(nombre_del_archivo_csv)


# Agregar mapa de calor
HeatMap(lista_de_coordenadas).add_to(mapa)  

# Agregar marcadores
for ciudad in lista_de_coordenadas:
    folium.Marker(location=ciudad).add_to(mapa)

mapa.save('mapa_calor_paraguay.html')
print(lista_de_coordenadas)

