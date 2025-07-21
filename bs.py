def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    operations = 0
    while low <= high:
        operations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, operations
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, operations 

input_str = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, input_str.split()))
arr.sort()
target = int(input("Enter the number to search for: "))
index, operations = binary_search(arr, target)

if index != -1:
    print(f"Number {target} found at index {index} after {operations} operations.")
else:
    print(f"Number {target} not found after {operations} operations.")
