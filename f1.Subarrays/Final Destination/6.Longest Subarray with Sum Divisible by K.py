def longestSubnumsWthSumDivByK(nums, N, k):
	maxl = 0
	for i in range(N):
		sum1 = 0
		for j in range(i, N):
			sum1 += nums[j]
			if sum1 % k == 0:
				maxl = max(maxl, j - i + 1)
	return maxl


nums = [2, 7, 6, 1, 4, 5]
n = len(nums)
k = 3

print("Length =", longestSubnumsWthSumDivByK(nums, n, k))
