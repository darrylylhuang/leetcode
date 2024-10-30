class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            # length * width where the shorter height determines how much water can be held
            max_area = max(max_area, min(height[i], height[j]) * (j - i))

            # "eliminate" the shorter of the heights as it is the bottleneck
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
