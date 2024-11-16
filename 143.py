# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # calculate the number of nodes
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        # add the second half of list to the stack
        # n - half, n - half + 1, ..., n - 1, n
        half = n // 2
        stack = []
        curr = head
        i = 0
        while curr:
            if i > half:
                stack.append(curr)
            i += 1
            curr = curr.next

        # pop from the stack and put nodes in order
        # 0, n, 1, n-1, 2, n-2, ...
        curr = head
        while stack:
            nxt = curr.next
            curr.next = stack.pop()
            curr.next.next = nxt
            curr = nxt

        curr.next = None
