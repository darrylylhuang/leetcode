class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []

        while True:
            current_combo = ""
            # try open
            if n > 0:
                stack.append("(")
                n -= 1

            # try close
            if "(" in stack:
                stack.append(")")

            if n == 0:
                break

        return result
