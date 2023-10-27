def BS(arr, ele):
    start = 0
    end = len(arr) - 1 
    while start<=end:
        mid = start + (end-start)//2
        if ele == arr[mid]:
            return mid
        elif ele<arr[mid]:
            end = mid - 1 
        elif ele>arr[mid]:
            start = mid + 1 
    return -1
            
nums = [1,2,3,4,5,6,7,8,9]
ele = 88 
bs = BS(nums,ele)
print(bs)
