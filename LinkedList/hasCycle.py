# https://leetcode.com/problems/linked-list-cycle/submissions/1130176487/
# Key word :
# hash table
# slow and fast pointer will move until they meet


class Solution(object):
  def hasCycle(self, head):
# solution 1 : using set to create a unique hash map 

      # In Python, a set is an unordered collection of unique elements. It is a built-in data type that is used to store multiple items in a single variable. The primary characteristics of a set are:
      # visited = set()  # Use a set to store visited nodes
      # curr = head

      # while curr:
      #     if curr in visited:
      #         return True  # Cycle detected
      #     visited.add(curr)
      #     curr = curr.next

      # return False  # No cycle found

#  solution 2 : 
# if slow catch up the fast pointer then it is has a cycle
      if not head or not head.next:
          return False

      #  init 2 pointer
      slow = head
      fast = head.next
      while slow != fast :
          if not fast or not fast.next:
              return False
      # Move the slow pointer one step and the fast pointer two steps
          slow = slow.next
          fast = fast.next.next
      return True


# solution = Solution()
