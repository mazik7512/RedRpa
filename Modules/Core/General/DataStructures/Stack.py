from Modules.Core.Abstract.General.DataStructures.Stack import AbstractStack


class STDStack(AbstractStack):

    def __init__(self):
        self._stack = []
        self._last = -1

    def pop(self):
        self._stack.pop(self._last)

    def top(self):
        return self._stack[self._last]

    def push(self, data):
        self._stack.append(data)
        self._last += 1

    def deserialize(self):
        return str(self._stack)
