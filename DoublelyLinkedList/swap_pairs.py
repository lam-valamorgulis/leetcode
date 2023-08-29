class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
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
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

        
      
      

    def swap_pairs(self):
    # 1. Initialize a dummy node that acts as a preceding node to the head.
    dummy = Node(0)
    dummy.next = self.head
    prev = dummy
 
    # 2. Loop through the doubly linked list in pairs as long as there are 
    # at least two nodes left.
    while self.head and self.head.next:
        # 2.1. 'first_node' points to the first node in the current pair.
        first_node = self.head
        # 2.2. 'second_node' points to the second node in the current pair.
        second_node = self.head.next
 
        # 2.3. Update the 'next' of the 'prev' node to point to 'second_node' 
        # since pairs are being swapped.
        prev.next = second_node
        
        # 2.4. Update the 'next' of 'first_node' to be the node after 'second_node'.
        first_node.next = second_node.next
        
        # 2.5. Update the 'next' of 'second_node' to point to 'first_node', 
        # completing the swap.
        second_node.next = first_node
        
        # 2.6. Set the previous pointers accordingly. 'second_node' will now 
        # precede 'first_node', so we set 'first_node's 'prev' to 'second_node'.
        second_node.prev = prev
        first_node.prev = second_node
        
        # 2.7. Update the 'prev' of the next node after the swapped pair 
        # to point back to 'first_node', if that node exists.
        if first_node.next:
            first_node.next.prev = first_node
 
        # 2.8. Move the head pointer to start at the next pair of nodes.
        self.head = first_node.next
        
        # 2.9. Update 'prev' to point to 'first_node' for the next iteration.
        prev = first_node
 
    # 3. After all pairs have been swapped, update the head of the linked list 
    # to point to the node after 'dummy', which is the new start of the list.
    self.head = dummy.next
    
    # 4. Set the 'prev' of the new head to None since it's the start of the list.
    if self.head:
        self.head.prev = None




my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""