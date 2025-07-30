import numpy as np

from SGedge13 import SGedge13
from SGorthoPolyspk import SGorthoPolyspk
from SGorthoPolyssk import SGorthoPolyssk

def SGorthoPolyEdge13phik(T,deg):
    '''
    Evaluates the orthonormal polynomial phi_deg_base along the edge between v1 and v3 (side edge)

    INPUT:
    T is a large matrix with the values of the polynomials up to level m=7
    deg (int) - highest degree of OP required
    '''
    m=7
    indices = SGedge13(m)
    Q = SGorthoPolyspk(T,deg)
    S = SGorthoPolyssk(T,deg)
    phi = np.sqrt(2/3) * Q + np.sqrt(1/3) * S

    edge = []
    idx = 0
    for j in range(1, 3**(m+1) + 1):
        if idx < len(indices) and j == indices[idx]:
            edge.append(phi[j - 1])
            idx += 1
    return edge
