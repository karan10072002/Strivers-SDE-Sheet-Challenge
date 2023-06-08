def nextPermutation(self, nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i - 1] < nums[i]:
            nums[i:] = sorted(nums[i:])
        i = i - 1
        for k in range(i, len(nums)):
            if nums[i] < nums[k]:
                nums[k], nums[i] = nums[i], nums[k]
                return nums
    return nums.reverse()
