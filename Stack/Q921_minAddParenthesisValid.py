'''

LeetCode Stack Q.921 Minimum Add to Make Parentheses Valid 

'''


def minAddToMakeValid(S):

    stack = []
    ans = 0
    for i in S:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop(-1)
            else:
                ans += 1
    ans += len(stack)
    return ans


if __name__ == '__main__':

    S = "()))(("
    print(minAddToMakeValid(S))
