def subarray_sum(nums, target):
  # Dictionary to store the running sums (keys) and
  # their corresponding indices (values).
  sum_index = {0: -1}

  # Variable to keep track of the current running sum.
  current_sum = 0

  # Iterate through the list with both index and value.
  for i, num in enumerate(nums):
    # Add the current number to the running sum.
    current_sum += num

    # Check if there's a subarray sum that matches the target.
    if current_sum - target in sum_index:
      # If there's a match, we return the start and end
      # indices of that subarray.
      #
      # 'sum_index[current_sum - target] + 1' gives the start
      # index of the subarray:
      # It accesses the index stored in sum_index where the
      # subarray begins (current_sum - target). We add 1
      # because Python is 0-indexed and we want the first
      # element of the subarray, not the element before it.
      #
      # 'i' gives the end index of the subarray:
      # It's the current index in the loop, where the
      # subarray ends as the cumulative sum up to this
      # index equals the target when we subtract the sum at
      # the start of the subarray.
      return [sum_index[current_sum - target] + 1, i]

    # If no subarray sum has been found, store the current
    # running sum and its corresponding index.
    sum_index[current_sum] = i

  # If no subarray sum is found after iterating through the
  # entire list, return an empty list.
  return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
