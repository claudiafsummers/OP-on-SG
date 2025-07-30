import numpy as np

from index import index

def SGedge23(m):
    """
    Returns the indices of the points along the edge of the Sierpinski gasket
    between v2 and v3 on the level m graph.
    """
    
    indices = np.zeros(2**(m+1), dtype=int)

    for j in range(1, 2**(m+1) + 1):
        v = []
        l = j
        for _ in range(m + 1):
            if l % 2 == 0:
                v.append(2)
            else:
                v.append(3)
            l = l // 2
        indices[j - 1] = index(v, m)

    return np.sort(indices)
