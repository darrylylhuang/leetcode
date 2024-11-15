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
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            head = list1
            curr1 = head.next
            curr2 = list2
        else:
            head = list2
            curr1 = list1
            curr2 = head.next

        curr = head
        while curr:
            # both lists have been exhausted
            if curr1 is None and curr2 is None:
                # we can point to the end
                curr.next = None
            # list1 has been exhausted
            elif curr1 is None:
                # append the rest of list2 and break
                curr.next = curr2
                break
            # list2 has been exhausted
            elif curr2 is None:
                # append the rest of list1 and break
                curr.next = curr1
                break
            elif curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next

        return head
