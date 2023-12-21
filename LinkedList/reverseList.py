# https://leetcode.com/problems/reverse-linked-list/
# Key solution :
# different betwen linked list with list, node will pointer to the next node


class Solution(object):

  def reverseList(self, head):
    # create 2 pointer, first pointer point to null, second point to head
    prev = None
    curr = head
    #  when curr is not none
    while curr:
      # linked list not a list, no index,
      # if break the chain, how we can continued the curr node to the next (traversial the linked list) ?
      # we have to store the curr node to temp node
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev


solution = Solution()
