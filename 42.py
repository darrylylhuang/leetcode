class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        trapped = 0
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                trapped += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                trapped += rmax - height[r]

        return trapped
