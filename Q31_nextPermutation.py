'''

LeetCode Arrays Q.31 Next Permutation

Implement next permutation,
which rearranges numbers into the lexicographically next greater permutation of numbers.

'''


def nextPermutation(nums):

    if sorted(nums, reverse=True) != nums[:]:
        ind = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                ind = i
        next_greater = -1
        for i in range(ind+1, len(nums)):
            if nums[ind] < nums[i]:
                next_greater = i
        nums[ind], nums[next_greater] = nums[next_greater], nums[ind]
        nums[:] = nums[:ind+1] + nums[ind+1:][::-1]
    else:
        nums[:] = nums[::-1]

    return nums


if __name__ == '__main__':

    nums = [1, 2, 3, 5, 4]
    print(nextPermutation(nums))
