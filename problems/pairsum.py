# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements sum to the given target.
# The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.


###solution###
def pair_sum(numbers, target_sum):
  map = {}
  for index, num in enumerate(numbers):
    diff = target_sum - num

    if diff in map:
      return(index, map[diff])

    map[num] = index

#The time complexity of this function is O(n), where n is the length of the input list numbers.
# This is because the function iterates through the list once to build a dictionary/map of each element and its index.
# Then, for each element, it checks whether the difference between the target sum and the element is already in the map.
# If so, it returns the indices of the pair that add up to the target sum.
# Otherwise, it adds the element to the map.
# Since the dictionary/map operations take constant time on average,
# the overall time complexity of the function is linear in the length of the input list.
