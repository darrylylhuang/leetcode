class ListNode(object):
    def __init__(self, x):
        self.val = x
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
            return self._key_value[key]
        else:
            return -1

        # TODO: update key usage

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # no space for a new key
        if key not in self._key_value and len(self._key_value) >= self._capacity:
            # delete key-value pair
            pop_key = self._head.val
            self._key_value.pop(pop_key)

            # remove old key usage data (remove node from linked list)
            self._head = self._head.next

        # delete existing key from linked list
        if key in self._key_value:
            old_node = self._key_value[key]
            old_node.prev.next = old_node.next
            old_node.next.prev = old_node.prev

        # add new key usage data (most recently used)
        self._tail.next = ListNode(value)
        self._tail.next.prev = self._tail
        self._tail = self._tail.next

        # updates old key or adds new key-value if there is space
        self._key_value[key] = self._tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
