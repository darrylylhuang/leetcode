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
        if key not in self._key_value and len(self._key_value) >= self._capacity:
            # TODO: Evict LRU key
            return
        else:
            # updates old key or adds new key-value if there is space
            self._key_value[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
