class Solution(object):
    def carFleet(self, target, position, speed):
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
