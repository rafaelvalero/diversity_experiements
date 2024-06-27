"""
https://github.com/ArnaoutLab/diversity?tab=readme-ov-file#similarity-sensitive-diversity
https://arxiv.org/abs/1404.6520

A need for diversity measures for meta and subcommunities Throughout, we consider a
metacommunity divided into subcommunities. We seek measures of alpha (within-subcommunity)
diversity and beta (between-subcommunity) diversity, as well as gamma (total metacommunity)
diversity, and we further seek to partition the metacommunity diversity into measurements for
individual subcommunities.
"""
from greylock import Metacommunity
import pandas as pd
import numpy as np

labels_2b = ("ladybug", "bee", "butterfly", "lobster", "fish", "turtle", "parrot", "llama", "orangutan")

counts_2b_1 = pd.DataFrame(
    {
        "Subcommunity_2b_1": [1, 1, 1, 1, 0, 0, 0, 0, 0],  # invertebrates
        "Subcommunity_2b_2": [0, 0, 0, 0, 1, 1, 1, 1, 1],  #   vertebrates
    },
    index=labels_2b
)

metacommunity_2b_1 = Metacommunity(counts_2b_1)

output = metacommunity_2b_1.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output



counts_2b_1 = pd.DataFrame(
    {
        "Subcommunity_2b_1": [2, 2, 2, 2, 1, 1, 1, 1, 1],  # invertebrates
        "Subcommunity_2b_2": [ 2, 2, 2, 2, 0, 0, 0, 0, 0],  #   vertebrates
        "Subcommunity_2b_3": [1, 1, 1, 1, 1, 1, 1, 1, 1],  # vertebrates
        "Subcommunity_2b_4": [1, 0, 0, 0, 0, 0, 0, 0, 0],  # vertebrates

    },
    index=labels_2b
)

metacommunity_2b_1 = Metacommunity(counts_2b_1)

output = metacommunity_2b_1.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison1.csv")


counts_2b_1 = pd.DataFrame(
    {
        "Subcommunity_2b_1": [6, 5, 5, 5, 2, 2, 2, 2, 2],  # invertebrates

    },
    index=labels_2b
)

metacommunity_2b_1 = Metacommunity(counts_2b_1)

output = metacommunity_2b_1.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison2.csv")


counts_2b_1 = pd.DataFrame(
    {
        "Subcommunity_2b_1": [1, 0, 0, 0, 0, 0, 0, 0, 0],  # invertebrates

    },
    index=labels_2b
)

metacommunity_2b_1 = Metacommunity(counts_2b_1)

output = metacommunity_2b_1.to_dataframe(viewpoint=[0, 1, 2, np.inf])
output.to_csv("comparison3.csv")