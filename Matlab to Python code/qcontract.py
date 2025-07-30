import numpy as np

from fi import fi

def q_contract(x, q):
    '''
    This function takes in a column of coordinate pairs and computes their image under the similarity which contracts
    distance to the point q by a factor of 1/2.

    INPUT:
    x - (3^(m+1)) by 2 matrix holding x and y coordinates
    q - point toward which to contract distance by 1/2
    n - the number of points

    OUTPT: 
    y - coordinates of the n images

    from http://www.math.cornell.edu/~mhall/SGprograms/qcontract.m
    '''
    n = max(x.shape)
    y = np.empty((0, 2)) 
    for j in range(n):
        y = np.vstack([y, fi(x[j, :], q)])
    return y
