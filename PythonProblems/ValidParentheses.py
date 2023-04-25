# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                # The line above checks whether the stack is empty of not.
                # If the stack is not empty, it pops the top element from the stack
                # and assigns it to 'top_element'.
                if mapping[char] != top_element:
                    return False
                # checks whether the top_element popped from the stack is
                # the corresponding opening bracket for the current closing
                #  bracket char. If top_element is not the corresponding opening bracket,
                # then the function returns False because the brackets are not valid.
            else:
                stack.append(char)
        return not stack

# This implementation uses a stack data structure to keep track of the opening brackets
# that have not been matched with a closing bracket yet. It iterates over each character
# in the input string and performs the following steps:

# If the character is a closing bracket, it checks if the corresponding opening bracket
# is at the top of the stack. If it is, it pops the opening bracket from the stack.
# If not, it returns False because the brackets are not valid.

# If the character is an opening bracket, it pushes it onto the stack.

# If the character is not a bracket, it ignores it.

# At the end of the iteration, if the stack is empty,
# it means that all the opening brackets have been matched
# with their corresponding closing brackets, and the input string is valid.
# Otherwise, there are some opening brackets that were not matched with a
# closing bracket, and the input string is not valid.

# The time complexity of this implementation is O(n),
# where n is the length of the input string,
# because it iterates over the string once and
# performs constant-time operations on the stack and dictionary.
# The space complexity is also O(n), because in the worst case,
# the stack could contain all the opening brackets in the string.
