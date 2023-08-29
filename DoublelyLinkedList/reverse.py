class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    def reverse(self):
    # 1. Initialize 'current_node' to the starting node of the doubly linked list.
    current_node = self.head
    
    # 2. Traverse through each node of the doubly linked list.
    while current_node is not None:
        # 2.1. Swap the 'next' and 'prev' pointers of the current node. 
        # This effectively reverses the direction of the node's pointers.
        current_node.prev, current_node.next = current_node.next, current_node.prev
        
        # 2.2. Since the 'next' and 'prev' pointers of the 'current_node' 
        # have been swapped, we move to what was originally the 'prev' 
        # node to continue the reversal. 
        # Note: In a reversed scenario, 'prev' becomes 'next', hence we use 'prev'.
        current_node = current_node.prev
 
    # 3. After all nodes have been reversed, the original head becomes the tail 
    # and the original tail becomes the head. Swap the 'head' and 'tail' of the linked list.
    self.head, self.tail = self.tail, self.head





my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""

