import numpy as np
import matplotlib.pyplot as plt

from SGorthoPolyspk import SGorthoPolyspk

def get_iteration(T, index, degree):
    '''
    This function generates the iteration map for a particular index of SG 

    INPUT:
    T is a large matrix with the values of the polynomials up to level m=7
    index - index of point on SG using TLR indexing (must be in range of 6562 (3**(8) + 1))
    degree (int) - highest degree polynomial to generate 
    '''
    q = np.zeros(degree+1)

    for i in range(degree + 1):
        vals = SGorthoPolyspk(T, i)
        q[i] = vals[index]

    plt.figure()
    plt.scatter(q[0:-1], q[1:])
    plt.title(f"Iteration Map for point {index}")
    plt.show()

    return
