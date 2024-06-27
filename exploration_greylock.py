"""

https://github.com/ArnaoutLab/diversity?tab=readme-ov-file#similarity-sensitive-diversity
https://arxiv.org/abs/1404.6520

"""


import pandas as pd
import numpy as np
from greylock import Metacommunity

from main import *

counts_1a = pd.DataFrame({"Dataset 1a": [30, 1, 1, 1, 1, 1]},
   index=["apple", "orange", "banana", "pear", "blueberry", "grape"])

metacommunity_1a = Metacommunity(counts_1a)

"""
Common diversity measures such as species richness, Shannon entropy,
 the Gini-Simpson index, and the Berger-Parker 
index have simple and natural relationships with Hill's indices 
at different values for the viewpoint parameter (
0,1 ,2 , inf , respectively).
"""
print('Richness')
print(metacommunity_1a.subcommunity_diversity(viewpoint=0, measure='alpha'))
print(richness(counts_1a.values))
print('Shannon entropy')
print(metacommunity_1a.subcommunity_diversity(viewpoint=1, measure='alpha'))
print(np.exp(shannonFunc(counts_1a.values)))
print('Gini-Simpson Index')
print(metacommunity_1a.subcommunity_diversity(viewpoint=2, measure='alpha'))
print(1/simpson(counts_1a.values))
#print(giniFunc(counts_1a.values))
print('Berger-Parker index')
print(metacommunity_1a.subcommunity_diversity(viewpoint=np.inf, measure='alpha'))
print(1/dom(counts_1a.values))

list_of_diversity_metrics = ['shannon', 'inverse-simpson', 'gini-simpson',
                             'simpson', 'dominance', 'spRich', 'even']

report_list = []
for diversity_metric in list_of_diversity_metrics:
    print(diversity_metric)
    aux = diversity(counts_1a.T,
                    method=diversity_metric)
    aux = pd.DataFrame(aux, index=counts_1a.columns, columns=[diversity_metric])
    report_list.append(aux)

output = pd.concat(report_list, axis=1)
print(output.T)

shannonFunc(counts_1a)


data_adelaide_river = {'agile_wallaby' : 5000,\
    'barramundi':40000,\
    'black_necked_stork':500,\
    'bull_shark':750,\
    'saltwater_crocodile':3000}
diversity(np.array( pd.DataFrame.from_dict(data_adelaide_river, orient ="index" ).T),
          method= 'gini-simpson')
diversity(np.array( pd.DataFrame.from_dict(data_adelaide_river, orient ="index" ).T),
          method= 'simpson')
shannonFunc(data_adelaide_river)
shannonFunc(counts_1a)

pd.DataFrame.from_dict(data_adelaide_river, orient ="index" )