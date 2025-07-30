import numpy as np

def get_omegas3(deg):
    """
    Reads the values of the coefficients of the Pj for the normalized antisymmetric OP.
    
    INPUT:
    deg (int) - highest degree of OP required
    """
    W = np.loadtxt('pk-recursionN')
    W = W[:deg+1, :deg+1]
    return W
