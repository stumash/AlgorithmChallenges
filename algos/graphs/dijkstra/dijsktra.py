from typing import List, Tuple
from random import sample, randint, choices

def main():
    test_priority_queue()
    graph = init_random_connected_weighted_graph(n=20, deg=3, cost_min=1, cost_max=3)
    print_graph(graph)
    start_node, end_node = choices(list(range(len(graph))), k=2)
    path, cost = dijkstra(graph, start_node, end_node)

    print(f"cost from {start_node} to {end_node}: {cost}")
    print(f"path:\n{path}")

def dijkstra(graph, start_node, end_node):
    """
    Dijkstra's Algorithm

    graph: adjacency list representation. list of edge lists, one per node. each edge list
    is a list of (destination_node_idx, edge_cost) pairs.

    Big O
    -------------------------
    time:
    O(# edges * log(# edges))
    note that this can be "reduced" to O(# edges * log(# nodes)) because
    # edge <= (# nodes)^2, and O(log ((# nodes)^2)) is equivalent to O(log (# nodes))
    why:
    For every edge in the graph, we do an insert and pop_min into the queue. The queue's
    size is therefore O(# edges), so inserts and pop_mins take O(log(# edges)).
    -------------------------
    space:
    O(# edges)
    why: dist[] and prev[] are fixed at size <# nodes>. but the priority queue can have a
    number of elements proportional to the number of edges.
    """
    visited = set()
    queue = PriorityQueue(seed=[(start_node, 0)], key=lambda tup: tup[1])
    dist = [Inf() if i!=start_node else 0 for i in range(len(graph))]
    prev = [None                          for _ in range(len(graph))]

    # all min-cost paths from start_node
    while queue:
        curr_node, curr_dist =  queue.pop_min()
        if curr_node in visited: continue
        visited.add(curr_node)
        for neighbor, edge_cost in graph[curr_node]:
            if neighbor in visited: continue
            alt_dist = curr_dist + edge_cost
            if alt_dist < dist[neighbor]:
                dist[neighbor] = alt_dist
                prev[neighbor] = curr_node
                queue.insert((neighbor, alt_dist))

    # build path (in reverse)
    curr_node, path = end_node, []
    while curr_node is not None:
        path.append(curr_node)
        curr_node = prev[curr_node]

    return list(reversed(path)), dist[end_node]

def init_random_connected_weighted_graph(n, deg, cost_min, cost_max) -> List[List[Tuple[int,int]]]:
    if n < 1 or deg < 1 or deg >= n-1:
        raise ValueError("n={n} and deg={deg} but must have n>=1 and deg>=1 and deg<n-1")
    if cost_min < 1 or cost_min > cost_max:
        raise ValueError("cost_min={cost_min} and cost_max={cost_max} but need cost_min>=1 and cost_max>=cost_min")

    node_idxs = list(range(n))
    graph = [[] for _ in node_idxs]

    # first, random hamiltonian path to guarantee connectedness
    hamiltonian_path = sample(node_idxs, len(node_idxs))
    for node1, node2 in zip(hamiltonian_path, hamiltonian_path[1:]):
        graph[node1] += [(node2, randint(cost_min, cost_max))]

    # fill in remaining edges
    for node in node_idxs:
        ns = sample([_n for _n in range(n) if _n!=node], deg-len(graph[node]))
        cs = [randint(cost_min, cost_max) for _ in range(deg-len(graph[node]))]
        graph[node] += list(zip(ns, cs))
    return graph

def print_graph(graph):
    nodes = graph
    for i, outgoing_edges in enumerate(nodes):
        print(f"{i}: "+", ".join(f"(idx:{node_idx} cost:{cost})" for node_idx, cost in outgoing_edges))

def test_priority_queue():
    N = 100

    pq = PriorityQueue()
    elems = sample(list(range(N)), N)
    for n in elems:
        pq.insert(n)
    assert(list(range(N)) == [pq.pop_min() for _ in range(N)])

    pq = PriorityQueue(key=lambda l: l[0])
    elems = sample([[n] for n in range(N)], N)
    for n in elems:
        pq.insert(n)
    assert([[n] for n in range(N)] == [pq.pop_min() for _ in range(N)])

class PriorityQueue():
    """
    Binary Heap - Min Heap

    Underlying data structure is a list. A node at index i in the array has two
    children, at (i*2) and (i*2)+1. A node at index i has a parent at i//2. 0th
    element is always None.

    Big O: heap of n elements
    -------------------------
    pop_min:      O( log(n) )
    insert:       O( log(n) )
    """
    def __init__(self, seed=None, key=lambda x: x):
        self.q = [None]
        self.key = key
        if seed:
            for s in seed:
                self.insert(s)
    def pop_min(self):
        if len(self.q) == 1:
            raise IndexError("pop from empty queue")
        min_item = self.q[1]
        self._swap(1, -1)
        self.q.pop()
        self._bubble_down(1)
        return min_item
    def insert(self, item):
        self.q.append(item)
        self._bubble_up(len(self.q)-1)

    def _bubble_up(self, i):
        if i == 1:
            return # already at root
        parent_i = self._get_parent_index(i)
        if self.key( self.q[i] ) < self.key( self.q[parent_i] ):
            self._swap(i, parent_i)
            self._bubble_up(parent_i)
    def _bubble_down(self, i):
        children_indices = self._get_children_indices(i)
        if not children_indices:
            return # already at end
        min_child_i = min(children_indices, key=lambda c_i: self.key(self.q[c_i]))
        if self.key( self.q[i] ) > self.key( self.q[min_child_i] ):
            self._swap(i, min_child_i)
            self._bubble_down(min_child_i)
    def _get_parent_index(self, i):
        return i//2
    def _get_children_indices(self, i):
        maybes = [(i*2), (i*2)+1]
        return [m for m in maybes if m < len(self.q)]
    def _swap(self, i, j):
        self.q[i], self.q[j] = self.q[j], self.q[i]

    def __bool__(self):
        return len(self.q) > 1

class Inf:
    def __lt__(self, other):
        return False
    def __gt__(self, other):
        return True

if __name__ == "__main__":
    main()
