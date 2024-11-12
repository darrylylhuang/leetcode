class TimeMap(object):

    def __init__(self):
        self._store = dict()

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self._store:
            self._store[key][0].append(timestamp)
            self._store[key][1].append(value)
        else:
            self._store[key] = [[timestamp], [value]]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not key in self._store:
            return ""

        # the timestamp for the last element in the list will be the max since timestamp is strictly increasing
        old_timestamps = self._store[key][0]
        values = self._store[key][1]

        # max old_timestamp is less than given so we return
        if old_timestamps[-1] <= timestamp:
            return values[-1]

        # given timestamp is less than min, so a value is impossible
        if timestamp < old_timestamps[0]:
            return ""

        l, r = 0, len(old_timestamps) - 1
        most_recent_time_index = l
        # binary search for give timestamp
        while l <= r:
            mid = (l + r) // 2
            if old_timestamps[mid] > timestamp:
                r = mid - 1
            else:
                most_recent_time_index = mid
                l = mid + 1

        return values[most_recent_time_index]
