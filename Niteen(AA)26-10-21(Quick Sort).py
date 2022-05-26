#Quick Sort
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  return i + 1
def qs(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    qs(arr, low, pi - 1)
    qs(arr, pi + 1, high)
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted lst of ele")
print(data)
size = len(data)
qs(data, 0, size - 1)
print('Sorted list')
print(data)
#o(n suare)