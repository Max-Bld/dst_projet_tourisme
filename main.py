from extract_data import data
from cli import cli_test
from visualisation_data import visualize_data


cli_test(data)
m = visualize_data(data)
m.save("test_print2.html")

