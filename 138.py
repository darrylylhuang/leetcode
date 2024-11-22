"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        new_head = Node(head.val)
        new, old = new_head, head
        # map old nodes to new nodes
        old_to_new = dict()
        old_to_new[old] = new
        while new:
            # there is a chance that the next Node already exists because of random
            if old.next in old_to_new:
                new.next = old_to_new[old.next]
            # if the next Node doesn't exist, create and map it even if it is None
            else:
                if old.next is None:
                    new.next = None
                else:
                    new.next = Node(old.next.val)
                old_to_new[old.next] = new.next

            new = new.next
            old = old.next
