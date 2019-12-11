from typing import List

class LLNode:
    def __init__(self, datum, succ=None):
        self.datum = datum
        self.succ = succ
    def __iter__(self):
        curr = self
        while curr:
            yield curr
            curr = curr.succ

def createLL(data: List):
    """
    assume data is list of at least 1 element
    """
    head = LLNode(data[0])
    curr = head
    for datum in data[1:]:
        curr.succ = LLNode(datum)
        curr = curr.succ
    return head

def printLL(head: LLNode):
    while head:
        print(head.datum, end=' ')
        head = head.succ
    print()

def getNthLLNode(head, n):
    """
    0-indexed
    """
    for i, node in enumerate(head):
        if i == n:
            return node
    raise ValueError("n is larger than length of Linked List")

def linkedListsDoIntersect(head1, head2):
    for node1 in head1:
        for node2 in head2:
            if node1 is node2:
                return True
    return False

def test():
    l1 = createLL(list(range(10)))
    l2 = getNthLLNode(l1, 5)

    print(linkedListsDoIntersect(l1, l2))
