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
            # TODO: FIX STACK LOGIC
            # new trough found
            if len(stack) == 0 or height[r] < stack[-1][1]:
                stack.append((r, height[r]))

            # new right barrier found
            if height[r] > stack[-1][1]:
                while len(stack) > 0:
                    (width, length) = stack.pop()
                    # stack is still not empty, so we have an intermediate left barrier
                    if len(stack) > 0:
                        left_bar = stack[-1][1]
                    # stack has been emptied
                    else:
                        left_bar = height[l]

                    if height[r] < left_bar:
                        trapped += (r - width) * (height[r] - length)
                    else:
                        trapped += (r - width) * (left_bar - length)

                # current "right barrier" could be an intermediate left barrier
                stack.append((r, height[r]))
                # if left barrier was the bottleneck on the last iteration,
                # we've added all rain possible to the left of the right pointer
                if height[l] <= height[r]:
                    l = r
            r += 1

        return trapped
