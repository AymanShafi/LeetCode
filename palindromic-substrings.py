#https://leetcode.com/problems/palindromic-substrings/description/
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        count = 0
        for i in range(length):
            l,r = i,i
            while l>=0 and r < length and s[l]==s[r]:
                count += 1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r < length and s[l]==s[r]:
                count += 1
                l-=1
                r+=1
        return count
