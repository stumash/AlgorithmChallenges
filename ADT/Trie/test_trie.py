import pytest
from trie import Trie

def test_insert_and_search():
    keys = ['abc', 'abcd']
    t = make_trie_from_keys(keys)

    for key in keys:
        assert(t.search(key))

def test_remove_and_search():
    keys = ['abc', 'abcd']
    t = make_trie_from_keys(keys)

    new_keys = ['abcc', 'abcde']
    t.insert(new_keys)

    for key in new_keys:
        assert(t.search(key))

    t.remove(keys)
    for key in keys:
        assert(not t.search(key))

def make_trie_from_keys(keys):
    t = Trie()
    t.insert(keys)
    return t
