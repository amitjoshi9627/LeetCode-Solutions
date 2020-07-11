'''

LeetCode Arrays Q.167

Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

'''


def twoSum(numbers, target):

    i = 0
    j = len(numbers) - 1

    while i < j:

        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]

        if numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1


if __name__ == '__main__':

    numbers = [2, 7, 11, 15]
    target = 9

    print(twoSum(numbers, target))
