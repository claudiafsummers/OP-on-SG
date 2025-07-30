import numpy as np
import matplotlib.pyplot as plt

from qcontract import q_contract
from zeroflag import zeroflag

def SGcontour(u,m):
    '''
    plots a countour plot of the function u
    from http://www.math.cornell.edu/~mhall/SGprograms/SG.m
    '''

    q0 = np.array([np.cos(5*np.pi/12), np.sin(5*np.pi/12)])
    q1 = np.array([0, 0])
    q2 = np.array([np.cos(np.pi/12), np.sin(np.pi/12)])
    y = np.vstack([q0, q1, q2])
    
    for _ in range(m):
        y = np.vstack([
            q_contract(y, q0),
            q_contract(y, q1),
            q_contract(y, q2)
            ])

    # Plotting
    plt.figure()
    for j in range(3**(m + 1)):
        color = 'black'
        if u[j] > 0:
            color = 'blue'
        elif u[j] < 0:
            color = 'cyan'

        if u[j] == 0 or zeroflag(u, j, m) == 1:
            color = 'black'

        plt.plot(y[j, 0], y[j, 1], '.', color=color)

    plt.axis('equal')
    plt.show()

    return 
