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

        end = [char for char in start]

        # handle L
        obstruction = -1
        for i, char in enumerate(end):
            if char == '_':
                continue
            elif char == 'R':
                obstruction = i
            elif char == 'L':
                # the L piece in start is further left than the L piece in target
                if i < L_positions[0]:
                    return False
                # something is blocking the L piece in start from moving to its correct position in target
                elif L_positions[0] < obstruction:
                    return False
                # L is unobstructed from moving to its correct position in target
                else:
                    end[L_positions[0]] = "L"
                    end[i] = "_"
                    L_positions.pop(0)

        # handle R
        obstruction = len(target)
        for i in range(len(target) - 1, -1, -1):
            char = end[i]
            if char == '_':
                continue
            if char == 'L':
                obstruction = i
            # the R piece in start is further right than the R piece in target
            elif char == 'R':
                if i > R_positions[-1]:
                    return False
                # something is blocking the R piece in start from moving to its correct position in target
                elif obstruction < R_positions[-1]:
                    return False
                # R is unobstructed from moving to its correct position in target
                else:
                    end[R_positions[-1]] = "R"
                    end[i] = "_"
                    L_positions.pop()

        return True
