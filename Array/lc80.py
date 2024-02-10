# 1st review(02.09.2024)

# 숫자가 나타나면 2번까지 카운트를 한다. 2번이상이면 
# 3번째부터 인덱스 -1씩 하고 마지막칸은 공백으로 넣어준다

from typing import List


nums = [1,1,1,2,2,3]
def removeDuplicates(nums: List[int]) -> int:
        
        if len(nums) == 1:
            return len(nums)
        
        count = 0
       

        for i in range(0, len(nums)-1):
            current = nums[i]
           # print("i : ", i)
            #print("len :", lenOfList)

            if count > 1:
                 for i in range(i, len(nums)-1):
                      nums[i] = nums[i+1]
            
            if current == nums[i+1] :
                count +=1
                  
            else:
                 count = 0

        print(nums)
        return len(nums)


print(removeDuplicates(nums))