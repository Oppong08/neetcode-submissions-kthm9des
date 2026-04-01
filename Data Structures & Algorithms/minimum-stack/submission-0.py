class MinStack:

    def __init__(self):
        self.data = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    def pop(self) -> None:
        self.data.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1] 
        
