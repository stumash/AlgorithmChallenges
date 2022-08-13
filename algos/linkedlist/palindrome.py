from typing import Generic, List, TypeVar, Optional

T = TypeVar('T')

class LLNode(Generic[T]):
    def __init__(
        self,
        value: T,
        next: Optional['LLNode[T]'] = None
    ) -> None:
        self.value = value
        self.next = next

    @staticmethod
    def from_list(ts: List[T]) -> Optional['LLNode[T]']:
        if ts == []:
            return None
        first = ts[0]
        head = LLNode(first)
        curr = head
        for t in ts[1:]:
            curr.next = LLNode(t)
            curr = curr.next
        return head

    def to_list(self) -> List[T]:
        result = []
        curr: "LLNode[T]|None" = self
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result

    def reverse(self, i: Optional[int] = None) -> 'LLNode[T]':
        """reverse the linked list, up until (not including) the node of a given index i

        Note: this function mutates the linkedlist in place

        :i: the index of the node at which to stop reversing the linkedlist. i <= 1 has no effect
        :returns: the new head of the linekdlist
        """
        head = self
        curr = head.next
        self.next = None

        while curr and (i is None or i > 1):
            next = curr.next
            curr.next = head
            head = curr
            curr = next
            if i is not None: i -= 1
        if i is not None and i in [0, 1]:
            self.next = curr

        return head

    def size(self) -> int:
        count = 0
        curr = self
        while curr:
            count += 1
            curr = curr.next
        return count

    def node_at(self, i: int) -> Optional['LLNode[T]']:
        if i < 0: return None
        curr = self
        while curr and i != 0:
            i -= 1
            curr = curr.next
        return curr if curr else None

    def check_palindrome(self) -> bool:
        """check if the linked list is a palindrome by reversing the front half of the linkedlist and then traversing
        the two halves at once to verify that all node pairs have the same value

        Note: this method completely corrupts the linkedlist by reversing half of it in place

        :returns: True if the linkedlist is palindrome, else False
        """
        size = self.size()
        half = int(size / 2)
        ll = self.reverse(half)

        half_node = ll.node_at(half)
        head_1, head_2 = ll, (half_node if size % 2 == 0 else (half_node.next if half_node else None))

        while head_1 and head_2:
            if head_1.value != head_2.value:
                return False
            head_1, head_2 = head_1.next, head_2.next
        return True


class LinkedList(Generic[T]):
    def __init__(self, head: Optional[LLNode[T]] = None):
        self.head = head

    @staticmethod
    def from_list(ts: List[T]) -> 'LinkedList[T]':
        return LinkedList(LLNode.from_list(ts))

    def size(self) -> int:
        return 0 if self.head is None else self.head.size()

    def node_at(self, i: int) -> Optional[LLNode[T]]:
        return None if (self.head is None or i < 0) else self.head.node_at(i)

    def reverse(self, i: Optional[int] = None):
        if self.head:
            self.head = self.head.reverse(i)

    def to_list(self) -> List[T]:
        return [] if self.head is None else self.head.to_list()

    def check_palindrome(self) -> bool:
        if self.head is None:
            return True

        size = self.size()
        half = int(size / 2)

        self.head = self.head.reverse(half)
        half_node = self.node_at(half)

        head_1, head_2 = self.head, (half_node if size % 2 == 0 else (half_node.next if half_node else None))

        while head_1 and head_2:
            if head_1.value != head_2.value:
                return False
            head_1, head_2 = head_1.next, head_2.next
        return True


if __name__ == "__main__":
    for test in [
        [],
        [1],
        [1,2],
        [1,1],
        [1,2,3],
        [1,2,2,1],
        [1,2,3,2,1]
    ]:
        if (ll := LLNode.from_list(test)):
            assert(ll.to_list() == test)
            assert(ll.reverse().to_list() == list(reversed(test)))
        if (ll := LLNode.from_list(test)):
            assert(ll.check_palindrome() == (list(reversed(test)) == test))

        if (ll := LinkedList.from_list(test)):
            assert(ll.to_list() == test)
            ll.reverse()
            assert(ll.to_list() == list(reversed(test)))
            ll.reverse()
            assert(ll.check_palindrome() == (list(reversed(test)) == test))
