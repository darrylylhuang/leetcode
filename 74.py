class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        mid = m * n // 2
        offset = 0
        while mid > 0:
            i = mid + offset // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                mid = mid // 2
            else:
                mid = mid // 2
                offset += mid
        
        i = offset // n
        j = offset % n
        # final element
        return matrix[i][j] == target