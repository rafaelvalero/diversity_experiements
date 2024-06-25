"""
Measurements of diversity:
Implementation in python of diversity metrics --> Ecopy: https://ecopy.readthedocs.io/en/latest/diversity.html
     * Nate Lemoine, & Matt Gregory. (2015). ecopy: First release (v0.8). Zenodo. https://doi.org/10.5281/zenodo.29232
"""

import main
import utils

varespec = utils.load_data('varespec')
shannonH = main.diversity(varespec, 'shannon')