""""
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
        
"""