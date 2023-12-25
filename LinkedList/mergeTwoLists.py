# https://leetcode.com/problems/reorder-list/
# Key solution :
# 1.divide problem into smaller known problem : reversed linked list, merger two list
# 2.find the middle node of linked list
# 3.reversed second half of linked list
# 4. merge first and second half
# note : 
# -how to find the middle node of the linked list, ho
# -how to make a reversed linked list
# -how to disconnect the noode
# -how to merged 2 linked list

class Solution(object):

def reorderList(self, head):

    # Define a helper function to reverse a linked list
    def reverse_list(node):
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # Define a helper function to merge two linked lists
    def merge_lists(first, second):
        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second

    # 1. Find the middle node in the linked list
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half of the linked list
    second_half = reverse_list(slow.next)
    # 3. Disconnect the first half
    slow.next = None
    # 4. Merge the first and reversed second halves
    merge_lists(head, second_half)







    
    


solution = Solution()
