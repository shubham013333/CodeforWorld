''' Input: nums = [-1, 4, 5, -9]
    Output: -9'''
def maxsubArray(nums):
    if not nums:
        return 0
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
    return max_sum
    
nums = [-1,4,5,-9]

res = maxsubArray(nums)
print(res)
    