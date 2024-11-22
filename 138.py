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
            if old.next is None:
                new.next = None
            else:
                new.next = Node(old.next)

            new = new.next
            old = old.next
