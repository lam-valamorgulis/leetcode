# https://leetcode.com/problems/merge-two-sorted-lists/
# Key solution :
# linked list all come down to the pointer(reference) node.next = nextnode
# note the way how we create an empty linked list, and a dummy start from null then pointer the first node
# when traversing, notice the way how update the curr node, and next dummny node (new_node = currnode.next)
# notice the way pointer is point to the location of memory
# traversing curr mean update the dummy list node


class Solution(object):
  # Input: list1 = [1,2,4], list2 = [1,3,4]
  # Output: [1,1,2,3,4,4]

  def mergeTwoLists(self, list1, list2):
    # create a dummy node :
    dummy = ListNode()
    # creat a current node to traverse the linked list :
    curr = dummy

    # traverse until no more node in list1 or list2 :
    while list1 and list2:
      if list1.val < list2.val:
        # curr.next point to the list1 :
        curr.next = list1
        # moving list1 to the next
        list1 = list1.next
        # otherwise list1.val >= list2.val
      else:
        # curr.next point to the list1 :
        curr.next = list2
        # moving list1 to the next
        list2 = list2.next
      # move curr to to the next
      curr = curr.next
    if list1:
      curr.next = list1
    if list2:
      curr.next = list2
    # The merged list starts from the next node of the dummy node (the first actual node in the merged list).
    return dummy.next


solution = Solution()
