from stack import Stack

class ExpressionEvaluator:
    def __init__(self, invert_precedence=False):
        self.output = [] #creating empty list to store output
        self.operators = {"+", "*"} #Defining operators
        
        

    def parse(self, expression):
        stack = Stack()
        for char in expression:
            if isinstance(char, int):
                self.output.append(char)
            elif char in self.operators:
                last_operator = stack.peek()
                if last_operator == "*" and char == "+":
                    self.output.append(stack.pop())
                    stack.push(char)
                else:
                    stack.push(char)

        while stack:
            self.output.append(stack.pop)

        return self.output

    def evaluate(self, expression):
        pass
