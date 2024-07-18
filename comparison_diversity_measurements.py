"""
https://github.com/ArnaoutLab/diversity?tab=readme-ov-file#similarity-sensitive-diversity
https://arxiv.org/abs/1404.6520

"""

from greylock import Metacommunity
import pandas as pd
import numpy as np

from main import diversity

data = pd.DataFrame({"example_1": [30, 1, 1, 1, 1, 1],
                     "example_2": [6, 6, 6, 6, 6, 5],
                     "example_3": [2, 0, 0, 0, 0, 0],
                     "example_4": [2, np.nan, np.nan, np.nan, np.nan, np.nan],
                     "example_5": [1, 1, np.nan, np.nan, np.nan, np.nan],
                     "example_6": [np.nan, 1, np.nan, np.nan, np.nan, np.nan],
                     "example_7": [1, 1, 0, 0, 0, 0],
                     },
                    index=["apple", "orange", "banana", "pear", "blueberry", "grape"])

print(data)

list_of_diversity_metrics_conditions = [{'method': 'spRich',
                                         'num_equiv': True},
                                        {'method': 'shannon',
                                         'num_equiv': True},
                                        {'method': 'simpson',
                                         'num_equiv': True},
                                        {'method': 'dominance',
                                         'num_equiv': True},
                                        ]

report_list = []
for diversity_metric in list_of_diversity_metrics_conditions:
    print(diversity_metric)
    aux = diversity(data.T.to_numpy(),
                    method=diversity_metric['method'],
                    num_equiv=diversity_metric['num_equiv'],
                    breakNA=False
                    )
    aux = pd.DataFrame(aux, index=data.columns, columns=[diversity_metric['method']])
    report_list.append(aux)

output = pd.concat(report_list, axis=1)
print(output)

""" 
Subcommittees
"""
data = pd.DataFrame({"example_2": [4, 6, 6, 6, 6, 5],
                     "example_4": [2, 0, 0, 0, 0, 0],
                     "example_7": [1, 1, 0, 0, 0, 0], },
                    index=["apple", "orange", "banana", "pear", "blueberry", "grape"])

print(data)

metacommunity = Metacommunity(data)

output = metacommunity.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison1.csv")

metacommunity.subcommunity_diversity(viewpoint=1,
                                     measure='normalized_rho')

""" 
Subcommittees
"""
data = pd.DataFrame({"example_2": [6 - 1, 6 - 1, 6, 6, 6, 6],
                     "example_7": [1, 1, 0, 0, 0, 0], },
                    index=["apple", "orange", "banana", "pear", "blueberry", "grape"])

print(data)

metacommunity = Metacommunity(data)

output = metacommunity.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison2.csv")

metacommunity.subcommunity_diversity(viewpoint=1,
                                     measure='normalized_rho')

for viewpoint in [0, 1, 2, np.inf]:
    print(metacommunity.subcommunity_diversity(viewpoint=viewpoint,
                                               measure='normalized_rho'))

measure = 'normalized_rho'
metacommunity.components.numerators

""" 
Subcommittees
"""
data = pd.DataFrame({"example_2": [6 - 2, 6 - 1, 6, 6, 6, 6],
                     "example_7": [2, 1, 0, 0, 0, 0], },
                    index=["apple", "orange", "banana", "pear", "blueberry", "grape"])

print(data)

metacommunity = Metacommunity(data)

output = metacommunity.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison3.csv")

""" 
Subcommittees
"""
data = pd.DataFrame({"example_2": [1, 0, 0],
                     "example_7": [1, 1, 0],
                     "example_8": [1, 0, 1]},
                    index=["apple", "orange", "banana"])

print(data)

metacommunity = Metacommunity(data)

output = metacommunity.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison4.csv")

""" 
Subcommittees
"""
data = pd.DataFrame({"example_2": [10, 2, 2],
                     "example_7": [1, 1, 0],
                     "example_11": [2, 0, 0],
                     "example_8": [1, 0, 1],
                     "example_10": [0, 1, 1],
                     "example_9": [0, 0, 2],
                     },

                    index=["apple", "orange", "banana"])

print(data)

metacommunity = Metacommunity(data)

output = metacommunity.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison5.csv")
