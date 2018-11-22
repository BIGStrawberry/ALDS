"""
Student Naam:   Wouter Dijkstra
Student Nr. :   1700101
Klas        :   ??
Docent      :   frits.dannenberg@hu.nl
"""

"""
Description
-----------
A stack class, an extension of a list.
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def clear(self):
        while self.size() > 0:
            self.pop()

# Create stack instance
stack = Stack()

# Testing the Stack Class (-:
print("Is stack empty?: %s" % stack.is_empty())
stack.push(4)
stack.push("platform")
print("Peek: %s " % stack.peek())
stack.push(True)
print("Is stack empty?: %s" % stack.is_empty())
print("Stack size: %d" % stack.size())
stack.push(4.1)
print("Stack size: %d" % stack.size())
print("Popping ", stack.pop())
print("Popping ", stack.pop())
print("Stack size: %d" % stack.size())
stack.push(True)
print("Peek: %d " % stack.peek())

stack.clear()
print("Is stack empty?: %s" % stack.is_empty())
