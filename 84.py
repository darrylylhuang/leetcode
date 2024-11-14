class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        for height, i in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))

        return max_area
