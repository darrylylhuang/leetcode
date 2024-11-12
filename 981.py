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
        if key in self._values:
            self._values[key][0].append(timestamp)
            self._values[key][1].append(value)
        else:
            self._values[key] = [[timestamp], [value]]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self._values:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
