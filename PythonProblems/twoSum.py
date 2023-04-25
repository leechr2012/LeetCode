# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i

# The time complexity of this function is O(n), where n is the length of the input list nums. This is because the function iterates through the input list once, performing a constant amount of work (O(1)) for each element in the list.

# Within the loop, the function performs a constant amount of work for each element, including a dictionary lookup and insertion operation. Since dictionary operations are average-case O(1) time complexity (with worst-case O(n)), the overall time complexity of the function is O(n).

# Therefore, this function has a linear time complexity, meaning that the time required to run the function increases linearly with the size of the input list.
