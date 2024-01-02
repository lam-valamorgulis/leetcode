# Definition for singly-linked list.

# Overall:
# traversial the LL, step of traversial is the K-reversed-order
# take small chunk
# - reverse each K group
# - connect prevGruop to nextGruop
# Q&A:
# - how to reverse a given a LL ?
# - how to connect prevGruop to the nextGruop ?
# - how to find a kth in LL
# - how to traversal a LL
# Step:
# -

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

  # helper function to get k-th
  def getKth(self, curr, k):
    while curr and k > 0:
      curr = curr.next
      k -= 1
    return curr

  def reverseKGroup(self, head, k):

    # creat a dummy point to the head of LL
    # The dummy node ensures that the first group is treated the same way as subsequent groups.
    dummy = ListNode(0, head)
    # make a groupPrev to traversial the step-k-reversed LL:
    # groupPrev will point to the node before the starting group
    groupPrev = dummy

    while True:
      # navigate to the Kth node (k-group)
      kth = self.getKth(groupPrev, k)

      # if can't form a k-group then exit the loop
      if not kth:
        break

      groupNext = kth.next

      # reversed group before kth
      # init the curr, prev node
      # prev is the next of kth node because it will not break the LL
      prev, curr = kth.next, groupPrev.next
      while curr != groupNext:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
      # after revered the group
      # connect the end of prev node of revered group to the next k-group
      # the groupPrev.next is point to the last of reversed groupNext
      # save node before group for next iteration
      tmp = groupPrev.next
      # to connect the groupPrev to the reversed groupNext
      groupPrev.next = kth
      # update move groupPrev to next iteration
      groupPrev = tmp
    return dummy.next
