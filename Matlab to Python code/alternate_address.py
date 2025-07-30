import numpy as np

def alternate_address(v,m):
    '''
    This function finds the alternative address for a given point in an SG ordering. 
    If the point is on the boundary of SG, (and hence has only one such address) the same address vector is returned.

    INPUT: 
    v - address of the point (vector with length = m+1)
    m - level of SG (meaning we have 3^(m+1) points)

    OUTPUT: 
    w - alternate address vector for the same point (vector with length = m+1)

    e.g. 
    v = [1, 2, 3] m = 2 returns [1 3 2]
    v = [2, 1, 1] m = 2 returns [1 2 2]
    '''
    w = np.array(v).copy()

    if m == 0: 
        # if at level zero, nothing to be done
        return w 
    else:
        i = w[m] 
        j = w[m-1]
        k = m 
        # find the last entry of w which is not equal to w's final entry
        while j == i and k > 1:
            k -= 1 
            j = w[k-1] 

        # if there is such an entry, interchange its value with that of all subsequent entries
        if j != 0:  
            w[k-1] = i
            w[k : m + 1] = j
    
        return w 
