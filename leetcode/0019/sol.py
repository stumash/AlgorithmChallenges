from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

    @staticmethod
    def from_list(xs):
        if xs == []:
            return None
        head = ListNode(xs[0])
        curr = head
        for x in xs[1:]:
            curr.next = ListNode(x)
            curr = curr.next
        return head

    def to_list(self):
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # get the nth node
        prev, curr, i = None, head, 0
        while curr and i != length - n:
            prev, curr = curr, curr.next
            i += 1
        if prev and curr:
            prev.next = curr.next

        return head


if __name__ == "__main__":
    for nums, i_back, expected in [
    ]:
        pass
    result = Solution().removeNthFromEnd(ListNode.from_list([1,2,3,4,5]), 3)
    assert(result.to_list() == [1,2,4,5])
