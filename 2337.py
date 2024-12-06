class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        return self.canChange3(start, target)

    def canChange3(self, start, target):
        """
        Utilizes the fact that pieces cannot cross each other to do a single pass through
        both input strings; find matching pieces and determine whether target's position can be achieved
        from start's position
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i = j = 0
        # add stop characters to prevent one of the strings from ending the loop early without checking validity
        start += '\0'
        target += '\0'
        while i < n or j < n:
            # skip empty spaces in start
            while i < n and start[i] == '_':
                i += 1
            # skip empty spaces in target
            while j < n and target[j] == '_':
                j += 1

            piece = start[i]
            # pieces are not equivalent; this is impossible since pieces cannot cross each other
            if piece != target[j]:
                return False
            # L pieces cannot move to the right
            elif piece == 'L' and i < j:
                return False
            # R pieces cannot move to the left
            elif piece == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True

    def canChange2(self, start, target):
        """
        Uses helper functions to find the next piece position in target
        Traverses start forwards and backwards to simulate movement of pieces
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
