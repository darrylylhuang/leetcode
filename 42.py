class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, 0
        trapped = 0
        non_increasing_stack = []

        # find our first barrier
        while r < len(height) and height[r] == 0:
            r += 1

        # 1. height[0] == 0 : l == 0  < r
        # 2. height[0] != 0 : l == 0 == r
        l = r

        # TODO: find smaller valleys

        # start looking for the right barrier
        while r < len(height) and height[r] < height[l]:
            r += 1

        while l < r:
            l += 1
            trapped += height[l]

        # we've reached the end of the list
        if l == len(height):
            return trapped
