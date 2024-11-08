class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # combine to one list
        pos_speed = []
        for i, p in enumerate(position):
            pos_speed.append((p, speed[i]))
        # sort by position
        pos_speed.sort(key=lambda x: x[0])

        # fleets
        stack = []
        new_positions = position
        while new_positions != [target] * len(position):
            for i, s in enumerate(speed):
                new_positions[i] += s
                if not stack or stack[-1] > new_positions[i]:
                    stack.append(new_positions[i])
                else:
                    # a car has caught up to another
                    new_positions[i] = stack[-1]
                    # TODO: identify fleet
                    # TODO: update speed somehow
