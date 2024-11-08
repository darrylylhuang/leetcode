class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = []
        days = 0
        for temperature in temperatures:
            if not stack or temperature < stack[-1]:
                stack.append(temperature)
            else:
                answer.append(len(stack))
                stack.pop()
                stack.append(temperature)
