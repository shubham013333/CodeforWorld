'''Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.'''

def max_cir_array(nums,n):
    if n ==1:
        return nums[0]
    max_arr = nums[0]
    max_so_far = nums[0]
    min_arr = nums[0]
    min_so_far = nums[0]
    sm = 0
    for i in range(n):
        sm += nums[i]
    
    for i in range(1,n):
        max_arr = max(nums[i], nums[i] + max_arr)
        max_so_far = max(max_so_far,max_arr)
        min_arr = min(nums[i], nums[i] + min_arr)
        min_so_far = min(min_arr, min_so_far)
        
        if sm == min_so_far:
            return max_so_far
    return max(max_so_far, sm - min_so_far)
    
    
nums =[1,-2,-3,-3,10]
n = len(nums)
res = max_cir_array(nums,n)
print(res)