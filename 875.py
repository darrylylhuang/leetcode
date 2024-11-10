class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # if we have a very generous h, we can eat one banana at a time
        # having a banana-eating rate higher than our largest pile is pointless
        # O(n)
        l, r = 1, max(piles)
        lowest_eating_rate = r
        # O(log(r))
        while l <= r:
            time_taken = 0
            mid = (l + r) // 2
            # O(n)
            for pile in piles:
                # use ceiling division because we can't take fractional hours to eat
                time_taken += -(pile // -mid)

            # increase eating rate because we took too long
            if time_taken > h:

                l = mid + 1
            # within time limit h, this is the lowest eating rate seen
            else:
                lowest_eating_rate = mid
                # see if we can go lower
                r = mid - 1

        return lowest_eating_rate
