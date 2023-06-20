# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Create a dictionary to store the count of each character in s
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Iterate over each character in t and decrement its count in the dictionary
        # If any character count becomes negative or doesn't exist in the dictionary, it's not an anagram
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False

        # Check if all character counts in the dictionary are zero
        for count in char_count.values():
            if count != 0:
                return False

        # If all checks pass, t is an anagram of s
        return True
