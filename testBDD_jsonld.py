# Créé par khadim, le 21/02/2024 en Python 3.7

#g.parse("C:/Users/khadi/Documents/Datascientest 2023-2024/2023-2024/Projet geo tourisme/flux-19287-202401260747.jsonld", format="jsonld")

from rdflib import Graph, BNode
from pymongo import MongoClient

def load_jsonld_to_mongodb(jsonld_file, database_name, collection_name, mongodb_uri, username=None, password=None):
    # Charger le graph RDF depuis le fichier JSON-LD
    g = Graph()
    g.parse(jsonld_file, format="json-ld")

    # Supprimer les triplets contenant des nœuds anonymes
    triplets_sans_bnodes = [(s, p, o) for s, p, o in g if not isinstance(s, BNode) and not isinstance(o, BNode)]

    # Créer une nouvelle connexion MongoDB
    client = MongoClient(mongodb_uri, username=username, password=password)

    # Sélectionner la base de données et la collection
    db = client[database_name]
    collection = db[collection_name]

    # Ajouter chaque triplet filtré à la base de données MongoDB
    for triplet in triplets_sans_bnodes:
        subject, predicate, obj = triplet
        doc = {"subject": str(subject), "predicate": str(predicate), "object": str(obj)}
        collection.insert_one(doc)

    # Afficher un message lorsque l'opération est terminée
    print("Les triplets ont été ajoutés à la base de données MongoDB.")

# Exemple d'utilisation
load_jsonld_to_mongodb(
    jsonld_file="C:/Users/khadi/Documents/Datascientest 2023-2024/2023-2024/Projet geo tourisme/flux-19287-202401260747.jsonld",
    database_name="Test_jsonld",
    collection_name="Col_Test_jsonld",
    mongodb_uri="mongodb://localhost:27017/",
    username="admin",
    password="pass"
)
