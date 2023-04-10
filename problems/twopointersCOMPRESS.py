# Write a function, compress, that takes in a string as an argument.
# The function should return a compressed version of the string where consecutive
# occurrences of the same characters are compressed into the number of occurrences
# followed by the character. Single character occurrences should not be changed.

def compress(s):
    s += '!'
    result = ''
    i = 0
    j = 0
    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
          num = j - i
          if num == 1:
            result += s[i]
          else:
            result += str(num) + s[i]
          i = j

    return result
