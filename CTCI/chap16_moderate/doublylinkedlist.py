class DLLNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, node):
        if self.head is None and self.tail is None:
            self.head, self.tail = node, node
        elif self.head == self.tail:
            self.tail = node
            if self.head is not None: self.head.next = self.tail
            self.tail.prev = self.head
        else:
            old_tail = self.tail
            self.tail = node
            if old_tail is not None: old_tail.next = self.tail
            self.tail.prev = old_tail

    def push_front(self, node):
        if self.head is None and self.tail is None:
            self.head, self.tail = node, node
        elif self.head == self.tail:
            self.head = node
            node.next = self.tail
            if self.tail is not None: self.tail.prev = self.head
        else:
            old_head = self.head
            self.head = node
            if old_head is not None: old_head.prev = self.head
            self.head.next = old_head

    def remove(self, node):
        retval = node.value if node else None

        if self.head == node and self.tail == node:
            self.head, self.tail = None, None
            node.prev, node.next = None, None
        elif self.head == node:
            self.head = self.head and self.head.next
            if self.head is not None: self.head.prev = None
            node.next = None
        elif self.tail == node:
            self.tail = self.tail and self.tail.prev
            if self.tail is not None: self.tail.next = None
            node.prev = None

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        return retval

    def pop_back(self):
        return self.remove(self.tail)

    def pop_front(self):
        return self.remove(self.head)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    @staticmethod
    def from_list(xs):
        result = DoublyLinkedList()
        for x in xs:
            result.push_back(DLLNode(x))
        return result

if __name__ == "__main__":
    ns = DoublyLinkedList.from_list([1,2,3])
    assert(ns.to_list() == [1,2,3])
    ns.push_back(DLLNode(4))
    ns.push_back(DLLNode(5))
    assert(ns.to_list() == [1,2,3,4,5])
    ns.pop_back()
    ns.push_back(DLLNode(6))
    assert(ns.to_list() == [1,2,3,4,6])
    ns.pop_front()
    ns.push_front(DLLNode(0))
    assert(ns.to_list() == [0,2,3,4,6])
    ns.pop_back()
    ns.pop_back()
    ns.pop_back()
    assert(ns.to_list() == [0,2])
    ns.pop_back()
    assert(ns.to_list() == [0])
    ns.pop_back()
    assert(ns.to_list() == [])
