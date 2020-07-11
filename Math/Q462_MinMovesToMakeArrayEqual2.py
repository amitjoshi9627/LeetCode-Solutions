'''

LeetCode Math Q.462 Min Moves to make array equal -II

'''


def minMoves2(nums):

    res = 0

    nums.sort()
    if len(nums) % 2 != 0:
        median = nums[len(nums)//2]
    else:
        a = nums[len(nums)//2]
        b = nums[len(nums)//2-1]
        median = (a+b) // 2
    for i in nums:
        res += abs(median - i)
    return res


if __name__ == '__main__':

    nums = [1, 2, 3]
    print(minMoves2(nums))
