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
        # if the old Node isn't in the map, we need to create a new Node and map the two
        # if the old Node is in the map, we use the new Node in the mapping
        while new:
            # handle "next" nodes
            if old.next not in old_to_new:
                if old.next:
                    old_to_new[old.next] = Node(old.next.val)
                else:
                    old_to_new[old.next] = None
            new.next = old_to_new[old.next]

            # handle "random" nodes
            if old.random not in old_to_new:
                if old.random:
                    old_to_new[old.random] = Node(old.random.val)
                else:
                    old_to_new[old.random] = None
            new.random = old_to_new[old.random]

            new = new.next
            old = old.next
