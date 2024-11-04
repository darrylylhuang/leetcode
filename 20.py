class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            # add open brackets to the stack
            if char in bracket_map:
                stack.append(char)
            # when seeing a close bracket, pop off the stack and ensure validity
            else:
                # unopened bracket
                if len(stack) == 0:
                    return False
                # incorrect bracket closing
                if char != bracket_map[stack.pop()]:
                    return False
        # unclosed bracket(s)
        if len(stack) != 0:
            return False
        return True
