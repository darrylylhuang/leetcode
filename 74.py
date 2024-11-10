class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            if matrix[i][j] > target:
                r = mid - 1
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                return True
        return False
