def FirstOccurenec(arr,ele):
    start = 0
    end = len(arr) - 1 
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if ele == arr[mid]:
            res = mid
            end = mid -1
        elif ele<arr[mid]:
            end = mid -1
        else:
            start = mid + 1 
    return res 

def LastOccurenec(arr,ele):
    start = 0
    end = len(arr) - 1 
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if ele == arr[mid]:
            res = mid
            start = mid + 1 
        elif ele<arr[mid]:
            end = mid -1
        else:
            start = mid + 1 
    return res 
    
nums = [1,2,3,20,20,20,80,110]
ele = 20
first = FirstOccurenec(nums, ele)
last = LastOccurenec(nums, ele)

count = last - first + 1 
print(count)

