class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            row = board[i]
            current_row = set()
            for j in range(len(row)):
                box = row[j]

                # empty box; move on
                if box == ".":
                    continue

                # row duplicate
                if box in current_row:
                    return False
                else:
                    current_row.add(box)
