import collections

ransomNote = "aa"
magazine = "aab"

"""
* Review
- 1st 2/22/24


"""


# Sol 1)
# TC O(len(ransomeNote)+len(magazine))
# MC O(len(magazine))
def canConstruct(ransomNote: str, magazine: str) -> bool:

    answer = True

    lc = collections.defaultdict(int)

    for m in magazine:
        if lc[m] != None:
            lc[m] = lc[m] + 1
        else:
            lc[m] = 0

    for r in ransomNote:
        if lc[r] > 0:
            lc[r] = lc[r] - 1
        else:
            answer = False

    # print(lc)
    return answer


print(canConstruct(ransomNote, magazine))


# Sol2 - Sol1 enhancement
def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    letter_count = collections.defaultdict(int)

    for m in magazine:
        letter_count[m] += 1

    for r in ransomNote:
        if letter_count[r] > 0:
            letter_count[r] -= 1
        else:
            return False

    return True


# Sol3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False

        return True
