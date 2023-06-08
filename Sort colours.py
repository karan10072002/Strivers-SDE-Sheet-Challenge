def sort012(nums, n) :
    low, mid, high = 0, 0 , n-1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low], nums[mid]
            mid+=1
            low+=1
        elif nums[mid] == 1:
            mid+=1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high-=1

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n
