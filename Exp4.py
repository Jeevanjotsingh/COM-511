#Linear Search
'''def linear_search(arr , key):
    for i in range(0,len(arr)):
        if key == arr[i]:
            return i
    return -1

# Sample list of elements
arr = [2,1,7,45,89,33,66]
key = 89
result = linear_search(arr , key)
print("Using linear search :")
if result != -1:
    print(f"{key} found at index {result}.")
else:
    print(f"{key} not found in the list.")'''


# Binary Search
def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Sample list of elements
arr = [10, 20, 30, 40, 50]
key = 50
result = binary_search(arr, key, 0, len(arr) - 1)
print("Using binary search :")
if result != -1:
    print(f"{key} found at index {result}.")
else:
    print(f"{key} not found in the list.")
