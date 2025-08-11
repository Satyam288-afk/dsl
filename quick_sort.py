def partition(arr, low, high):
    pivot = arr[high]
    i = low
    j = high - 1

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while j >= i and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[i], arr[high] = arr[high], arr[i]
    print(f"After partitioning with pivot {pivot}: {arr}")
    return i

def quick_sort(arr, low, high, depth=0):
    if low < high:
        pi = partition(arr, low, high)
        
    
        print(f"{'  ' * depth}Sorting left  of pivot index {pi}: {arr[low:pi]}")
        quick_sort(arr, low, pi - 1, depth + 1)
        
    
        print(f"{'  ' * depth}Sorting right of pivot index {pi}: {arr[pi+1:high+1]}")
        quick_sort(arr, pi + 1, high, depth + 1)

arr = [10, 7, 8, 9, 1, 5, 17, 32, 41]
print(f"Original array: {arr}")
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")
