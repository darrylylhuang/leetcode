class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # if we have a very generous h, we can eat one banana at a time
        # having a banana-eating rate higher than our largest pile is pointless
        l, r = 1, max(piles)
        # longest_time = 0
        lowest_eating_rate = r
        # O(log(n))
        while l < r:
            time_taken = 0
            mid = (l + r) // 2
            # O(n)
            for pile in piles:
                # ceiling divison
                time_taken += -(pile // -mid)

            if time_taken > h:
                l = mid + 1
            else:
                r = mid - 1
                # longest_time = time_taken
                lowest_eating_rate = mid
        return lowest_eating_rate
