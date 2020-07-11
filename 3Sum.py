'''

LeetCode Arrays Q.15 3Sum

Given an array nums of n integers,
are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero

'''


def threeSum(nums, n):

    nums.sort()
    ans = set()
    for i in range(n):
        j = i+1
        k = n-1

        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                ans.add((nums[i], nums[j], nums[k]))
                j += 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

    return list(ans)


if __name__ == '__main__':

    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums, len(nums)))
