from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = []
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d = {key: value for key, value in d.items() if value > 1}
        for key, value in d.items():
            a.append(sum(range(value)))
        return sum(a)

nums= [1,1,1,3,3,3]
p = Solution()
print(p.numIdenticalPairs(nums))
