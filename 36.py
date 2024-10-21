class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            current_row = set()
            for box in row:
                if box != "." and box in current_row:
                    return False
                else:
                    current_row.add(box)
