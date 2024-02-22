import rdflib
from rdflib import Graph
import folium
import random
import geopy.distance





def visualize_data(data, latitude_user, longitude_user, perimetre_user):

    coords_user = (latitude_user, longitude_user)

    m = folium.Map([latitude_user, longitude_user])

    # Afficher les résultats
    for row in data:
        name = row.name
        lat = row.lat
        lon = row.lon

        coords_resto = (row.lat, row.lon)
        distance = int(geopy.distance.geodesic(coords_user, coords_resto).km)

        popup_description = name + "\n\n" + "distance en km :" + str(distance)

        folium.Marker(
            location=[lat, lon],
            tooltip=popup_description,
            popup=popup_description,
            icon=folium.Icon(color="blue"),
        ).add_to(m)


    #le radius est le rayon en metres
    folium.Circle(
        location=[latitude_user, longitude_user],
        radius=perimetre_user,
        color="black",
        weight=1,
        fill_opacity=0.6,
        opacity=1,
        fill_color="green",
        fill=False,  # gets overridden by fill_color
        popup="{} meters".format(perimetre_user),
        tooltip="I am in meters",
    ).add_to(m)

    folium.Marker(
        location=[latitude_user, longitude_user],
        tooltip="Votre position",
        popup="Votre position",
        icon=folium.Icon(color="red"),
    ).add_to(m)

    return m
