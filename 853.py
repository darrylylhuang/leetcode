class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        return self.carFleet2(target, position, speed)

    def carFleet1(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # combine to one list
        pos_speed = [(p, s) for p, s in zip(position, speed)]
        # sort by position
        pos_speed.sort(key=lambda x: x[0], reverse=True)

        # fleets
        stack = []
        for ps in pos_speed:
            (pos, spd) = ps
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

    def carFleet2(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        position_time_map = {position[i]: (target - position[i]) / speed[i]
                             for i in range(len(position))}
        position.sort(reverse=True)

        stack = []
        for p in position:
            time = position_time_map[p]
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
