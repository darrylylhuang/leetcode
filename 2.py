# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy node to keep track of head
        prehead = ListNode()
        curr = prehead
        # initialize carry at 0
        carry = 0

        # loop while either list is non-empty
        while l1 or l2:
            # initialize sum of digits
            sum = carry

            # add digit value(s) to sum and increment input(s)
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # addition carry over logic
            curr.next = ListNode(sum % 10)
            carry = sum // 10

            # increment output
            curr = curr.next

        # two equal length lists may have a final carry overflow
        if carry != 0:
            curr.next = ListNode(carry)

        return prehead.next
