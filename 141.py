# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.hasCycleTwoPointer(head)

    def hasCycleSet(self, head):
        """
        Uses a set to see if a node gets repeated (will go through the whole linked list)
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
        return False

    def hasCycleTwoPointer(self, head):
        """
        Uses a slow and fast pointer; if they collide, there is a loop
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
