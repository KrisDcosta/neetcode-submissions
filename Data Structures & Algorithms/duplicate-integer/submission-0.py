class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = []
        for check_element in nums:
            if check_element not in duplicate_check:
                duplicate_check.append(check_element)
            else:
                return True
        return False
        