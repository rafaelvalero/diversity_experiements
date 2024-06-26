"""
Borrow from Lemoine, & Matt Gregory. (2015). ecopy: First release (v0.8). Zenodo. https://doi.org/10.5281/zenodo.29232

https://github.com/ArnaoutLab/diversity?tab=readme-ov-file#similarity-sensitive-diversity
https://arxiv.org/abs/1404.6520

"""

import numpy as np
from pandas import DataFrame, Series


def diversity(x, method='shannon', breakNA=True):
    '''
    Docstring for function ecopy.diversity
    ========================
    Computes a given diversity index for a site x species matrix.
        All indices computed along rows (axis = 1)

    Use
    ----
    diversity(x, method='shannon', breakNA=True, num_equiv=True)

    Returns a numpy.ndarray or a pandas.Series

    Parameters
    ----------
    x:  numpy array or pandas dataframe with observations as rows
        and descriptors as columns
    method: a method used for calculating species diversity
        shannon: Shannon's H
            H = -sum( p_i * log(p_i) )
            where p_i is relative abundance of species i
        gini-simpson: Gini-Simpson
            \lambda = 1 - sum( p_i^2 )
        simpson: Simpson's D
            \lambda = sum(p_i^2)
        dominance: Dominance index
            \lambda = max(p_i)
        spRich: Species richness
            \lambda = Number of non-zero observations
        even: Evenness of a sample. This is Shannon's H divided by the
            log of species richness
    breakNA: should the process halt if the matrix contains any NAs?
        if False, then NA's undergo pairwise deletion during distance calculation,
        such that when calculating the distance between two rows, if any
        species is missing from a row, that species is removed from both rows

    Example
    --------
    import ecopy as ep
    varespec = ep.load_data('varespec')
    
    div = ep.diversity(varespec, 'shannon')
    '''
    listofmethods = ['shannon', 'gini-simpson',
                     'inverse-simpson',
                     'simpson',
                     'dominance',
                     'spRich',
                     'even']
    if not isinstance(breakNA, bool):
        msg = 'remove NA argument must be boolean'
        raise ValueError(msg)
    if method not in listofmethods:
        msg = 'method argument {0!s} is not an accepted metric'.format(method)
        raise ValueError(msg)
    if not isinstance(x, (DataFrame, np.ndarray)):
        msg = 'x argument must be a numpy array or pandas dataframe'
        raise ValueError(msg)
    if isinstance(x, DataFrame):
        if (x.dtypes == 'object').any():
            msg = 'DataFrame can only contain numeric values'
        if breakNA:
            if x.isnull().any().any():
                msg = 'DataFrame contains null values'
                raise ValueError(msg)
        if (x < 0).any().any():
            msg = 'DataFrame contains negative values'
            raise ValueError(msg)
        z = np.array(x, 'float')
    if isinstance(x, np.ndarray):
        if breakNA:
            if np.isnan(np.sum(x)):
                msg = 'Array contains null values'
                raise ValueError(msg)
        if (x < 0).any():
            msg = 'Array contains negative values'
            raise ValueError(msg)
        z = np.array(x, 'float')
    z = z / z.sum(axis=1)[:, np.newaxis]
    if method == 'shannon':
        div = np.apply_along_axis(shannonFunc, 1, z)
        return div
    if method == 'gini-simpson':
        div = np.apply_along_axis(simpson, 1, z)
        return 1. - div
    if method == 'simpson':
        div = np.apply_along_axis(simpson, 1, z)
        return div
    if method == 'inverse-simpson':
        div = np.apply_along_axis(simpson, 1, z)
        return 1. / div
    if method == 'dominance':
        div = np.apply_along_axis(dom, 1, z)
        return div
    if method == 'spRich':
        div = np.apply_along_axis(richness, 1, z)
        return div
    if method == 'even':
        div = np.apply_along_axis(evenFunc, 1, z)
        return div


def shannonFunc(y):
    """
    Example from https://www.omnicalculator.com/ecology/shannon-index#:~:text=For%20example%2C%20the%20index%20for,values%20between%200%20and%201.
    >>> import numpy as np
    >>> data_example = {'scarlet_macaw': 5,\
                      'blue_morpho_butterfly': 12,\
                      'capybara': 2,\
                      'three_toed_sloth': 5,\
                      'jaguar': 1,\
                      }
    >>> shannonFunc(np.array([i for i in data_example.values()]))
    np.float64(1.326893693551525)
    """
    notabs = ~np.isnan(y)
    t = y[notabs] / np.sum(y[notabs])
    t = t[t != 0]
    H = -np.sum(t * np.log(t))
    return H


def giniFunc(y):
    notabs = ~np.isnan(y)
    t = y[notabs] / np.sum(y[notabs])
    D = 1 - np.sum(t ** 2)
    return D


def simpson(y):
    """
    Example from https://www.studysmarter.co.uk/explanations/biology/ecology/simpsons-diversity-index/
    >>> import numpy as np
    >>> data_adelaide_river = {'agile_wallaby' : 5000,\
    'barramundi':40000,\
    'black_necked_stork':500,\
    'bull_shark':750,\
    'saltwater_crocodile':3000}
    >>> simpson(np.array([i for i in data_adelaide_river.values()]))
    np.float64(0.6739931459197609)
    >>> data_pantanal_wetlands = {'capybara' : 1000000,\
    'giant_anteater':250,\
    'giat_river_otter':500,\
    'jaguar':400,\
    'mash_deer':10000,\
    'ocelot':500,\
    'yacare_caiman':1000000}
    >>> simpson(np.array([i for i in data_pantanal_wetlands.values()]))
    np.float64(0.4942503933180924)
    """
    notabs = ~np.isnan(y)
    t = y[notabs] / np.sum(y[notabs])
    D = np.sum(t ** 2)
    return D


def dom(y):
    notabs = ~np.isnan(y)
    t = y[notabs] / np.sum(y[notabs])
    D = np.max(t)
    return D


def richness(y):
    """
    Example from https://www.omnicalculator.com/ecology/shannon-index#:~:text=For%20example%2C%20the%20index%20for,values%20between%200%20and%201.
    >>> import numpy as np
    >>> data_example = {'scarlet_macaw': 5,\
                      'blue_morpho_butterfly': 12,\
                      'capybara': 2,\
                      'three_toed_sloth': 5,\
                      'jaguar': 1}
    >>> richness(np.array([i for i in data_example.values()]))
    5.0
    """
    notabs = ~np.isnan(y)
    t = y[notabs]
    D = np.sum(t != 0)
    return float(D)


def evenFunc(y):
    notabs = ~np.isnan(y)
    t = y[notabs] / np.sum(y[notabs])
    n = float(np.sum(t != 0))
    t = t[t != 0]
    H = -np.sum(t * np.log(t))
    return H / np.log(n)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
