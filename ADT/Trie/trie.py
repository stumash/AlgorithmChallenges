class TrieNode:
    def __init__(self, children=None, is_eow=None):
        self.children = children if children is not None else {}
        self.is_eow = is_eow if is_eow is True else False # eow = end of word

    def __contains__(self, c):
        return c in self.children

    def __setitem__(self, k, v):
        self.children[k] = v

    def __getitem__(self, k):
        return self.children[k]

    def __repr__(self):
        s = "TrieNode(children={}, is_eow={})"
        return s.format(self.children, self.is_eow)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        if type(key) == str:
            self._insert_one(key)
        elif type(key) == list:
            keys = key
            for key in keys:

                self._insert_one(key)
        else:
            s = 'Error: exptected str or List[str]'
            raise TypeError(s)

    def _insert_one(self, key):
        curr = self.root
        for c in key:
            if c not in curr:
                curr[c] = TrieNode()
            curr = curr[c]
        curr.is_eow = True

    def search(self, key):
        curr = self.root
        for c in key:
            if not c in curr:
                return False
            curr = curr[c]
        return curr.is_eow

    def remove(self, key):
        if type(key) == str:
            self._remove_one(key)
        elif type(key) == list:
            keys = key
            for key in keys:
                self._remove_one(key)
        else:
            s = 'Error: expected str or List[str]'
            raise TypeError(s)

    def _remove_one(self, key):
        curr = self.root
        for c in key:
            if c not in curr:
                return
            curr = curr[c]
        curr.is_eow = False

    def __str__(self):
        return str(self.root)
