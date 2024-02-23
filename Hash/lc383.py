import collections

ransomNote = "aa"
magazine = "aab"


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
