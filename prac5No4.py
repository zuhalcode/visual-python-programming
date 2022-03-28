# Python Program to Check if String is Palindrome using Stack
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
string = "zuhal"
for i in string:
    stack.push(i)

reversed_string = ""
for i in range(len(string)):
    reversed_string += stack.pop()

if string == reversed_string:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')