'''Input: arr[] = {1, 2, 3}
Output: 20
Explanation: {1} + {2} + {3} + {2 + 3} + {1 + 2} + {1 + 2 + 3} = 20

Input: arr[] = {1, 2, 3, 4}
Output: 50'''

def sum_of_all_subarrays(nums):
    sm , res = 0,0

    for i in range(len(nums)):
        sm =0
        for j in range(i, len(nums)):
            sm+=nums[j] 
            res+=sm
    return res 

arr = [1,2,3,4]
res = sum_of_all_subarrays(arr)
print(res)