# Créé par khadi, le 21/02/2024 en Python 3.7

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 04:42:30 2024

@author: Khadim
"""

from rdflib import Graph
import folium

def get_user_location():
    print("Enter the latitude and longitude of the geographic point (separated by a space):")
    user_input = input("Example: 48.8566 2.3522 (Paris): ")
    try:
        latitude, longitude = map(float, user_input.split())
        return latitude, longitude
    except ValueError:
        print("Invalid input. Please enter valid latitude and longitude.")
        return get_user_location()

def query_graph_for_location(graph, latitude, longitude):
    # Your existing query logic goes here
    # ...

    # Example: Set name and description based on the query result
    name = "Place Name"  # Replace with actual query result
    description = "Description of the place"  # Replace with actual query result

    return name, description

def main():
    # Initialize the RDF graph
    g = Graph()
    g.parse("C:/Users/khadi/Documents/Datascientest 2023-2024/2023-2024/Projet geo tourisme/flux-19287-202401180748.ttl")

    # Get user location
    latitude, longitude = get_user_location()

    # Query the graph for the entered location
    name, description = query_graph_for_location(g, latitude, longitude)

    # Generate Folium map
    m = folium.Map([latitude, longitude], zoom_start=12)

    # Customize the map popup content with queried data
    html = f"""
        <h1> {name}</h1>
        <p>
        {description}
        </p>
        """

    folium.Marker(
        location=[latitude, longitude],
        tooltip=name,
        popup=folium.Popup(html, max_width=300),
        icon=folium.Icon(icon="home"),
    ).add_to(m)

    # Save the map as an HTML file
    m.save("dst_map_example.html")

if __name__ == "__main__":
    main()
