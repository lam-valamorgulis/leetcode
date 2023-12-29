# https://leetcode.com/problems/find-the-duplicate-number/


class Solution(object):

  def findDuplicate(self, nums):
    # note:
    # + floyd cycle detection
    # + because if the pointer to next is null it mean linked list is end
    # + how to detection a cycle ?
    # in linked list , can use set to find
    # + how to find meet up point:
    # slow and fast pointer will move
    # slow move 1 step
    # fast move 2 step
    # the first time meet , it mean there has a cycle => find the entrance of cycle
    # + how to make array transfer to linked list
    # value = index
    # pointer = value of arr
    # (index, value)

    slow = nums[0]
    fast = nums[0]

    # move pointer until they meet
    while True:
      slow = nums[slow]
      fast = nums[nums[fast]]
      if slow == fast:
        break

    # move pointer to the start
    slow = nums[0]
    while slow != fast:
      slow = nums[slow]
      fast = nums[fast]
    return fast
