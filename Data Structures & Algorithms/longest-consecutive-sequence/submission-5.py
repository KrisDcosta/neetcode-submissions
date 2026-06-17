class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                sequence_length = 1
                while current + 1 in nums_set:
                    sequence_length += 1
                    current += 1
                longest_consecutive = max(sequence_length, longest_consecutive)
        return longest_consecutive


        