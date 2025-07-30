import numpy as np

from log3 import log3

def SG_rotate_1(graph):
    """
    Rotates the level-m SG graph so that q1 is at the top.

    INPUT:
    graph (np.ndarray or list) - function values of length 3^(m+1)

    OUTPUT: rotated version of graph
    """
    graph = np.array(graph)
    N = len(graph)
    m = int(round(log3(N))) - 1

    if m > 0:
        third = N // 3
        graph1 = graph[:third]
        graph2 = graph[third:2*third]
        graph3 = graph[2*third:]
        rot = np.concatenate([
            SG_rotate_1(graph2),
            SG_rotate_1(graph3),
            SG_rotate_1(graph1)
        ])
    else:
        # m=0: rotate q1 to the top
        rot = np.array([graph[1], graph[2], graph[0]])

    return rot
