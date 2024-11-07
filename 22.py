class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []

        # base case: all strings start with an open
        stack.append("(")
        n -= 1
        while stack:
            old_combo = stack.pop()

            # try close
            stack.append(old_combo + ")")

            # try open
            if n > 0:
                stack.append(old_combo + "(")
                n -= 1

            result.append(stack.pop())

        return result
