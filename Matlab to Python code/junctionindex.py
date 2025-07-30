from index import index

def junctionindex(add0, m):
    '''
    Given an address (add0) in V_n, junctionindex outputs the index of add0 in V_m where m>=n
    
    INPUT:
    add0 - address of the point of the form [1, 2] (vector with length = n+1)
    m - level of SG (m>=n)
    
    OUTPUT: index of the point indicated by add0, but in V_m
    
    e.g.
    junctionindex([1, 2], 3) = 14
    junctionindex([1, 2], 2) = 5
    '''
    n = len(add0) - 1

    if m >= n:
        k = m - n
        add1 = add0.copy()
        q = add1[n]
        for _ in range(k):
            add1.append(q)
    else:
        m = n
        add1 = add0

    v = index(add1, m)
    return v
