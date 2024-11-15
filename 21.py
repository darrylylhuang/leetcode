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
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        curr = head
        while curr:
            # both lists have been exhausted
            if list1 is None and list2 is None:
                # we can point to the end
                curr.next = None
            # list1 has been exhausted
            elif list1 is None:
                # append the rest of list2 and break
                curr.next = list2
                break
            # list2 has been exhausted
            elif list2 is None:
                # append the rest of list1 and break
                curr.next = list1
                break
            elif list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        return head
