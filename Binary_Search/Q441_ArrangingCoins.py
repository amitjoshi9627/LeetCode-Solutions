'''

LeetCode Binary Search Q.441 Arranging Coins

'''


def arrangeCoins(n):

    if n == 1 or n == 0:
        return n
    l = 1
    r = n

    while l < r:
        mid = (l+r)//2
        res = (mid * (mid+1))//2
        if res == n:
            return mid
        if res < n:
            l = mid+1
        else:
            r = mid
    return l-1


if __name__ == '__main__':

    n = 10
    print(arrangeCoins(n))
