class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# Create a Stack class that represents a last-in, first-out (LIFO) data structure using a linked list implementation.


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""