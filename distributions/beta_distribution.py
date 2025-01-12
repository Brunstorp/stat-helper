## For the fun of it I implemented the beta distribution from scratch
import numpy as np
from scipy.integrate import quad

def gamma_function(x):
    integrand = lambda t: t**(x-1) * np.exp(-t)
    result, _ = quad(integrand, 0, np.inf)
    return result