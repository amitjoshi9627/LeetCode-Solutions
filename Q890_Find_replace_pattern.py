'''

LeetCode Strings Q.890 Find and Replace Pattern

'''


def findAndReplacePattern(words, pattern):

    d2 = {pattern[0]: 0}
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            continue
        else:
            d2[pattern[i+1]] = i+1

    d = {j: i for i, j in d2.items()}
    ans = []
    for word in words:
        copy = word[:]
        pat_copy = pattern[:]
        for i in d:
            word = word.replace(word[i], d[i].upper())
            pat_copy = pat_copy.replace(d[i], d[i].upper())

        if word == pat_copy:
            ans.append(copy)
    return ans


if __name__ == '__main__':

    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(findAndReplacePattern(words, pattern))
