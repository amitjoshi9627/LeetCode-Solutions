'''
LeetCode Q.1170 Compare Strings by Frequency of the Smallest Character

'''

def numSmallerByFrequency(queries, words):

    def bin_search(arr, t):
        l = 0
        r = len(arr)-1

        while l <= r:
            mid = (l+r)//2
            if l == r:
                if arr[mid] > t:
                    return len(arr) - mid
                elif arr[mid] == t:
                    return len(arr) - mid - 1
                else:
                    break
            if (arr[mid] <= t and arr[mid+1] > t):
                return len(arr) - mid-1
            if (arr[mid-1] <= t and arr[mid] > t):
                return len(arr) - mid
            elif arr[mid] <= t:
                l = mid+1
            else:
                r = mid-1
        return 0

    def f(s):

        smallest = min(s)
        return s.count(smallest)

    arr1 = [f(i) for i in queries]
    arr2 = sorted([f(i) for i in words])

    ans = [0] * len(arr1)
    for ind, i in enumerate(arr1):

        ans[ind] = bin_search(arr2, i)

    return ans


if __name__ == '__main__':

    queries = ["cbd"]
    words = ["zaaaz"]

    print(numSmallerByFrequency(queries, words))
