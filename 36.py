class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = {x: set() for x in range(9)}
        mini_squares = {x: set() for x in range(9)}

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

                # map indices to the range of [0, 2]
                # basically, we simulate a 3x3 as if it were represented by a single list
                k = (i // 3) * 3 + (j // 3)
                # mini-squares duplicate
                if box in mini_squares[k]:
                    return False
                else:
                    mini_squares[k].add(box)

        # default case
        return True
