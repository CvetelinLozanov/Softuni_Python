class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise ValueError("")
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


stack = Stack()
stack.push('1')
stack.push('2')
stack.push('3')
print(stack.pop())
print(stack.top())
print(stack.is_empty())
print(stack)