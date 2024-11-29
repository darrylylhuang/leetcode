class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._key_value = dict()
        self._head = None
        self._tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self._key_value:
            # upate usage
            node = self._key_value[key]
            # node is already MRU so we don't need to change anything
            if node is self._tail:
                return node.val
            # node being the head of the list requires additional logic
            elif node is self._head:
                # at this point, we know there is a tail node that is not head (at least 2 nodes)
                # so we can move the head pointer to the next node in the list
                self._head = self._head.next
                # head has no prev
                node.next.prev = node.prev
            else:
                # delete node from middle of the list
                node.prev.next = node.next
                node.next.prev = node.prev

            # move node to the end of the list
            node.next = None
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
            # return value from key-value pair
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
            old_node = self._key_value[key]
            if old_node.prev:
                old_node.prev.next = old_node.next
            if old_node.next:
                old_node.next.prev = old_node.prev

        if not self._tail:
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
