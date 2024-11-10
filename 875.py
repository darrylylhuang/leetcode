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
        mid = (l + r) // 2
