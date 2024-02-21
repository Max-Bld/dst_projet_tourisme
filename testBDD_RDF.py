from rdflib import Graph, BNode
from pymongo import MongoClient

def load_rdf_to_mongodb(rdf_file, database_name, collection_name, mongodb_uri, username=None, password=None):
    # Charger le graph RDF depuis le fichier Turtle (TTL)
    g = Graph()
    g.parse(rdf_file, format="turtle")

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
load_rdf_to_mongodb(
    rdf_file="C:/Users/khadi/Documents/Datascientest 2023-2024/2023-2024/Projet geo tourisme/flux-19287-202401180748.ttl",
    database_name="Test_RDF",
    collection_name="Col_Test_RDF",
    mongodb_uri="mongodb://localhost:27017/",
    username="admin",
    password="pass"
)
