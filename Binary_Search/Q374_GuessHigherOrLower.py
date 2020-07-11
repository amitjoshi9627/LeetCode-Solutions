'''

LeetCode Binary Search Q.374 Guess Number Higher or Lower

'''


class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        r = n
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n

        while l < r:
            mid = (l+r)//2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:
                l = mid+1
            else:
                r = mid-1
        return l
