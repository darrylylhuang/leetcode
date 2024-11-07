class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []

        # base case: all strings start with an open
        stack.append(("(", n - 1))
        while stack:
            old_combo = stack.pop()

            # try close
            stack.append((old_combo[0] + ")", old_combo[1]))

            # try open
            if old_combo[1] > 0:
                stack.append((old_combo[0] + "(", old_combo[1] - 1))
            # if no more brackets can be opened, our last element used it's last close since we try close first
            else:
                result.append(stack.pop()[0])

        return result
