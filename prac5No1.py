# STACK

class Stack:
    def __init__(self, items=[]):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def insertStack(string):
    s = Stack()
    index = 0
    while index < len(string) and string[index] != '*':
        symbol = string[index]
        if symbol == "*":
            s.pop()
        else:
            s.push(symbol)
        index += 1
    return s.items

    

character = 'E A S * Y * Q U E * * * S T * * * I O * N * * *'
stack = Stack(insertStack(character))
print(stack.items)




