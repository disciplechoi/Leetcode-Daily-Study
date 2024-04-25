class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letter_cnt = collections.defaultdict(int)

        for i in range(0, len(s)):
            letter_cnt[s[i]] += 1

        for i in range(0, len(t)):
            letter_cnt[t[i]] -= 1

        for key in letter_cnt.values():
            if key != 0:
                return False

        return True
