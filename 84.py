class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 1 <= heights.length <= 10^5
        max_area = heights[0]
