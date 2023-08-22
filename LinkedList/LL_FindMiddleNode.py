class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        
        # 12345
    def get(self, index):
        # if index < 0 or index >= self.length:
        #     return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def find_middle_node(self):
        index = 0
        temp = self.head
        while temp is not None :
            index +=1
            temp = temp.next
        if index % 2 != 0:
            return self.get(round(index//2))
        else :
            return self.get(index//2)

          



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""