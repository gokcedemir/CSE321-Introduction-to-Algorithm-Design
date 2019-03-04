#divides array of two parts; right and left 
def findingMax(array, left, mid, right):
    # left sub array
    leftSum = 0
    totalSumLeft = -5000 #min val
        
    # right sub array
    rightSum =0
    totalSumRight = -5000
        
    # calculate sum of right part 
    for i in range(mid+1, right+1):
        rightSum += array[i]
        if(rightSum > totalSumRight):
            totalSumRight = rightSum
        #Calculate sum of left part
    for j in range(mid,left-1,-1):
        leftSum += array[j]
        if(leftSum > totalSumLeft):
            totalSumLeft = leftSum
    #return sum of right and left part
    return totalSumRight+ totalSumLeft;

#Find the largest sum of subarrray in given array as parameter.
def LargestSubArray(array,left,right):
        
    #If array has only one element, the sum is equals this one element.
    if(right == left):
        return array[left]
    mid = (left+right)//2 
            
    forLeftPart = LargestSubArray(array, left, mid) #max sub array in left array
    forRightPart= LargestSubArray(array,mid+1, right) #max sub array in right array
    totalSum = findingMax(array, left,mid, right) # max sub array in array
            
    #The max() method returns the largest element in an iterable or largest of two or more parameters.
    returnVal = max(forLeftPart, forRightPart, totalSum)
    return returnVal
        
#main function 

array=[5, -6, 6, 7, -6, 7, -4, 3]
largestSum = LargestSubArray(array, 0, len(array)-1)
print("The contiguous subset with the largest sum is ", largestSum)

    
    
        
        
            