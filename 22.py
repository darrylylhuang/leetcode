class Solution(object):
    def generateParenthesis(self, n):
        return self.generateParenthesisI(n)

    def generateParenthesisI(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        # our stack will be in the form (str, open, close)
        stack = []

        # base case: all strings start with an open
        stack.append(("(", 1, 0))
        while stack:
            (old_combo, open, close) = stack.pop()
            # try close
            if close < open:
                stack.append((old_combo + ")", open, close + 1))

            # try open
            if open < n:
                stack.append((old_combo + "(", open + 1, close))

            # open and close are both invalid meaning we've found a result element
            if open == n and close == n:
                result.append(old_combo)

        return result

    def generateParenthesisR(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        # base case: all strings start with an open
        element = "("

        def backtrack(element, open, close):
            if open < n:
                backtrack(element + "(", open + 1, close)

            if close < open:
                backtrack(element + ")", open, close + 1)

            if open == n and close == n:
                result.append(element)

        backtrack(element, 1, 0)
        return result
