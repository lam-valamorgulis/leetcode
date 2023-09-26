class Solution(object):

  # Solution 1 : O(n^2)
  # def productOfArray(self, nums):
  #   res = []
  #   for i in range(len(nums)):
  #     n = 1
  #     for j in range(len(nums)):
  #       if i != j:
  #         n = n * nums[j]
  #     res.append(n)
  #   return res

  # solution 2 : O(n) space O(n)
  def productOfArray(self, nums):
    n = len(nums)
    # create a list for left and right product with default value is 1
    left_product = [1] * n
    right_product = [1] * n
    res = [0] * n

    # traverse from the left
    l_product_num = 1
    for i in range(n):
      left_product[i] = l_product_num
      l_product_num *= nums[i]

    # traverse from the right
    r_product_num = 1
    for j in range(n - 1, -1, -1):
      right_product[j] = r_product_num
      r_product_num *= nums[j]

    print(right_product)
    for k in range(n):
      res[k] = left_product[k] * right_product[k]
    return res


sol = Solution()
testA = sol.productOfArray([5, 2, 3, 4])
print(testA)
testB = sol.productOfArray([-1, 1, 0, -3, 3])
print(testB)
