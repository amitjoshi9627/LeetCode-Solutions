'''

LeetCode Binary Search Q69 Sqrt(x)

Implementation of int(sqrt(x))

'''


def mySqrt(x):

    if x <= 1:
        return x
    l = 1
    r = x
    while l < r:
        mid = (l+r)//2
        res = mid*mid
        if res == x:
            return mid
        if res > x:
            r = mid
        else:
            l = mid+1
    return l-1


if __name__ == '__main__':

    num = 86
    print(mySqrt(num))
