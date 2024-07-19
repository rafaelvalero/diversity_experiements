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
    print(" Greylock ")
    try:
        dict_['rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                               measure="rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                          measure="normalized_rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['gamma'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                 measure="gamma")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                            measure="normalized_alpha")[0]
    except Exception as e:
        print(e)
    try:
        dict_['alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=0,
                                                                 measure="alpha")[0]
    except Exception as e:
        print(e)

    list_.append(dict_)
# comparing
comparison = pd.DataFrame(list_).round(2)
#comparison.round(2)
print(comparison)

"""
let create another examples
"""
viewpoint = 0
population = [89, 10, 1]

samples_list = [[2, 0, 0],
                [1, 1, 0],
                [0, 2, 0],
                [1, 1, 1],
                [50, 1, 0],
                [50, 1, 1],
                [0, 0, 1],
                [9, 1, 0], ]
#population]

list_ = []
for sample in samples_list:
    print(sample, multivariate_hypergeom.pmf(x=sample,
                                             m=population,
                                             n=np.sum(sample)))
    counts_1a = pd.DataFrame({"sample1": sample,
                              "rest_population": np.array(population) - np.array(sample)},
                             index=["apple", "orange", "tomatoes"])
    metacommunity_1a = Metacommunity(counts_1a)
    dict_ = {}
    dict_['sample'] = sample
    dict_['probability'] = multivariate_hypergeom.pmf(x=sample,
                                                      m=population,
                                                      n=np.sum(sample))
    print(" Greylock ")
    try:
        dict_['rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                               measure="rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                          measure="normalized_rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['gamma'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                 measure="gamma")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                            measure="normalized_alpha")[0]
    except Exception as e:
        print(e)

    try:
        dict_['potential_alpha_gap'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                               measure="normalized_alpha")[0]

        if np.sum(metacommunity_1a.counts.sample1) >= metacommunity_1a.counts.sample1.shape[0]:
            dict_['potential_alpha_gap'] = (metacommunity_1a.counts.sample1.shape[0] -
                                            dict_['normalized_alpha']) / \
                                           metacommunity_1a.counts.sample1.shape[0]
        # here just the number of people available
        elif np.sum(metacommunity_1a.counts.sample1) < metacommunity_1a.counts.sample1.shape[0]:
            dict_['potential_alpha_gap'] = (np.sum(metacommunity_1a.counts.sample1) -
                                            dict_['normalized_alpha']) / \
                                           np.sum(metacommunity_1a.counts.sample1)

    except Exception as e:
        print(e)
    try:
        dict_['alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                 measure="alpha")[0]
    except Exception as e:
        print(e)

    list_.append(dict_)
# comparing
comparison_v2 = pd.DataFrame(list_).round(2)
#comparison.round(2)
print(comparison_v2)
comparison_v2.to_csv('v2_examples.csv')
"""
Changing view points
"""
viewpoint = 1
population = [89, 10, 1]

samples_list = [[2, 0, 0],
                [1, 1, 0],
                [0, 2, 0],
                [1, 1, 1],
                [50, 1, 0],
                [50, 1, 1],
                [0, 0, 1],
                [9, 1, 0],
                population]

list_ = []
for sample in samples_list:
    print(sample, multivariate_hypergeom.pmf(x=sample,
                                             m=population,
                                             n=np.sum(sample)))
    counts_1a = pd.DataFrame({"sample1": sample,
                              "rest_population": np.array(population) - np.array(sample)},
                             index=["apple", "orange", "tomatoes"])
    metacommunity_1a = Metacommunity(counts_1a)
    dict_ = {}
    dict_['sample'] = sample
    dict_['probability'] = multivariate_hypergeom.pmf(x=sample,
                                                      m=population,
                                                      n=np.sum(sample))
    print(" Greylock ")
    try:
        dict_['rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                               measure="rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_rho'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                          measure="normalized_rho")[0]
    except Exception as e:
        print(e)
    try:
        dict_['gamma'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                 measure="gamma")[0]
    except Exception as e:
        print(e)
    try:
        dict_['normalized_alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                            measure="normalized_alpha")[0]
    except Exception as e:
        print(e)

    try:

        if np.sum(metacommunity_1a.counts.sample1) >= metacommunity_1a.counts.sample1.shape[0]:
            dict_['potential_alpha_gap'] = np.abs((metacommunity_1a.counts.sample1.shape[0] -
                                                   dict_['normalized_alpha']) / \
                                                  metacommunity_1a.counts.sample1.shape[0])
        # here just the number of people available
        elif np.sum(metacommunity_1a.counts.sample1) < metacommunity_1a.counts.sample1.shape[0]:
            dict_['potential_alpha_gap'] = np.abs((np.sum(metacommunity_1a.counts.sample1) -
                                                   dict_['normalized_alpha']) / \
                                                  np.sum(metacommunity_1a.counts.sample1))

    except Exception as e:
        print(e)
    try:
        dict_['alpha'] = metacommunity_1a.subcommunity_diversity(viewpoint=viewpoint,
                                                                 measure="alpha")[0]
    except Exception as e:
        print(e)

    list_.append(dict_)
# comparing
comparison_v3 = pd.DataFrame(list_).round(2)
#comparison.round(2)
print(comparison_v3)

comparison_v3.to_csv('v3_examples.csv')