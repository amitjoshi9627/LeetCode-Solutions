'''

LeetCode Strings Q.20 Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.


'''


def isValid(s):

    stack = []
    open = ['(', '{', '[']
    close = {'(': ')', '{': '}', '[': ']'}

    for i in s:
        if i in open:
            stack.append(i)
        else:
            if not stack:
                return False
            if not close[stack.pop()] == i:
                return False

    if not stack:
        return True
    return False


if __name__ == '__main__':

    s = '[[(()){}]]'
    print(isValid(s))
