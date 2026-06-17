class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            countS = [0]*26
            for c in s:
                countS[ord(c)-ord('a')] += 1
            hash[tuple(countS)].append(s)
        return list(hash.values())
            

    
        # for i in range(len(strs)):
        #     anagrams = []
        #     hash[strs[i]] = hash.get(strs[i], 0) + 1
        #     if hash[strs[i]] == 1: 
        #         anagrams.append(strs[i])
        #         for j in range(i + 1, len(strs)):
        #             if len(strs[i]) == len(strs[j]):
        #                 if sorted(strs[i]) == sorted(strs[j]):
        #                     hash[strs[i]] = hash.get(strs[i], 0) + 1
        #                     hash[strs[j]] = hash.get(strs[j], 0) + 1
        #                     anagrams.append(strs[j])
        #         group.append(anagrams)
                            
        return group 