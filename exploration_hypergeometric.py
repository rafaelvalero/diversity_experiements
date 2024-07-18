"""
We could calculate the probability of the sample.
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_hypergeom.html
https://en.wikipedia.org/wiki/Hypergeometric_distribution

"""

from scipy.stats import multivariate_hypergeom
import numpy as np
import pandas as pd
from greylock import Metacommunity

"""
Sample simple cases
"""
population = [98, 2]
sample = [1, 1]
print(multivariate_hypergeom.pmf(x=sample, m=population, n=np.sum(sample)))
sample = [2, 0]
print(multivariate_hypergeom.pmf(x=sample, m=population, n=np.sum(sample)))
sample = [0, 2]
print(multivariate_hypergeom.pmf(x=sample, m=population, n=np.sum(sample)))
sample = population
print(multivariate_hypergeom.pmf(x=sample, m=population, n=np.sum(sample)))

"""Let explore vs rarity from greylock
"""

samples_list = [[2, 0],
                [1, 1],
                [0, 2],
                population]
"""
samples_list = [[2, 0],
                [1, 1],
                [0, 2]]
"""

list_ = []
for sample in samples_list:
    print(sample, multivariate_hypergeom.pmf(x=sample,
                                             m=population,
                                             n=np.sum(sample)))
    np.array(population) - np.array(sample)
    counts_1a = pd.DataFrame({"sample1": sample,
                              "rest_population": np.array(population) - np.array(sample)},
                             index=["apple", "orange"])
    metacommunity_1a = Metacommunity(counts_1a)
    dict_ = {}
    dict_['sample'] = sample
    dict_['probability'] = multivariate_hypergeom.pmf(x=sample,
                                                      m=population,
                                                      n=np.sum(sample))

    try:
        print(" Greylock ")
        print(metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                      measure="rho")[0])
        print(metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                      measure="normalized_rho")[0])
        dict_['rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                               measure="rho")[0]
        dict_['normalized_rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                          measure="normalized_rho")[0]
        dict_['gamma'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                 measure="gamma")[0]
        dict_['normalized_alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                            measure="normalized_alpha")[0]
        dict_['alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                 measure="alpha")[0]
    except Exception as e:
        print(e)
    list_.append(dict_)
# comparing
comparison = pd.DataFrame(list_).round(2)
#comparison.round(2)
print(comparison)
