def SubArraySum(arr, n):
	summ, result = 0, 0
	
	for i in range(0, n):
		summ = 0
		for j in range(i, n):
			summ += arr[j]
			result += summ
	return result

arr = [1, 2]
n = len(arr)
print("Sum of SubArray :", SubArraySum(arr, n))