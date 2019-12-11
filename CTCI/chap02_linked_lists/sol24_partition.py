from random import sample

class LLNode:
    def __init__(self, datum, succ=None):
        self.datum = datum
        self.succ = succ

def createLinkedList(data):
    if len(data) < 1:
        raise ValueError("Cannot create linked list using no data")
    head = LLNode(data[0])
    curr = head
    for datum in data[1:]:
        curr.succ = LLNode(datum)
        curr = curr.succ
    return head

def printLinkedList(head: LLNode):
    curr = head
    while curr:
        print(curr.datum, end=' ')
        curr = curr.succ
    print()

def partitionLinkedList(head: LLNode, pivot):
    """
    moves all elements in the LL that are less than the pivot to the front
    """
    curr = head
    while curr.succ:
        if curr.succ.datum < pivot:
            new_head = curr.succ
            curr.succ = curr.succ.succ
            new_head.succ = head
            head = new_head
        else:
            curr = curr.succ
    return head

def test():
    n = 10
    head = createLinkedList(sample(list(range(n)), n))
    printLinkedList(head)
    print('-'*10)
    head = partitionLinkedList(head, 5)
    printLinkedList(head)
