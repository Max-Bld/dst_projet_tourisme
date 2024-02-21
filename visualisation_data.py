from cli import data, perimetre 
import rdflib
from rdflib import Graph
import folium



m = folium.Map([49, 5])

# Afficher les résultats
for row in data:
    name = row.name
    lat = row.lat
    lon = row.lon

    folium.Marker(
        location=[lat, lon],
        tooltip=name,
        popup=name,
    ).add_to(m)


radius = 10000 #chercher comment convertir les méridiens de périmetre en metres
folium.Circle(
    location=[49, 5],
    radius=radius,
    color="black",
    weight=1,
    fill_opacity=0.6,
    opacity=1,
    fill_color="green",
    fill=False,  # gets overridden by fill_color
    popup="{} meters".format(radius),
    tooltip="I am in meters",
).add_to(m)

