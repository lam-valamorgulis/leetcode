class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, m, n):
    # 1. Edge Case: If the list has only one node or none,
    # there's nothing to reverse.
    if self.length <= 1:
        return

  # 1 pre 2345 6
  # 1 pre 3245 6
    # 2. Create a dummy node. This will help in case we are 
    # reversing from the start of the list.
    dummy = Node(0)
    dummy.next = self.head  # Let it point to the start of the list.
 
    # 3. Initialize 'prev' pointer. This will end up pointing 
    # to the node just before the reversal starts.
    prev = dummy
 
    # 4. Move 'prev' to its intended position.
    # After this loop, 'prev' will be at index 'm - 1'.
    for i in range(m):
        prev = prev.next
 
    # 5. Initialize 'current' pointer. It will point 
    # to the node at position 'm', the start of the reversal.
    current = prev.next
 
    # 6. Begin Reversal:
    # This loop will perform the main task of reversing the
    # nodes between 'm' and 'n'.
    for i in range(n - m):
        # 6.1. 'temp' will point to the next node in line
        # that we want to reverse.
        temp = current.next
 
        # 6.2. Disconnect 'temp' from the list and 
        # point 'current' to the node after 'temp'.
        current.next = temp.next
 
        # 6.3. Prepare to insert 'temp' to its new position.
        # Connect 'temp' to the node immediately after 'prev'.
        temp.next = prev.next
 
        # 6.4. Now, connect 'prev' to 'temp' completing 
        # its new placement in the reversed segment.
        prev.next = temp
 
    # 7. If m was 0, then we reversed from the start and
    # we need to update the head of the list.
    self.head = dummy.next

    

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""

