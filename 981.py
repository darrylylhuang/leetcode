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

        # the timestamp for the last element in the list will be the max since timestamp is strictly increasing
        old_timestamps = self._values[key][0]
        values = self._values[key][1]

        # max old_timestamp is less than given so we return
        if old_timestamps[-1] <= timestamp:
            return values[-1]

        l, r = 0, len(old_timestamps) - 1
        # binary search for give timestamp
        while l <= r:
            mid = (l + r) // 2


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
