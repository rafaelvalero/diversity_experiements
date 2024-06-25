"""
Measurements of diversity:
Implementation in python of diversity metrics --> Ecopy: https://ecopy.readthedocs.io/en/latest/diversity.html
     * Nate Lemoine, & Matt Gregory. (2015). ecopy: First release (v0.8). Zenodo. https://doi.org/10.5281/zenodo.29232
"""
import pandas as pd

from main import *
from utils import *

data = load_data('varespec')
shannonH = diversity(data, 'shannon')

list_of_diversity_metrics = ['shannon', 'gini-simpson', 'simpson', 'dominance', 'spRich', 'even']

report_list = []
for diversity_metric in list_of_diversity_metrics:
    print(diversity_metric)
    aux = diversity(data.T,
                    method=diversity_metric)
    aux = pd.DataFrame(aux, index=data.columns, columns = [diversity_metric])
    report_list.append(aux)

output = pd.concat(report_list, axis = 1)
print(output)