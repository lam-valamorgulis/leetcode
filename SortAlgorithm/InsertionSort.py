# https://www.youtube.com/watch?v=EwjnF7rFLns
def insertionSort(arr):
  for i in range(1, len(arr)):
    temp_val = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > temp_val:
      # move element which is its value greater than temp_val
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = temp_val


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
insertionSort(arr)
print('The array after sorting in Ascending Order by insertionSort  is:')
print(arr)
