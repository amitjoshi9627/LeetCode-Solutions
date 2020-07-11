'''

LeetCode Q.1189 Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

'''


def maxNumberOfBalloons(text):

    d = {i: text.count(i) for i in 'balon'}

    d['l'] //= 2
    d['o'] //= 2

    return min(d.values())


if __name__ == '__main__':

    text = 'sebsoalolon'
    print(maxNumberOfBalloons(text))
