# https://www.youtube.com/watch?v=EwjnF7rFLns
def selectionSort(arr):
  for i in range(len(arr)):
    index_min = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[i]:
        index_min = j
    # swap value between current index with actual value of min index
    arr[i], arr[index_min] = arr[index_min], arr[i]


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
