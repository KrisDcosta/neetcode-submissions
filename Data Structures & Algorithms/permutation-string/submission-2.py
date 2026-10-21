class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq_target = {}
        freq_subs = {}
        for i in range(len(s1)):
            freq_target[s1[i]] = freq_target.get(s1[i], 0) + 1
        
        n = len(s2)    
        l = 0
        r = len(s1)-1

        for j in range(l, r+1):
            freq_subs[s2[j]] = freq_subs.get(s2[j], 0) + 1
        while (n > r+1):
            if freq_subs == freq_target:
                return True
            freq_subs[s2[l]] = freq_subs.get(s2[l], 0) - 1
            if freq_subs[s2[l]] == 0:
                del freq_subs[s2[l]]
            l += 1
            r += 1
            freq_subs[s2[r]] = freq_subs.get(s2[r], 0) + 1
        
        if freq_subs == freq_target:
            return True
        
        return False