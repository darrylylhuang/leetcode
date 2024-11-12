class TimeMap(object):

    def __init__(self):
        self._values = dict()

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if self._values[key]:
            self._values[key].append((timestamp, value))
        else:
            self._values[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
