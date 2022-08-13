class LLNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class OD:
    def __init__(self, order):
        self.order = order
        self.d = {}
        self.head = None
        self.tail = None
    def get(self, key):
        if key in self.d:
            node = self.d[key]
            if self.order == 'get' or self.order == 'both':
                prev, next = node.prev, node.next
                if prev:
                    prev.next = next
                node.next = self.head
                self.head = node
            return node.value
        return None
    def set(self, key, value):
        if key not in self.d:
            self.d[key] = LLNode(value)
        node = self.d[key]
        prev, next = node.prev, node.next

