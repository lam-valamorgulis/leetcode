# divide and conquer algorithm
def quick_sort(arr):
  # base case if only one element it already sorted
  if len(arr) <= 1:
    return arr
  # Choose a pivot element (in this case, the last element)
  pivot = arr[-1]

  # Create empty lists for elements less than, equal to, and greater than the pivot
  less_than_pivot = []
  equal_to_pivot = []
  greater_than_pivot = []

  for element in arr:
    if element < pivot:
      less_than_pivot.append(element)
    elif element == pivot:
      equal_to_pivot.append(element)
    else:
      greater_than_pivot.append(element)

  # Recursively sort the sub-arrays (less than and greater than the pivot)
  sorted_less = quick_sort(less_than_pivot)
  sorted_greater = quick_sort(greater_than_pivot)

  # Combine the sorted sub-arrays and the elements equal to the pivot
  sorted_arr = sorted_less + equal_to_pivot + sorted_greater

  return sorted_arr


# Example usage
arr = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
