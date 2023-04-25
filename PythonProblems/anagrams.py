# Write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the strings are anagrams.
# Anagrams are strings that contain the same characters, but in any order.


#Solution1 w/ Time complexity of O(n^2):
def anagrams(s1, s2):
  j = 0
  if len(s1) != len(s2):
    return False
  else:
    while j < len(s1):
      if s1[j] in s2 and s1.count(s1[j]) == s2.count(s1[j]):
        j += 1
      else:
          return False
    return True

#Solution2 w/ Time Complexity of O(n+m):
  def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

  def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count

#solution3 using built in Counter method:
from collections import Counter

def anagrams(s1, s2):
   return Counter(s1) == Counter(s2)
