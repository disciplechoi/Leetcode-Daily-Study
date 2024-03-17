""""
* Review
 - 1st : 02/20/24
 - 2nd : 03/17/24


 
* Solution
1) Naive - Me
TC : O(len(T))
MC : O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        answer = False
        s_index = 0

        if len(s) == 0 :
            answer = True
            return answer
        
        for t_index in range(0, len(t)) :
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1

        if s_index == len(s):
            answer = True


        return answer

 1-1) Runtime enhancement
 class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        
        for t_index in range(0, len(t)) :
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1

        return s_index == len(s)
            
        
"""

"""
2nd Review
"""

# 결국은 첫 번째 리뷰에서 봤던 방식과 똑같이 구현했다.
# 아래 알고리즘은 다른사람이 푼 방식인데. 나는 여전히 첫번째 방식이 t가 긴경우에는 순회를 끝까지 해도 되지 않아 성능이 더 좋다고 생각한다.
def isSubsequence(self, s: str, t: str) -> bool:
 if len(s) == 0:
            return True

        s_index = 0
        
        for t_index in range (0, len(t)) :
            if s[s_index] == t[t_index]:
                s_index +=1
                if s_index == len(s):
                    return True


        return False        
        

 def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
