"""
* Review
 - 1st : 02/21/24

 

* Solution
1) native - time exceeded 
- you need to think about the case given large array and the target indexs are located in the last.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

       
        answer = []

        for i in range (0, len(numbers)-1):
            for j in range (i+1, len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    answer.append(i+1)
                    answer.append(j+1)
                    return answer
"""