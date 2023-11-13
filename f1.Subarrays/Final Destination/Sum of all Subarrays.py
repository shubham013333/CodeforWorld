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

#-----------------------O(N)--------------------------
def SubArraySum(arr, n):
	result = 0
	for i in range(0, n):
		result += (arr[i] * (i+1) * (n-i))
	return result

arr = [1, 2, 3]
n = len(arr)
print("Sum of SubArray : ",SubArraySum(arr, n))
