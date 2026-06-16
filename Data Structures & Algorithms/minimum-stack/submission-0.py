class MinStack:

    def __init__(self):
        self.stack = deque()
        self.pair = ()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        _, lastMin = self.stack[-1]

        self.stack.append((val, min(val, lastMin)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
