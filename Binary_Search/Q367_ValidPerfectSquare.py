'''

LeetCode Binary Search Q.367 Valid Perfect Square

A solution without using any built-in library such as sqrt

'''


def isPerfectSquare(num):
    if num == 0 or num == 1:
        return True
    l = 1
    r = num

    while l <= r:
        mid = (l+r)//2
        res = mid * mid
        if res == num:
            return True
        if res < num:
            l = mid+1
        else:
            r = mid-1
    return False


if __name__ == '__main__':

    num = 144
    print(isPerfectSquare(num))
