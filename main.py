from extract_data import data
from cli import cli_test
from visualisation_data import visualize_data


latitude_user, longitude_user, perimetre_user = cli_test(data)
m = visualize_data(data, latitude_user, longitude_user, perimetre_user)
m.save("test_print6.html")

