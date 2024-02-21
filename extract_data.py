import rdflib
from rdflib import Graph

# Charger les données TTL dans un graph RDF
g = Graph()
g.parse("data/flux-19287-202401180748.ttl")

# Requête SPARQL pour extraire les informations sur la localisation
q = """
    SELECT ?name ?lat ?lon  
    WHERE {
        ?restaurant rdf:type core:Restaurant.
        ?restaurant rdfs:label ?name.
        ?restaurant core:isLocatedAt ?localisationuri.
        ?localisationuri schema1:geo ?geouri.
        ?geouri schema1:latitude ?lat ; schema1:longitude ?lon.
        
    }
"""

results = g.query(q)


for i in results:
    print(i.lat)