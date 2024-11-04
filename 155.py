class MinStack(object):

    def __init__(self):
        self._stack = []
        self._mins = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self._mins or val <= self._mins[-1]:
            self._mins.append(val)
        self._stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self._stack[-1] == self._mins[-1]:
            self._mins.pop()
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._mins[-1]
