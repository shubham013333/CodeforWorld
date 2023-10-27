def FirstOccurence(arr,ele):
    start = 0
    end = len(arr) -1
    res = -1
    
    while start <= end:
        mid = start + (end - start)//2
        if ele == arr[mid]:
            res = mid
            end = mid-1
        elif ele<arr[mid]:
            end = mid -1 
        else:
            start = mid + 1 
    return res 

def LastOccurence(arr,ele):
    start = 0
    end = len(arr) -1
    res = -1
    
    while start <= end:
        mid = start + (end - start)//2
        if ele == arr[mid]:
            res = mid
            start = mid +1 
        elif ele<arr[mid]:
            end = mid -1 
        else:
            start = mid + 1 
    return res 

nums = [1,2,10,10,10,40,50,90]
ele = 10 
first = FirstOccurence(nums, ele)
Last = LastOccurence(nums, ele)
print(first)
print(Last)
