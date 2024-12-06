class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        sum = 0
        ints = 0
        banned_set = {x for x in banned if x <= n}
        for i in range(1, n + 1):
            if i in banned_set:
                continue

            sum += i
            if sum > maxSum:
                return ints

            ints += 1
        return ints
