# Infix checker
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
stack = Stack()
string = "5*(4-2)"
for i in string:
    if i == '(' or i == '[' or i == '{':
        stack.push(i)
    elif i == ')' or i == ']' or i == '}':
        if stack.isEmpty():
            print(f'{i} is not a valid infix expression')
            break
        else:
            if i == ')' and stack.pop() == '(':
                continue
            elif i == ']' and stack.pop() == '[':
                continue
            elif i == '}' and stack.pop() == '{':
                continue
            else:
                print(f'{i} is not a valid character')
                break
else:
    if stack.isEmpty():
        print(f'{string} is a correct expression')
    else:
        print(f'{string} is not a correct expression')

