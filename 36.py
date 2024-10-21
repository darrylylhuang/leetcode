class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = {x: set() for x in range(9)}

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

                # column duplicate
                if box in columns[j]:
                    return False
                else:
                    columns[j].add(box)

        # default case
        return True
