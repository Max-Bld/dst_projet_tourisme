import rdflib
from rdflib import Graph
import folium
import random
import geopy.distance


latitude_user = random.uniform(47.9,49.5)
longitude_user = random.uniform(5.0,5.8)

coords_user = (latitude_user, longitude_user)

def visualize_data(data):


    m = folium.Map([49, 5])

    # Afficher les résultats
    for row in data:
        name = row.name
        lat = row.lat
        lon = row.lon

        coords_resto = (row.lat, row.lon)
        distance = geopy.distance.geodesic(coords_user, coords_resto).km

        popup_description = name + "\n\n" + "distance en km :" + str(distance)

        folium.Marker(
            location=[lat, lon],
            tooltip=popup_description,
            popup=popup_description,
            icon=folium.Icon(color="blue"),
        ).add_to(m)


    radius = 10000 #chercher comment convertir les méridiens de périmetre en metres
    folium.Circle(
        location=[latitude_user, longitude_user],
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

    folium.Marker(
        location=[latitude_user, longitude_user],
        tooltip="Votre position",
        popup="Votre position",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    return m
