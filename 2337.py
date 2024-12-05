class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        L_positions = []
        R_positions = []
        for i, char in enumerate(target):
            if char == 'L':
                L_positions.append(i)
            if char == 'R':
                R_positions.append(i)
