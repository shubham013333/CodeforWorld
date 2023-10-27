def NumberTimesSortedRotatedArray(arr):
    start = 0
    end = len(arr) - 1
    N = len(arr)
    
    while start <= end:
        mid = start + (end - start) // 2
        next_index = (mid + 1) % N
        prev_index = (mid + N - 1) % N
        
        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
            return mid
        elif arr[start] <= arr[mid]:
            start = mid + 1
        elif arr[mid] <= arr[end]:
            end = mid - 1
    
    return -1

nums = [11, 1, 2, 15, 18, 2, 5, 6, 8]
ans = NumberTimesSortedRotatedArray(nums)
print(ans)

