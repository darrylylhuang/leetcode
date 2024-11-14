class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))
            else:
                while stack and stack[-1][1] > height:
                    dimensions = stack.pop()
                    max_area = max(
                        max_area, (i - dimensions[0]) * dimensions[1])
                stack.append((dimensions[0], height))

        i += 1
        while stack:
            dimensions = stack.pop()
            max_area = max(
                max_area, (i - dimensions[0]) * dimensions[1])

        return max_area
