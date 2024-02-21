from extract_data import data
from cli import cli_test
from visualisation_data import visualize_data


cli_test(data)
m = visualize_data(data)
m.save("test_print1.html")

"""

À FAIRE :

- proposer de demander le type de moment dans le cli
- variabiliser la source de données
- voir pyroot libre pour les itinéraires
- conversion méridien en mètres
- rajouter addresse, numéro, distance avec utilisateur
- modifier marqueur selon type d'établissement
"""