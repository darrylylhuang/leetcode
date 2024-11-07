class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        stack = []

        current_combo = "("
        stack.append(current_combo)
        n -= 1
        while True:
            # try open
            if n > 0:
                current_combo += "("
                stack.append("(")
                n -= 1

            # try close
            if stack:
                stack.pop()
                current_combo += ")"

            if n == 0:
                break

        return result
