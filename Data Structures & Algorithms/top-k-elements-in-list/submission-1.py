class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        bucket =[[] for i in range(len(nums) + 1)] 
        result = []

        # Creating the hash to find freq of each number
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        # Creating the bucket sorting list
        for num, freq in hash.items():
            bucket[freq].append(num)

        for i in range(len(nums)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
        
        l = dict(sorted(hash.items(), key = lambda x: x[1], reverse = True))
        return list(l.keys())[:k]