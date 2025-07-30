import numpy as np 

def get_omegas5(deg):
    '''
    Reads the coefficients of the normalized symmetric OP.

    INPUT:
    deg (int) - highest degree of OP required
    '''
    W = np.loadtxt('sk-recursionN')
    W = W[:deg+1, :deg+1]
    return W
