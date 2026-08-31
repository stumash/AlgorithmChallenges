class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self) -> list[int]:
        retval = []
        curr = self
        while curr:
            retval.append(curr.val)
            curr = curr.next
        return retval

    @classmethod
    def fromList(cls, l: list[int]) -> ListNode | None:
        if len(l) < 1:
            return None
        retval = ListNode(l[0])
        curr = retval
        i = 1
        while i < len(l):
            curr.next = ListNode(l[i])
            i += 1
            curr = curr.next
        return retval


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            retval = ListNode(list1.val)
            list1 = list1.next
        else:
            retval = ListNode(list2.val)
            list2 = list2.next

        curr: ListNode = retval
        while list1 or list2:
            if (list1 and not list2) or (list1 and list2 and list1.val <= list2.val):
                curr.next = ListNode(list1.val)
                list1 = list1.next
            elif (list2 and not list1) or (list1 and list2 and list2.val < list1.val):
                curr.next = ListNode(list2.val)
                list2 = list2.next
            else:
                raise ValueError("unreachable")
            curr = curr.next

        return retval


examples = [
    (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    ),
    (
        [],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ),
    (
        [],
        [],
        [],
    ),
    (
        [1, 3, 5],
        [2, 4, 6],
        [1, 2, 3, 4, 5, 6],
    )
]

for l1, l2, result in examples:
    sol = Solution().mergeTwoLists(ListNode.fromList(l1), ListNode.fromList(l2))
    if sol:
        assert sol.toList() == result, f"{l1=}, {l2=}, {result}"
    print(l1, l2, result)
