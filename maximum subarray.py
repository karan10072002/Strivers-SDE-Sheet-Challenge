from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(nums, n) :

    maximum= 0
    sum= 0
    if len(nums)==1:
        return nums[0]
    else:
        for i in nums:
            if (sum+i)>=i:
                sum+=i
            else:
                sum=i
            if sum>maximum:
                maximum=sum
                
        return maximum


#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
