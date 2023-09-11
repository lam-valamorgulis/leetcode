# https://www.youtube.com/watch?v=Dv4qLJcxus8

def bubbleSort (arr) :
  for i in range(len(arr) - 1) :
    for j in range(len(arr) - 1 - i) :
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)

print(arr)