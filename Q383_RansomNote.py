'''

LeetCode Strings Q.383 Ransom Note

'''


def canConstruct(ransomNote, magazine):

    d1 = {i: magazine.count(i) for i in set(magazine)}
    d2 = {i: ransomNote.count(i) for i in set(ransomNote)}

    for i in d2:

        if i in d1:
            if d1[i] - d2[i] < 0:
                return False
        else:
            return False
    return True


if __name__ == '__main__':

    s1 = 'aaa'
    s2 = 'ababab'

    print(canConstruct(s1, s2))
