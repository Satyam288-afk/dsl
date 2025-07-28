
import time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"After pass {i + 1}: {arr}")

arr = [723, 105, 106,459,]





start_time=time.time()
bubble_sort(arr)
end_time=time.time()
print(end_time-start_time)
