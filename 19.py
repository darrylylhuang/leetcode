# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        return self.removeNthFromEndSlowFast(head, n)

    def removeNthFromEndSlowFast(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # input is assumed to be valid: 1 <= n <= sz
        # base case: valid list with only one element
        if not head.next:
            return None
        slow, fast = head, head.next
        # assume two nodes to start
        sz = 2
        # slow += 1; fast += 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # jump 2 nodes
            sz += 2
        # fast is pointing to None because we have odd elements
        if not fast:
            sz -= 1

        index = sz - n
        # edge case, we're removing the first element of the list
        if index == 0:
            return head.next

        # start at 1 because we want to stop right before the element
        i = 1
        curr = head
        # element is in the second half of the list
        if index > (sz - 1) // 2:
            # increment our counter to the midpoint
            i += (sz - 1) // 2
            curr = slow

        # loop until we're just before the desired element to remove
        while i < index:
            curr = curr.next
            i += 1

        # set prev.next = curr.next to "delete" curr
        curr.next = curr.next.next
        return head
