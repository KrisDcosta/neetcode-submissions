class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        read = 0
        write = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
            read += 1

        for j in range(write, n):
            nums[j] = 0

        return nums
        