#Input :  10, 3, 7 
#Output : 27783000

def product_subarrays(arr, n):
	product = 1;
	for i in range(0, n):
		for j in range(i, n):
			for k in range(i, j + 1):
				product *= arr[k];
	print(product, "\n");

arr = [ 10, 3, 7 ];
n = len(arr);

product_subarrays(arr, n)



def product_subarrays(arr, n):
	res = 1;
	for i in range(n):
		product = 1
		for j in range(i, n):
			product *= arr[j];
			res = res * product

	print(res);


arr = [ 10, 3, 7 ]
n = len(arr)
product_subarrays(arr, n)




