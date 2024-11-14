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
            # once we reach a smaller height, we should calculate all intermediate areas
            while stack and stack[-1][1] > height:
                w, h = stack.pop()
                max_area = max(
                    max_area, (i - w) * h)
                # extend the new low bar as far back as the oldest bar with height greater
                start = w
            # either adds the new high bar starting at i
            # or extends the new low bar back to just after the previous low
            stack.append((start, height))

        # calculate the rest of the pending areas
        i += 1
        while stack:
            w, h = stack.pop()
            max_area = max(
                max_area, (i - w) * h)

        return max_area
