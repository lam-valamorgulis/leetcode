# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Key word :
# two pointer : 
# + keeping the distance of 2 pointer, 
# + using pointer to modified the linked between node
# + when we modify the next pointer of first or second, we are actually modifying the next pointer of the dummy node, which, in turn, affects the linked list. Let me explain with an example:
# delele node : curr.next = curr.next.next


class Solution(object):

  # Here's a step-by-step breakdown:
  # Initially: dummy -> 1 -> 2 -> 3 -> 4 -> 5, n = 2
  # After moving first and second: dummy -> 0 -> 1 -> 2 -> 3 -> 4 -> 5
  # After traversing and removing the nth node: dummy -> 0 -> 1 -> 2 -> 3 -> 5
  # The modified list starts from dummy.next, so returning dummy.next gives us the correct head of the modified list.

  def removeNthFromEnd(head, n):
    # Create a dummy node to handle the case when the head needs to be removed
    dummy = ListNode()
    dummy.next = head

    # Use two pointers to maintain a gap of n nodes between them
    slow = fast = dummy

    # Move the fast pointer n+1 steps ahead
    for _ in range(n + 1):
      fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast:
      slow = slow.next
      fast = fast.next

    # Remove the nth node from the end
    slow.next = slow.next.next

    return dummy.next


solution = Solution()
