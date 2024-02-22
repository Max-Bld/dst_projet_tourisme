from libraries.extract_data import data
from libraries.cli import cli_test
from libraries.visualisation_data import visualize_data


latitude_user, longitude_user, perimetre_user = cli_test(data)
m = visualize_data(data, latitude_user, longitude_user, perimetre_user)
m.save("display/test_print9.html")

