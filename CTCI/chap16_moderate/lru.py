from orderedmap import OrderedMap
from collections import OrderedDict
from decorator import decorator
from threading import currentThread

class LRU:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.om = OrderedMap()

    def get(self, key):
        return self.om.get(key)

    def set(self, key, value):
        if self.size >= self.max_size:
            self.om.pop_back()
        else:
            self.size += 1
        self.om.set(key, value)

    def to_list(self):
        return self.om.to_list()

class LRU2:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.od = OrderedDict()

    def get(self, key):
        self.od.move_to_end(key, last=False)
        return self.od.get(key)

    def set(self, key, value):
        if self.size >= self.max_size:
            self.od.popitem(last=True)
        else:
            self.size += 1
        self.od[key] = value
        self.od.move_to_end(key, last=False)

    def to_list(self):
        return self.od.items()


@decorator
def with_print(f, *args, **kwargs):
    retval = f(*args, **kwargs)
    print(retval)
    return retval

@with_print
def plus_2(x: int) -> int:
    return x + 2

plus_2(1)
plus_2(2)
plus_2(3)

def lru_cache(size):
    cache = LRU(size)

    @decorator
    def wrapped(f, key):
        if cache.get(key) is None:
            print(f'{key} NOT in cache')
            cache.set(key, f(key))
        else:
            print(f'{key} in cache')
        return cache.get(key)

    return wrapped

@lru_cache(3)
def add_1(x: int) -> int:
    return x + 1

if __name__ == "__main__":
    # test LRU using my orderedmap
    lru = LRU(3)
    lru.set('a', 1)
    lru.set('b', 2)
    lru.set('c', 3)
    print(lru.to_list())
    lru.set('d', 4)
    print(lru.to_list())
    lru.set('e', 5)
    print(lru.to_list())

    # test lru using python's ordereddict
    lru = LRU2(3)
    lru.set('a', 1)
    lru.set('b', 2)
    lru.set('c', 3)
    print(lru.to_list())
    lru.set('d', 4)
    print(lru.to_list())
    lru.set('e', 5)
    print(lru.to_list())

    # test lru_cache decorator
    add_1(1)
    add_1(1)
    add_1(2)
    add_1(2)
    add_1(3)
    add_1(3)
    add_1(4)
    add_1(1)
