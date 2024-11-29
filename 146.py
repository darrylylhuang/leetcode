class ListNode(object):
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._key_value = dict()
        # dummy head and tail to prevent head/tail deletion
        self._head, self._tail = ListNode(0, 0), ListNode(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head

    def remove(self, node):
        """
        :type node: ListNode
        """
        # sever node's ties to delete it from the middle of the list
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        """
        :type node: ListNode
        """
        # insert node at the "tail" of the list
        node.prev = self._tail.prev
        node.next = self._tail
        # detach old pointers and attach to node
        self._tail.prev.next = node
        self._tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._key_value:
            # upate usage
            node = self._key_value[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # no space for a new key
        if key not in self._key_value and len(self._key_value) >= self._capacity:
            # delete key-value pair
            pop_key = self._head.key
            self._key_value.pop(pop_key)

            # remove old key usage data (remove node from linked list)
            self._head = self._head.next

        # delete existing key from linked list
        if key in self._key_value:
            node = self._key_value[key]
            # increment head pointer if we delete head
            if node is self._head:
                self._head = self._head.next
            # decerement tail pointer if we delete tail
            elif node is self._tail:
                self._tail = self._tail.prev

            # sever any links
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        # empty list
        if not self._head:
            self._head = ListNode(key, value)
            self._tail = self._head
        else:
            # add new key usage data (most recently used)
            self._tail.next = ListNode(key, value)
            self._tail.next.prev = self._tail
            self._tail = self._tail.next

        # updates old key or adds new key-value if there is space
        self._key_value[key] = self._tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
