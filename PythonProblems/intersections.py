# Write a function, intersection, that takes in two lists, a,b, as arguments.
# The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

#SOLUTION 1 w/ time complexity of O(nm):
def intersection(a, b):
  new_list = []
  for num in a:
    if num in b:
      new_list.append(num)
  return new_list

#Solution2:
def intersection(a, b):
  result = []
  items_set = set()

  for item in a:
    items_set.add(item)

  for ele in b:
    if ele in items_set:
      result.append(ele)

  return result

#Solution3 w/ time complexity of O(N):
def intersection(a, b):
  set_a = set(a)
  return [ item for item in b if item in set_a ]
