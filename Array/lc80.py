# 1st review(02.09.2024)

#for 문의 조건절이 변하는 변수는 넣지 않는 것이 좋다

from typing import List

#TC : O(N)
#MC : O(1)
nums = [0,0,1,1,1,1,2,3,3]

def removeDuplicates(nums: List[int]) -> int:

    i, cnt = 1,1

    while(i<len(nums)) :

        print(nums)
        if nums[i] == nums[i-1]:
            cnt+=1

            if cnt > 2:
                nums.pop(i-1)
                i-=1

            
        else:
            cnt = 1
        i+=1
    return None

print(removeDuplicates(nums))