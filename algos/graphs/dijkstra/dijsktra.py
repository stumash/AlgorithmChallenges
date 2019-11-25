from typing import List
import heapq

heapq.heappush

G, visited

def dijkstra(graph, node1, node2):
    pass

class Queue1():
    """
    Use a binary heap

    Big O: heap of n elements
    -------------------------
    pop_min:      O( log(n) )
    decrease_key: O( log(n) )
    insert:       O( log(n) )
    """
    def __init__(self):
        self.q = []
    def pop_min(self):
        return heapq.heappop(self.q)
    def decrease_key(self, item, new_key):

class Queue2():
    """
    Use a fibonacci heap
    """ # TODO
    pass

class Queue3():
    """
    Use a binomial heap
    """ # TODO
    pass
