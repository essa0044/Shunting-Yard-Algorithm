class Stack:

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return bool(self.stack)

    def clear(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            raise IndexError("can't pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None