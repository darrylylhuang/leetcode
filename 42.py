class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, 0
        trapped = 0
        # find our first left barrier
        while l < len(height) and height[l] == 0:
            l += 1

        # catch right pointer up to left pointer
        r = l

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
