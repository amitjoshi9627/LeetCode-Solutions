'''

LeetCode Strings Q.1347 Minimum Number of Steps to Make Two Strings Anagram

'''


def minSteps(s, t):

    ans = 0
    for i in set(s):
        ans += max(s.count(i) - t.count(i), 0)
    return ans


if __name__ == '__main__':

    s = 'leetcode'
    t = 'practice'

    print(minSteps(s, t))
