import numpy as np

def log3(x):
    """
    Computes log base 3 of x

    INPUT: 
    x - scalar or array-like input

    OUTPUT: log base 3 of x
    """
    return np.log10(x) / np.log10(3)
