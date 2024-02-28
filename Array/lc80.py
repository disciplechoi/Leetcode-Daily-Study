# 1st review(02.09.2024)
# 2nd Review(02.25.2024)

# for 문의 조건절이 변하는 변수는 넣지 않는 것이 좋다

from typing import List

# TC : O(N)
# MC : O(1)
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]


# 1.
# stack
def removeDuplicates(nums: List[int]) -> int:

    i, cnt = 1, 1

    while i < len(nums):

        print(nums)
        if nums[i] == nums[i - 1]:
            cnt += 1

            if cnt > 2:
                nums.pop(i - 1)
                i -= 1

        else:
            cnt = 1
        i += 1
    return None


print(removeDuplicates(nums))


# 2.
# array
# Time Complexity: O(n^2) -- pop()  worst case
# Space Complexity: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        cnt = 1
        k = len(nums)

        n = 0

        while n < len(nums) - 1:
            if nums[n] == nums[n + 1]:
                cnt += 1
                if cnt > 2:
                    nums.pop(n)
                    k -= 1
                    n -= 1
            elif nums[n] != nums[n + 1]:
                cnt = 1

            n += 1

        return k


# 3. (improvement of 2)
 아무리바도 이해안가는 알고리즘음..

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        index = 2  # 결과 리스트의 인덱스, 처음 두 개의 요소는 항상 포함

        for i in range(2, n):
            if nums[i] != nums[index - 2]:
                nums[index] = nums[i]
                index += 1

        return index
