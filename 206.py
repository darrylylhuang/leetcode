# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.reverseListI(head)

    def reverseListI(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # end of the list
        prev = None
        # first node
        curr = head
        # we travel forwards while shifting pointers backwards
        while curr is not None:
            # save next node so we can set it to something else
            next = curr.next
            # shift pointer backwards
            curr.next = prev
            # save current value to point backwards
            prev = curr
            # move to the next node
            curr = next
        # will return None if the loop never executed
        # will return the new head otherwise
        return prev
    
    def reverseListR(self, head):
        return