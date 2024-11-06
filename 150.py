class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token.isnumeric():
                print("putting" + token + "in the stack")
                stack.append(int(token))
            # operator
            else:
                # case 1: negative number
                if token.strip("-").isnumeric():
                    stack.append(-1 * int(token))
                    continue
                # case 2: operator
                # second token is at the top of the stack
                right = stack.pop()
                left = stack.pop()
                print("doing" + token + "on" + str(left) + "and" + str(right))
                if token == "+":
                    stack.append(left + right)
                if token == "-":
                    stack.append(left - right)
                if token == "*":
                    stack.append(left * right)
                if token == "/":
                    stack.append(left // right)

        return stack.pop()


if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    print(solution.evalRPN(tokens))
