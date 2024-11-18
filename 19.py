# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # input is assumed to be valid: 1 <= n <= sz
        slow, fast = head, head.next
        # slow += 1; fast += 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

