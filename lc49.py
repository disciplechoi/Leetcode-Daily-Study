import collections
from typing import Collection, List

# 2회독 (1/27/2024)

# 자료 저장 형태
# key, value => Hashmap (딕셔너리)
# eat = 1001
# 1001 : [eat, tea, ate]
# 1002 : [nat, tan]


#1)
# TC
# SC

#2)
# TC : O(NK)
# SC : O(N+26)K
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)
        if not strs:
            return None
        
        

        for word in strs: #N
            key_arr = [0]*26
            for s in word: #K
                key_arr[ord(s)-ord('a')]+=1

            anagrams[key_arr].append(strs)

        return anagrams.values()    
        



#3)
# TC
# SC