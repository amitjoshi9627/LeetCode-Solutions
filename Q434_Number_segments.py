'''

LeetCode Strings Q.434 Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters


'''


def countSegments(s):

    if s == "":
        return 0
    s = " ".join(s.strip().split())
    seg = s.split(" ")
    return len(seg)


if __name__ == '__main__':

    s = "Hello, my name is John!"
    print(countSegments(s))
