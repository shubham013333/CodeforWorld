def countOne(arr, n) : 
	i = 0
	Len = 0
	ans = 0
	
	while(i < n) : 
		if(arr[i] == 1): 
			Len = 0
			while(i < n and arr[i] == 1) :
				i += 1
				Len += 1
			ans += (Len*(Len+1)) // 2
		i += 1
	
	return ans
def findSubarrayCount(arr, n, k) : 

	start, endval, p, countOnes, res = 0, 0, 1, 0, 0

	while (endval < n) : 
	
		p = p * (arr[endval])
		if(p > k) :
		
			while(start <= endval and p > k) :
			
				p = p // arr[start]
				start += 1
				
		if(p == k) :
			countOnes = 0
			while endval + 1 < n and arr[endval + 1] == 1 :
			
				countOnes += 1
				endval += 1
			res += (countOnes + 1) 
			while(start <= endval and arr[start] == 1 and k!=1) : 
			
				res += (countOnes + 1)
				start += 1
			p = p // arr[start] 
			start += 1

		endval += 1

	return res

arr1 = [ 2, 1, 1, 1, 3, 1, 1, 4 ] 
n1 = len(arr1) 
k = 1

if(k != 1) :
	print(findSubarrayCount(arr1, n1, k))
else :
	print(countOne(arr1, n1))

arr2 = [ 2, 1, 1, 1, 4, 5]
n2 = len(arr2)
k = 4

if(k != 1) :
	print(findSubarrayCount(arr2, n2, k))
else :
	print(countOne(arr2, n2))

