class MinStack(object):

    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self._min is None or val < self._min:
            self._min = val
        self._stack.append(val)

    def pop(self):
        """
        :rtype: None
        """

    def top(self):
        """
        :rtype: int
        """

    def getMin(self):
        """
        :rtype: int
        """
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
