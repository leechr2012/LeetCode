# https://leetcode.com/problems/valid-palindrome/submissions/966937235/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(i for i in s if i.isalnum())
        rev = ''.join(reversed(cleaned_string))
        if cleaned_string.lower() == rev.lower():
            return True
        else:
            return False 
