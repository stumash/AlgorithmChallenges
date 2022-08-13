from doublylinkedlist import DoublyLinkedList, DLLNode
from typing import Literal, Union

Ordering = Union[
    Literal['get'],
    Literal['set'],
    Literal['both']
]

class OrderedMap:
    def __init__(self, order: Ordering = 'both'):
        self.order = order
        self.d = {}
        self.ll = DoublyLinkedList()

    def get(self, key):
        if key in self.d:
            if self.order in ['get', 'both']:
                k,v = self.ll.remove(self.d[key])
                node = DLLNode((k,v))
                self.ll.push_front(node)
                self.d[key] = node
            return self.d[key].value[1]
        return None

    def set(self, key, value):
        if key in self.d:
            self.d[key].value = (key, value)
        else:
            self.d[key] = DLLNode((key, value))

        node = self.d[key]
        if self.order in ['set', 'both']:
            self.ll.push_front(node)
        else:
            self.ll.push_back(node)

    def remove(self, key):
        if key not in self.d: return
        node = self.d[key]
        self.ll.remove(node)
        self.d.pop(key)

    def pop_back(self):
        k,v = self.ll.pop_back()
        self.d.pop(k)
        return k,v

    def pop_front(self):
        k,v = self.ll.pop_front()
        self.d.pop(k)
        return k,v

    def to_list(self):
        return self.ll.to_list()

if __name__ == "__main__":
    om = OrderedMap()
    om.set('a', 1)
    om.set('b', 2)
    om.set('c', 3)
    print(om.to_list())
    print(om.get('a'))
    print(om.get('b'))
    print(om.get('c'))
    print(om.to_list())
    print(om.pop_back())
    print(om.to_list())
