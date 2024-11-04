class MinStack(object):

    def __init__(self):
        # val, current min
        self._stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self._stack:
            self._stack.append((val, val))
        else:
            self._stack.append((val, min(val, self._stack[-1][1])))

    def pop(self):
        """
        :rtype: None
        """
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self._stack[-1][1]
