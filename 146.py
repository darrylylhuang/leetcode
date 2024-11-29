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

            # add new key usage data (most recently used)
            new_node = ListNode(value)
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

            # add new key-value pair
            self._key_value[key] = new_node
        else:
            # updates old key or adds new key-value if there is space
            self._key_value[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
