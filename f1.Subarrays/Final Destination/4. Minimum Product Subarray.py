# Python program for the above approach

# Function to find the minimum product
# of the minimum and maximum among all
# the possible subarrays
def findMinMax(a):

	# Stores resultant minimum product
	min_val = 1000000000

	# Traverse the given array arr[]
	for i in range(1, len(a)):

		# Min of product of all two
		# pair of consecutive elements
		min_val = min(min_val, a[i]*a[i-1])

	# Return the resultant value
	return min_val


# Driver Code
if __name__ == ("__main__"):

	arr = [6, 4, 5, 6, 2, 4, 1]

	print(findMinMax(arr))
