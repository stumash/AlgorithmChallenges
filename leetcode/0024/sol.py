from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> List[int]:
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    @staticmethod
    def from_list(nums: List[int]) -> 'ListNode':
        if len(nums) == 0: raise Exception('cannot make linked list from empty list')
        head = ListNode(nums[0])
        curr = head
        for i,n in enumerate(nums):
            if i == 0: continue
            curr.next = ListNode(n)
            curr = curr.next
        return head

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        new_head = curr and curr.next

        while curr and curr.next:
            next = curr.next
            next_next = next.next

            if prev: prev.next = next
            next.next = curr
            curr.next = next_next

            prev = curr
            curr = next_next
        if new_head: return new_head
        return head

tests = [
    ([1,2,3,4], [2,1,4,3]),
    ([1], [1])
]

for inp, expected in tests:
    actual_ll = Solution().swapPairs(ListNode.from_list(inp))
    actual = actual_ll and actual_ll.to_list()
    if actual != expected:
        print(f'expected {expected} but got {actual} for swapPairs({inp})')
