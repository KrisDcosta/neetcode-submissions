class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        l = dict(sorted(hash.items(), key = lambda x: x[1], reverse = True))
        return list(l.keys())[:k]