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

"""
Description
-----------
Takes a string with characters and checks if the parentheses are balanced
({<>}) = True
<{>)(){ = False

Parameters
----------
s : String
    String with brackets to test

Return
------
  : Boolean
    True or False
"""


def balanced(s):
    stack = Stack()
    push_chars = "<({["
    pop_chars = ">)}]"

    for char in s:
        if char in push_chars:
            stack.push(char)
        elif char in pop_chars:
            if not stack.size():
                return False
            else:
                top_stack_char = stack.pop()
                opposite_bracket = push_chars[pop_chars.index(char)]
            if top_stack_char != opposite_bracket:
                return False
        else:
            return False
    return not stack.size()

example1 = "((<>))"
example2 = "([)]"
example3 = "({<>})"
example4 = "<{>)(){"

print(balanced(example3))
