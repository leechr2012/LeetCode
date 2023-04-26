# Write a function, most_frequent_char, that takes in a string as an argument.
# The function should return the most frequent character of the string.
# If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

###Solution1: Time Complexity O(n)###
def most_frequent_char(s):
    return char_count(s)

def char_count(s):
    count = {}
    for char in s:
        if char not in s:
            count[char] = 0
            count[char] += 1
        else:
            count[char] += 1
    return max(count, key = count.get)

#The time complexity is O(n) because the function iterates through the characters in the string
# once to count their frequencies using a dictionary, which takes O(n) time.
# Then, finding the character with the highest frequency using max(count, key=count.get)
# also takes O(n) time since it iterates through the dictionary to find the maximum value.
# Therefore, the total time complexity of the function is O(n) + O(n) = O(2n),
# which simplifies to O(n).

###Solution2###
def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None
    for char in s:
        if best is None and count[char] > count[best]:
            best = char
    return best

###Solution3###
from collections import Counter

def most_frequent_char(s):
    count = Counter(s)

    best = None
    for char in s:
        if best is None and count[char] > count[best]:
            best = char
    return best
