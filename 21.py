# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            head = list2
        elif list2 is None:
            head = list1
        elif list1.val < list2.val:
            head = list1
        else:
            head = list2

        curr = head

        while curr:
            break

        return head
