class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == "+":
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)
            elif token == "-":
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif token == "*":
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            elif token == "/":
                right, left = stack.pop(), stack.pop()
                # truncate towards 0
                # case 2: quotient negative non-whole number
                if (left > 0 and right < 0) or (left < 0 and right > 0):
                    # ceiling divison
                    new_token = -(left // -right)
                # case 1: quotient positive
                else:
                    new_token = left // right
                stack.append(new_token)
            # number
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == "__main__":
    solution = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]

    print(solution.evalRPN(tokens))
    # tokens = ["4", "-2", "/", "2", "-3", "-", "-"]
    # print(solution.evalRPN(tokens))
