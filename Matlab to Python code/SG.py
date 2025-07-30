import numpy as np
import itertools

from qcontract import q_contract

def SG(m):
    '''
    This function evaluates the coordinates of all points on the gasket up to a certain level V_m.

    INPUT:
    m - level of SG we would like to find coordinates for
    
    OUTPUT:
    y - ((3^m+3)/2)*2 matrix holding coordinate values

    from http://www.math.cornell.edu/~mhall/SGprograms/SG.m
    '''
    # Give coordinates for points in V_0
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

    return y
