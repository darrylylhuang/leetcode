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
                # there are too many L pieces in start to match target
                if not L_positions[0]:
                    return False
                # the L piece in start is further left than the L piece in target
                if i < L_positions[0]:
                    return False
                # something is blocking the L piece in start from moving to its correct position in target
                elif L_positions[0] < obstruction:
                    return False
                # L is unobstructed from moving to its correct position in target
                else:
                    end[i] = "_"
                    end[L_positions[0]] = "L"
                    L_positions.pop(0)
        # there were too few L pieces in start; or not enough could be moved
        if L_positions:
            return False

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
                # there are too many R pieces in start to match target
                if not R_positions:
                    return False
                # the R piece in start is further right than the R piece in target
                if i > R_positions[-1]:
                    return False
                # something is blocking the R piece in start from moving to its correct position in target
                elif obstruction < R_positions[-1]:
                    return False
                # R is unobstructed from moving to its correct position in target
                else:
                    end[i] = "_"
                    end[R_positions[-1]] = "R"
                    L_positions.pop()
        # there were too few R pieces in start; or not enough could be moved
        if R_positions:
            return False

        return True
