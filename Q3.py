# Using binary search method 
def Search(array, left, right):
    
    mid = (left+right)//2
    
    #base case --> ex. arr[0]=3 , Complexity is O(1)
    if(left == right and array[mid]!= mid):
        return -1
    #Complexity is O(1)
    if(array[mid]== mid): 
        return mid
    # if mid is greater than mid index, we check the left parts, because the array is already sorted
    if(array[mid]> mid):
        return Search(array, left, mid)
     # if mid is smaller than mid index, we check the right parts, because the array is already sorted
    if(array[mid]< mid):
        return Search(array, mid+1, right)
    
    # driver codes
array= [-3,0,1,2,4]
returnVal = Search(array,0, len(array)-1)
if(returnVal== -1): 
    # if there is not an index i for A[i]=i
    print("Not founded ", returnVal)
else:
    print("Founded element is ", returnVal)

