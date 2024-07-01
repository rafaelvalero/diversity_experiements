"""
Here making comparable ecopy and greylock outputs.

https://github.com/ArnaoutLab/diversity?tab=readme-ov-file#similarity-sensitive-diversity
https://arxiv.org/abs/1404.6520

"""

import pandas as pd
from greylock import Metacommunity
from main import *

"""
create example
"""
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
print(diversity(counts_1a.T,\
          method='spRich',\
          num_equiv=True))
print('Shannon entropy')
print(metacommunity_1a.subcommunity_diversity(viewpoint=1, measure='alpha'))
print(np.exp(shannonFunc(counts_1a.values)))
print(diversity(counts_1a.T,
          method='shannon',
          num_equiv=True))
print('Gini-Simpson Index')
print(metacommunity_1a.subcommunity_diversity(viewpoint=2, measure='alpha'))
print(1/simpson(counts_1a.values))
print(diversity(counts_1a.T,
          method='',
          num_equiv=True))
print('Berger-Parker index')
print(metacommunity_1a.subcommunity_diversity(viewpoint=np.inf, measure='alpha'))
print(1/dom(counts_1a.values))
