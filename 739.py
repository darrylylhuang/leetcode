class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack or temperatures[i] <= stack[-1][1]:
                stack.append((i, temperatures[i]))
            else:
                while stack and temperatures[i] > stack[-1][1]:
                    (j, temp) = stack.pop()
                    answer[j] = i - j
                stack.append((i, temperatures[i]))
        return answer
