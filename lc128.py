# 2nd Review (01/29/2024)

# Solution 1)
# TC : n^3
# SC : 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        for num in nums:
            longest_cnt = 1
            cnt = 0

            while num +1 in nums:
                cnt+=1
                num+=1
            
            longest_cnt = max(longest_cnt, cnt)
            
            return longest_cnt



# Solution 2)
# TC : O(nlogn)
# SC : O(1)
from typing import List

nums =[1,2,0,1]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        nums.sort()
        
        current_cnt = 1
        longest_cnt = 1

        for i in range(0, len(nums)-1):
               
            if nums[i+1]== nums[i]+1:
                current_cnt+=1

            elif nums[i+1] == nums[i]:
                continue

            else:
                longest_cnt = max(current_cnt, longest_cnt)
                current_cnt = 1   

        return max(current_cnt, longest_cnt)
    
sol = Solution()
print(sol.longestConsecutive(nums))
