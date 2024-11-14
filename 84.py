class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 1 <= heights.length <= 10^5
        max_area = heights[0]
        stack = [max_area]
        for height, i in enumerate(heights):
            if height < stack[-1]:
                # intermediate wide area constrained by previous stack min = i * stack[-1]
                max_area = max(max_area, i * stack[-1])
                stack.append(height)

        return max_area
