def asc_bs(arr,ele):
    start = 0
    end = len(nums) - 1 
    while start <= end:
        mid = start + (end - start)//2
        if ele == arr[mid]:
            return mid
        elif ele<arr[mid]:
            end = mid -1 
        else:
            start = mid + 1 
    return -1 
    
def dec_bs(arr,ele):
    start =0
    end = len(nums) - 1 
    while start <= end:
        mid = start + (end-start)//2
        if ele == arr[mid]:
            return mid
        elif ele<arr[mid]:
            start = mid+1
        else:
            end = mid -1 
    return -1 
    
nums = [9,8,7,6,5,4,3,2,1]
ele = 7
if nums[0]<nums[1]:
    a_bs = asc_bs(nums,ele)
    print(a_bs)
else:
    d_bs = dec_bs(nums, ele)
    print(d_bs)
