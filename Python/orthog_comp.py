import numpy as np
from scipy.linalg import null_space

from innerprods import inner0_j1k2, inner0_j2k2

def matrix_G(j):
    ''' 
    This function constructs the orthogonal compliment matrix of dimensions j+1 by 2j+2
    INPUT: j which is maximum degree polynomial
    OUTPUT: matrix of dimensions j+1 by 2j+2
    '''

    rows, cols = j+1, (2*j)+2
    G = np.zeros((rows, cols))

    cols = {}

    for m in range (j+1):
        cols[(2*m)+1] = []
        for i in range(j+1):
            cols[(2*m)+1].append(inner0_j1k2(m, i))

        cols[(2*m)+2] = []
        for i in range(j+1):
            cols[(2*m)+2].append(inner0_j2k2(m, i))

    G = np.column_stack([cols[k] for k in range(1, 2 * (j + 1)+1)])
    return G

def null_G(j):
    ''' 
    This function computes the null space of the orthogonal compliment matrix
    INPUT: j
    OUTPUT: 2D array whose columns form an orthonormal basis for the null space.
    '''
    G = matrix_G(j)
    G = np.array(G)
    float_G = [[float(x) for x in row] for row in G]
    N = null_space(float_G)

    return np.array(N)
