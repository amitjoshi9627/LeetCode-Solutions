'''

LeetCode Strings Q.415 Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Without using builtin libraries.

'''


def addStrings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    def solve(num1, num2):

        n1 = len(num1)
        n2 = len(num2)
        i = 0
        ans = ''
        carry = 0
        while i < n1:
            res = int(num1[i])+int(num2[i])+carry
            carry = 0

            if res <= 9:
                ans = str(res) + ans[:]
            else:
                res = str(res)
                ans = str(res[1]) + ans[:]
                carry = int(res[0])
            i += 1

        if n1 == n2:
            if carry:
                ans = str(carry) + ans[:]
                carry = 0
        else:
            i = n1
            while carry:
                res = carry + int(num2[i])
                carry = 0

                if res <= 9:
                    ans = str(res) + ans[:]
                else:
                    res = str(res)
                    ans = str(res[1]) + ans[:]
                    carry = int(res[0])

                i += 1
                if i == n2:
                    if carry:
                        ans = str(carry) + ans[:]
                        carry = 0
            while i < n2:
                ans = num2[i] + ans[:]
                i += 1
        return ans

    if len(num1) <= len(num2):
        return solve(num1, num2)
    else:
        return solve(num2, num1)


if __name__ == '__main__':

    num1 = "199"
    num2 = "99"

    print(addStrings(num1, num2))
