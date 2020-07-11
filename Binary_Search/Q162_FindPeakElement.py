'''

LeetCode Q.162 Find Peak Element

'''


def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    l = 0
    r = len(nums)-1

    while l < r:
        mid = (l+r)//2
        if nums[mid] > nums[mid+1]:
            r = mid
        else:
            l = mid+1
    return l


if __name__ == '__main__':

    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))
