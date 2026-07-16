class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        itr = len(stones)
        for i in range(itr):
            if len(stones) > 1:
                new = stones.sort()
                max_weight = stones.pop()
                second_max_weight = stones.pop()

                if max_weight == second_max_weight:
                    continue
                else:
                    stones.append(max_weight - second_max_weight)
        return stones[0] if stones else 0

        