import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyspk import SGorthoPolyspk

def attractorplot(T, index, degree):
    '''
    This function generates an attractor plot for a particular index of SG 

    INPUT:
    T is a large matrix with the values of the polynomials up to level m=7
    index - index of point on SG using TLR indexing (must be in range of 6562 (3**(8) + 1))
    degree (int) - max. degree polynomial to generate for kdegree
    '''

    for k in range(degree + 1):
        kdegree = SGorthoPolyspk(T, k)
        x = kdegree[index]

        kplusonedegree = SGorthoPolyspk(T, k + 1)
        y = kplusonedegree[index]

        kplustwodegree = SGorthoPolyspk(T, k + 2)
        z = kplustwodegree[index]

        plt.plot(np.log(y**2), np.log(x * z), 'bo-')

    plt.show()
