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

            # new right barrier found
            if height[r] > stack[-1][1]:
                (width, length) = stack.pop()
                # stack is not empty, so we have an intermediate left barrier
                if len(stack) != 0:
                    left_bar = stack[-1][1]
                else:
                    left_bar = height[l]

                # TODO: May need two cases here:
                # 1. Stack empty = left barrier
                # 2. Stack not empty = intermediate left barrier

                if height[r] < left_bar:
                    trapped += (r - width) * (height[r] - length)
                else:
                    trapped += (r - width) * (left_bar - length)
                    # if left barrier is the bottleneck, we've added all rain possible from that side
                    l = r
            r += 1

        return trapped
