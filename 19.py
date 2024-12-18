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
        return self.removeNthFromEndOffset(head, n)

    def removeNthFromEndOffset(self, head, n):
        """
        Uses an offset between a left and right pointer to find "n from the end".
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # dummy node removes edge cases where we remove head
        # including a list size of 1
        dummy = ListNode(0, head)
        l, r = dummy, head
        # we want the offset between the two pointers to be 1 larger than n
        # so we can stay at "prev" and delete "curr"
        i = 0
        while i < n:
            r = r.next
            i += 1

        # increment both pointers until r reaches the end of the list
        while r:
            l = l.next
            r = r.next

        # l is at the node before our desired "delete" node
        l.next = l.next.next
        # return head
        return dummy.next

    def removeNthFromEndSlowFast(self, head, n):
        """
        Uses fast and slow pointers to calculate the size of the list
        and determine the index of the node to delete. This algorithm
        should run twice as fast as using 2 loops since it runs two
        "half" loops instead of 2 full ones.
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
