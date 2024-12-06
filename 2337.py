class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        return self.canChange1(start, target)

    def canChange2(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # handle L
        def findL(target, lastL):
            """
            Finds the index of the next L in target given the last one found
            If no next L is found, return -1
            Scans left to right
            """
            l = lastL + 1
            while l < len(target):
                if target[l] == 'L':
                    return l
                l += 1
            return -1

        l = obstruction = leftestL = -1
        l += 1
        while l < len(start):
            char = start[l]
            if char == 'R':
                obstruction = l
            if char == 'L':
                leftestL = findL(target, leftestL)
                if leftestL == -1 or l < leftestL or leftestL <= obstruction:
                    return False
                obstruction = leftestL
            l += 1

        # There are L pieces left to move in target
        if findL(target, leftestL) != -1:
            return False

        # handle R
        def findR(target, lastR):
            """
            Finds the index of the next R in target given the last one found
            If no next R is found, return -1
            Scans right to left
            """
            r = lastR - 1
            while r > -1:
                if target[r] == 'R':
                    return r
                r -= 1
            return -1

        r = obstruction = rightestR = len(target)
        r -= 1
        while r > -1:
            char = start[r]
            if char == 'L':
                obstruction = r
            if char == 'R':
                rightestR = findR(target, rightestR)
                if rightestR == -1 or r > rightestR or rightestR >= obstruction:
                    return False
                obstruction = rightestR
            r -= 1

        # There are R pieces left to move in target
        if findR(target, rightestR) != -1:
            return False

        return True

    def canChange1(self, start, target):
        """
        Determines validity by mapping target's L and R piece positions, then
        constructing that result from the characters in start
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
                if not L_positions:
                    return False
                # the L piece in start is further left than the L piece in target
                if i < L_positions[0]:
                    return False
                # something is blocking the L piece in start from moving to its correct position in target
                elif L_positions[0] <= obstruction:
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
                elif obstruction <= R_positions[-1]:
                    return False
                # R is unobstructed from moving to its correct position in target
                else:
                    end[i] = "_"
                    end[R_positions[-1]] = "R"
                    R_positions.pop()
        # there were too few R pieces in start; or not enough could be moved
        if R_positions:
            return False

        return True


start = "_L__R__RL"
target = "L_____RLR"
print(Solution().canChange(start, target))
