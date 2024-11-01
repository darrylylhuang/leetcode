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

        # start looking for more barriers
        r += 1
        while r < len(height):
            # new trough found
            if len(stack) == 0 or height[r] < stack[-1][1]:
                stack.append((r, height[r]))

            # new barrier found
            if height[r] > stack[-1][1]:
                (width, length) = stack.pop()
                trapped += (r - width) * (min(height[l], height[r]) - length)
                # if left barrier is the bottleneck, we've added all rain possible from that side
                if height[l] < height[r]:
                    l = r
            r += 1

        return trapped
