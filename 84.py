class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                w, h = stack.pop()
                max_area = max(
                    max_area, (i - w) * h)
                start = w
            stack.append((start, height))

        i += 1
        while stack:
            dimensions = stack.pop()
            max_area = max(
                max_area, (i - dimensions[0]) * dimensions[1])

        return max_area
