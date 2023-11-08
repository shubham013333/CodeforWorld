def findSubArray(nums,n):
    summ = 0
    maxsize =-1 
     
    for i in range(0, n-1):
        if arr[i] == 0:
            summ = -1 
        else:
            summ = 1 
        for j in range(i+1, n):
            if arr[j] == 0:
                summ = summ + (-1) 
            else:
                summ = summ+1
            if summ == 0 and maxsize <j-i+1:
                maxsize = j-i+1 
                startindex = i 
    if maxsize == -1:
        print('No Such Subarray')
    else:
        print(startindex,' to', startindex + maxsize -1)
    return maxsize
arr = [1, 0, 0, 1, 0, 1, 1]
size = len(arr)
findSubArray(arr, size)

#Output - 0 to 5