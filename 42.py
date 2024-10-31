class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, 0
        trapped = 0
        # non-increasing monotonic stack
        stack = []

        # find our first barrier
        while r < len(height) and height[r] == 0:
            r += 1

        # 1. height[0] == 0 : l == 0  < r
        # 2. height[0] != 0 : l == 0 == r
        l = r

        # TODO: find smaller valleys
        # TODO: outer loop to repeat "large valley" procedure

        # start looking for the right barrier of a "large" valley
        r += 1
        while r < len(height) and height[r] < height[l]:
            if len(stack) == 0 or height[r] < stack[-1][1]:
                stack.append((r, height[r]))
            if height[r] > stack[-1][1]:
                trapped += (r - stack[-1][0]) * (height[r] - stack[-1][1])
                stack.pop()
            r += 1

        # large valley found
        # stack is not relevant to large valleys
        stack = []
        left_barrier = height[l]
        l += 1
        while l < r:
            trapped += left_barrier - height[l]
            l += 1

        # we've reached the end of the list
        if l == len(height):
            return trapped
