"""
Borrow from Lemoine, & Matt Gregory. (2015). ecopy: First release (v0.8). Zenodo. https://doi.org/10.5281/zenodo.29232
"""
import pandas as pd

def load_data(x):
    """Loads data from online repository. Requires internet."""
    path = 'https://github.com/Auerilas/ecopy-data/raw/master/data/{0}.csv'
    downloadPath = path.format(x)
    loaded = pd.read_csv(downloadPath)
    return loaded
