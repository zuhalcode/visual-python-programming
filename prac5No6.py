# infix to postfix
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]

class InfixToPostfix:
    def __init__(self):
        self.stack = Stack()
        self.postfix = []

    def isOperator(self, char):
        if char == '+' or char == '-' or char == '*' or char == '/':
            return True
        else:
            return False

    def isOperand(self, char):
        if char.isnumeric():
            return True
        else:
            return False

    def infixToPostfix(self, infix):
        for i in infix:
            if self.isOperand(i):
                self.postfix.append(i)
            elif self.isOperator(i):
                if self.stack.isEmpty():
                    self.stack.push(i)
                else:
                    if i == '+' or i == '-':
                        while self.stack.isEmpty() == False:
                            if self.stack.peek() == '*' or self.stack.peek() == '/':
                                self.postfix.append(self.stack.pop())
                            else:
                                self.stack.push(i)
                                break
                    elif i == '*' or i == '/':
                        while self.stack.isEmpty() == False:
                            if self.stack.peek() == '+' or self.stack.peek() == '-':
                                self.postfix.append(self.stack.pop())
                            else:
                                self.stack.push(i)
                                break
                    else:
                        self.stack.push(i)
            elif i == ' ':
                continue
            else:
                print('Invalid character')
                break
        while self.stack.isEmpty() == False:
            self.postfix.append(self.stack.pop())
        return self.postfix

    def evaluatePostfix(self, postfix):
        stack = Stack()
        for i in postfix:
            if self.isOperand(i):
                stack.push(i)
            elif self.isOperator(i):
                if stack.size() < 2:
                    print('Invalid postfix')
                    break
                else:
                    op1 = int(stack.pop())
                    op2 = int(stack.pop())
                    if i == '+':
                        result = op1 + op2
                    elif i == '-':
                        result = op1 - op2
                    elif i == '*':
                        result = op1 * op2
                    elif i == '/':
                        result = op1 / op2
                    stack.push(result)
        return stack.pop()

infix = InfixToPostfix()
string = "5*(4-2)"
postfix = infix.infixToPostfix(string)
print(f'{string} to postfix is ',postfix)
print(f'{string} is ',infix.evaluatePostfix(postfix))
