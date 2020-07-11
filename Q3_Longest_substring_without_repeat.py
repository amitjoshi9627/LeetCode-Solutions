'''

LeetCode Strings Q.3 Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

'''


def lengthOfLongestSubstring(s):

    if s == '':
        return 0
    if len(s) == 1:
        return 1

    a = ''
    ans = 0

    for i in range(len(s)):

        if s[i] not in a:
            a += s[i]
        else:
            ind = a.index(s[i])
            a = a[ind+1:]
            a += s[i]
        ans = max(len(a), ans)
    return ans


if __name__ == '__main__':

    s = 'abcabcabcd'
    print(lengthOfLongestSubstring(s))
