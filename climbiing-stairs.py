#https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 or n == 3:
            return n
        numWays = [1,2,3]
        for i in range(3,n):
            numWays.append(numWays[i-1] + numWays[i-2])
        return numWays[n-1]
