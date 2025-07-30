def index(v,m):
    '''
    This function finds the index in TLR ordering corresponding to a given address
    
    INPUT: 
    v - address of the point (vector with length = m+1)
    m - level of SG (meaning we have 3^(m+1) indices) 

    OUTPUT: index corresponding to the given address
    '''
   
    if len(v) == 1:
        # case m = 0
        return v[0]
    else:
        # general recursive formula
        return 3**m * (v[0] - 1) + index(v[1:], m - 1)
