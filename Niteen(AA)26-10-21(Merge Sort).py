def mergeSort(list):
    print("Splitting ",list)
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",list)

list = [54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)

#o(n)


# =============================================================================
# def mergeSort(array):
#     if len(array) > 1:
# 
#         #  r is the point where the array is divided into two subarrays
#         r = len(array)//2
#         L = array[:r]
#         M = array[r:]
# 
#         # Sort the two halves
#         mergeSort(L)
#         mergeSort(M)
# 
#         i = j = k = 0
# 
#         # Until we reach either end of either L or M, pick larger among
#         # elements L and M and place them in the correct position at A[p..r]
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
# 
#         # When we run out of elements in either L or M,
#         # pick up the remaining elements and put in A[p..r]
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1
# 
#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1
# 
# 
# # Print the array
# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()
# 
# 
# # Driver program
# if __name__ == '__main__':
#     array = [6, 5, 12, 10, 9, 1]
# 
#     mergeSort(array)
# 
#     print("Sorted array is: ")
#     printList(array)
# =============================================================================
