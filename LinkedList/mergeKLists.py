# https://leetcode.com/problems/merge-k-sorted-lists/
# Note:
# + merge 2 sorted list
# + what is Logk time complexity
# + how to loop with k step in python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

        # helper merged 2 lists
    def merged_2_list(self,list1, list2):
        dummy = ListNode()
        curr = dummy
    # and operator to ensure that traversial both linked list until each one of linked list reach None
        while list1 and list2:
            if list1.val < list2.val :
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
        # Move the current pointer to the last added node
            curr = curr.next  
        # Append the remaining elements from either list
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next

    def mergeKLists(self, lists):
        while len(lists) > 1 :
            merged_list = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged_list.append(self.merged_2_list(l1,l2))
            lists = merged_list
        return lists[0] if lists else None



