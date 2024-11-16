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
        self.reorderList2Pointers(head)

    def reorderList2Pointers(self, head):
        """
        Uses two pointers
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        # slow += 1; fast += 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the links for the second half of the list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # use two pointers to rearrange the list in order
        # 0, n, 1, n-1, 2, n-2, ...
        l, r = head, prev
        while l:
            # save our increments
            nextL, nextR = l.next, r.next
            # first half points to second half
            l.next = r
            # second half points back to first half incremented
            r.next = nextL
            l, r = nextL, nextR

    def reorderListArray(self, head):
        """
        Utilizes array functionality instead of strictly stack
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

        # calculate the number of nodes
        n = len(stack)

        # add the second half of list to the stack
        # n - half, n - half + 1, ..., n - 1, n
        half = (n - 1) // 2
        stack = stack[(half + 1):]

        # pop from the stack and put nodes in order
        # 0, n, 1, n-1, 2, n-2, ...
        curr = head
        while stack:
            nxt = curr.next
            curr.next = stack.pop()
            curr.next.next = nxt
            curr = nxt

        curr.next = None

    def reorderListStack(self, head):
        """
        Uses the strict definition of a stack
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
        half = (n - 1) // 2
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
