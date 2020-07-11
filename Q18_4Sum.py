'''

LeetCode Q.18 4Sum

Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

'''


def fourSum(nums, target):

    n = len(nums)
    nums.sort()
    ans = set()
    for l in range(n):
        for i in range(l+1, n):

            j = i+1
            k = n-1

            while j < k:
                if nums[l] + nums[i] + nums[j] + nums[k] == target:
                    ans.add((nums[l], nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[l] + nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1

    return list(ans)


if __name__ == '__main__':

    nums = [1, 0, -1, 0, -2, 2]
    print(fourSum(nums, 0))
